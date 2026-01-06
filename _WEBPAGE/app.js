import { KNIGHTS, KNIGHT_SPECS, COMMON_ITEMS, QUESTIONS } from './data.js';

// --- HELPERS ---
function getKnightItems(knightName) {
    const specs = KNIGHT_SPECS[knightName];
    if (specs && specs.items) {
        const filteredItems = specs.items.filter(item => item.type !== 'knight');
        return [...COMMON_ITEMS, ...filteredItems];
    }
    return [...COMMON_ITEMS, { type: "weapon", name: "Knightly Weapon", damage: "d8" }, { type: "shield", name: "Shield", armor: 1 }, { type: "coat", name: "Mail Armour", armor: 1 }];
}

function getKnightActors(knightName) {
    const specs = KNIGHT_SPECS[knightName];
    if (specs && specs.actors) return specs.actors;
    return [];
}

function getKnightTables(knightName) {
    const specs = KNIGHT_SPECS[knightName];
    if (specs && specs.tables) return specs.tables;
    return [];
}

function getKnightFlavorHeader(knightName) {
    const specs = KNIGHT_SPECS[knightName];
    if (specs && specs.items) {
        const knightItem = specs.items.find(i => i.type === "knight");
        if (knightItem && knightItem.flavor) return knightItem.flavor;
    }
    return "Details";
}

const Dice = {
    roll: (sides) => Math.floor(Math.random() * sides) + 1,
    parse: (formula) => {
        let total = 0;
        const parts = formula.toLowerCase().replace(/\s/g, '').split('+');
        parts.forEach(part => {
            if (part.includes('d')) {
                const [count, sides] = part.split('d');
                const num = count === '' ? 1 : parseInt(count);
                const s = parseInt(sides);
                for (let i = 0; i < num; i++) total += Math.floor(Math.random() * s) + 1;
            } else {
                total += parseInt(part);
            }
        });
        return total;
    }
};

const cleanText = (text) => {
    if (!text) return "";
    return text.replace(/\[\[\/r\s(.*?)\s.*?\]\]/g, "$1").replace(/\[\[.*?\]\]/g, "");
};

// --- GAME LOGIC ---
const game = {
    scores: {},
    answerHistory: [],
    isTurning: false,

    init: function() {
        console.log("Initializing Game (V14 - Medieval & Ink)...");
        KNIGHTS.forEach(k => this.scores[k.name] = 0);
        this.answerHistory = [];
        this.isTurning = false;
        
        $('#book-viewport').addClass('animate-toss');

        this.buildBook();
        this.setupHandlers();
        this.resizeBook();
        this.setupResizeHandler();
    },

    setupHandlers: function() {
        const book = $('#book');
        
        // 1. ANSWERS (With visual feedback)
        book.off('click').on('click', '.answer-btn', (e) => {
            e.stopPropagation();
            if (this.isTurning) return;
            
            const btn = $(e.currentTarget);
            btn.addClass('circled'); // Add Ink Circle
            
            const tags = JSON.parse(decodeURIComponent(btn.data('tags')));
            const idx = btn.data('idx');
            
            // Short delay to see the circle before turning
            setTimeout(() => {
                this.handleAnswer(tags, idx);
            }, 300);
        });

        // 2. QUILL START BUTTON
        book.on('click', '.btn-quill-start', (e) => {
            e.stopPropagation();
            if (this.isTurning) return;
            
            const quill = $(e.currentTarget);
            quill.addClass('quill-picked-up');
            
            setTimeout(() => {
                this.forceTurn(4);
            }, 500);
        });

        // 3. CLASP (Fixed Slow Open)
        book.on('click', '.book-clasp', (e) => {
            e.stopPropagation();
            if (this.isTurning) return;
            
            const clasp = $(e.currentTarget);
            clasp.addClass('open');
            
            // Wait for clasp slide (600ms)
            setTimeout(() => {
                // Set Slow Duration
                $('#book').turn('options', { duration: 2500 });
                
                // Small buffer to ensure option applies
                setTimeout(() => {
                    this.forceTurn(2); // Turn Cover
                    
                    // Reset duration back to normal after the slow turn finishes
                    setTimeout(() => {
                        $('#book').turn('options', { duration: 600 });
                    }, 2500);
                }, 50);
            }, 600);
        });

        // 4. OATH BUTTON
        book.on('click', '.oath-btn', (e) => {
            e.stopPropagation();
            if (this.isTurning) return;
            this.finishGame();
        });

        $('body').on('click', '.reset-btn', (e) => { e.preventDefault(); this.burnAndReset(); });
        book.bind("turned", (event, page, view) => { this.isTurning = false; });
        book.bind("start", (event, pageObject, corner) => { if (corner) event.preventDefault(); });
    },

    buildBook: function() {
        const book = $('#book');
        book.empty();

        // COVER
        const coverPage = $(`
            <div class="page hard">
                <div class="book-clasp"></div>
                <div class="card-inner" style="align-items: center; justify-content: center;">
                    <h1>Mythic Bastionland</h1>
                </div>
            </div>
        `);
        book.append(coverPage);

        // INTRO SPREAD (Poem & Quill)
        book.append($(`
            <div class="page">
                <div class="card-inner" style="justify-content: center; text-align: center; padding: 4rem;">
                    <p class="font-medieval">
                        On cold misten hills, beast witsome and fell<br>
                        In holdings and havens the vassals adwell<br>
                        Seers know the all, the start and the end<br>
                        Myths hushed aloud to which truth must abend
                    </p>
                    <br>
                    <p class="font-medieval">
                        Aside vagabonds on snakelene trails<br>
                        Knights render these stories awrenched from their veils<br>
                        For the oath, for the glory, through sorrow and ache<br>
                        The City, that quest to which no knight can make
                    </p>
                </div>
            </div>
        `));
        
        const beginPage = $(`
            <div class="page">
                <div class="card-inner" style="justify-content: center; align-items: center;">
                    <button class="btn-quill-start" title="Begin Journey"></button>
                </div>
            </div>
        `);
        book.append(beginPage);

        // QUESTIONS
        QUESTIONS.forEach((q, idx) => {
            const leftPage = $(`
                <div class="page">
                    <div class="card-inner">
                        <h2>Question ${idx + 1}</h2>
                        <p style="font-size: 1.6rem; font-style: italic;">"${q.text}"</p>
                        <div style="text-align: center; margin-top: auto; font-size: 0.9rem; opacity: 0.6;">
                            ${idx + 1} / ${QUESTIONS.length}
                        </div>
                    </div>
                </div>
            `);
            const rightPage = $(`
                <div class="page">
                    <div class="card-inner">
                        <div class="options-container" id="q-options-${idx}"></div>
                    </div>
                </div>
            `);
            const optContainer = rightPage.find(`#q-options-${idx}`);
            q.options.forEach((opt, optIdx) => {
                const tagString = encodeURIComponent(JSON.stringify(opt.tags));
                const btn = $(`<button class="btn answer-btn" data-idx="${optIdx}" data-tags="${tagString}">${opt.text}</button>`);
                optContainer.append(btn);
            });
            book.append(leftPage);
            book.append(rightPage);
        });

        // FINAL OATH PAGE
        book.append($('<div class="page"><div class="card-inner"><p class="font-medieval" style="text-align:center; font-size: 1.8rem; margin-top:50%;">SEEK THE MYTHS.<br>HONOUR THE SEERS.<br>PROTECT THE REALM.</p></div></div>'));
        
        const oathPage = $(`
            <div class="page">
                <div class="card-inner" style="justify-content: center; align-items: center;">
                    <button class="btn btn-hero oath-btn">Swear Your Oath</button>
                </div>
            </div>
        `);
        book.append(oathPage);

        book.turn({
            width: 1200, height: 800, display: 'double',
            acceleration: true, gradients: false, elevation: 50, duration: 600, 
            autoCenter: true, pages: 1 
        });
    },

    forceTurn: function(pageNumber) {
        this.isTurning = true;
        $('#book').turn('page', pageNumber);
        setTimeout(() => { if (this.isTurning) this.isTurning = false; }, 1500);
    },

    setupResizeHandler: function() { $(window).resize(() => this.resizeBook()); },
    
    resizeBook: function() {
        const winWidth = $(window).width();
        const winHeight = $(window).height();
        const targetRatio = 1200 / 800; 
        const screenRatio = winWidth / winHeight;
        let scale;
        if (screenRatio > targetRatio) scale = (winHeight * 0.95) / 800;
        else scale = (winWidth * 0.95) / 1200;
        $('#book-viewport').css({ 'transform': `scale(${scale})` });
    },

    handleAnswer: function(tags, optionIndex) {
        // isTurning check handled in handler
        this.answerHistory.push(optionIndex);
        KNIGHTS.forEach(knight => {
            let matchCount = 0;
            tags.forEach(tag => {
                if (knight.keywords.some(k => k.toLowerCase() === tag.toLowerCase())) matchCount += 3;
                else if (knight.keywords.some(k => k.toLowerCase().includes(tag.toLowerCase()))) matchCount += 1;
            });
            this.scores[knight.name] += matchCount;
        });

        if (this.answerHistory.length === QUESTIONS.length) {
            const finalPageNum = 3 + (QUESTIONS.length * 2) + 2; 
            this.forceTurn(finalPageNum);
        } else {
            const nextPageNum = 4 + (this.answerHistory.length * 2);
            this.forceTurn(nextPageNum);
        }
    },

    finishGame: function() {
        this.isTurning = true; 
        const rapidCloseInterval = setInterval(() => {
            const currentPage = $('#book').turn('page');
            if (currentPage > 1) {
                $('#book').turn('previous');
            } else {
                clearInterval(rapidCloseInterval);
                this.isTurning = false; 
                this.generateProfile();
                $('#result-sheet').addClass('rise-up');
            }
        }, 100); 
    },

    burnAndReset: function() {
        $('#result-sheet').addClass('burn-out');
        setTimeout(() => { location.reload(); }, 2000); 
    },

    generateProfile: function() {
        let maxScore = -1;
        let winners = [];
        for (const [name, score] of Object.entries(this.scores)) {
            if (score > maxScore) { maxScore = score; winners = [name]; }
            else if (score === maxScore) winners.push(name);
        }
        let winnerName = winners[0];
        if (winners.length > 1) {
            const hash = this.answerHistory.reduce((acc, val, idx) => acc + (val + 1) * (idx + 1), 0);
            winners.sort(); 
            winnerName = winners[hash % winners.length];
        }
        const knightData = KNIGHTS.find(k => k.name === winnerName);
        const inventory = getKnightItems(winnerName);
        const totalArmor = inventory.reduce((sum, item) => sum + (item.armor || 0), 0);
        
        const stats = {
            vigour: Dice.parse("d12+d6"),
            clarity: Dice.parse("d12+d6"),
            spirit: Dice.parse("d12+d6"),
            guard: Dice.parse("d6"),
            armor: totalArmor
        };

        const actors = getKnightActors(winnerName);
        const flavorHeader = getKnightFlavorHeader(winnerName);
        const tables = getKnightTables(winnerName);
        
        let flavorText = [];
        if (tables) {
            tables.forEach(table => {
                const roll = Dice.parse(table.formula || "d6");
                const result = table.results.find(r => roll >= r[0] && roll <= r[1]);
                if (result) {
                    flavorText.push({ label: table.name, text: cleanText(result[2]) });
                }
            });
        }

        this.renderResultSheet(knightData, stats, inventory, actors, flavorText, flavorHeader);
    },

    renderResultSheet: function(knight, stats, inventory, actors, flavorText, detailsHeader) {
        const container = $('#result-content');
        let html = `
            <div class="save-controls">
                <button class="btn" onclick="window.print()">Print Sheet</button>
                <button class="btn reset-btn">New Oath</button>
            </div>

            <div class="sheet-header">
                <h1>${knight.name}</h1>
                <div class="sheet-archetype">${knight.archetype}</div>
                <p><em>"${knight.description}"</em></p>
            </div>

            <div class="stat-grid">
                <div class="stat-box"><span class="stat-label">Vigour</span><span class="stat-value">${stats.vigour}</span></div>
                <div class="stat-box"><span class="stat-label">Clarity</span><span class="stat-value">${stats.clarity}</span></div>
                <div class="stat-box"><span class="stat-label">Spirit</span><span class="stat-value">${stats.spirit}</span></div>
                <div class="stat-box"><span class="stat-label">Guard</span><span class="stat-value">${stats.guard}</span></div>
                <div class="stat-box"><span class="stat-label">Armour</span><span class="stat-value">${stats.armor}</span></div>
            </div>

            <div class="sheet-columns">
                <div class="col">
                    <h3>Features</h3>
                    <div class="content-block">
                        <p><strong>Passion:</strong><br>${cleanText(knight.passion).replace("Passion:", "")}</p>
                    </div>
                    <div class="content-block">
                        <p><strong>Ability:</strong><br>${cleanText(knight.ability).replace("Ability:", "")}</p>
                    </div>
                </div>

                <div class="col">
                    <h3>Inventory</h3>
                    ${inventory.map(item => `
                        <div class="item-row">
                            <span class="item-name">${item.name}</span>
                            <span>${item.damage || ""} ${item.armor ? `(A${item.armor})` : ''}</span>
                        </div>
                    `).join('')}
                </div>

                <div class="col">
                    <h3>Companions</h3>
                    ${actors.length > 0 ? actors.map(actor => `
                        <div class="steed-box">
                            <strong>${actor.name}</strong> <small>(${actor.type})</small>
                            <div style="font-size: 0.85em; margin-top:0.2rem;">${actor.biography || ""}</div>
                             <div style="font-size: 0.8em; margin-top:0.2rem;">
                                V:${actor.vigour||"-"} C:${actor.clarity||"-"} S:${actor.spirit||"-"} G:${actor.guard||"-"}
                             </div>
                        </div>
                    `).join('') : '<p>None.</p>'}

                    <h3>${detailsHeader}</h3>
                    ${flavorText.length > 0 ? flavorText.map(f => `
                        <div class="flavor-item">
                            <span class="flavor-label">${f.label}: </span>
                            <span class="flavor-text">${f.text}</span>
                        </div>
                    `).join('') : '<p>None.</p>'}
                </div>
            </div>
            
            <div class="sheet-footer-quote">
                SEEK THE MYTHS &bull; HONOUR THE SEERS &bull; PROTECT THE REALM
            </div>
        `;

        container.html(html);
    }
};

$(document).ready(function() {
    game.init();
});