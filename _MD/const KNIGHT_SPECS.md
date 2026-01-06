 const KNIGHT_SPECS = {
        "The True Knight": {
            items: [{ type: "knight", flavor: "Symbol of Truth", flavorLabel1: "Trigger", flavorLabel2: "Effect" }, { type: "weapon", name: "Heavy Mace", damage: "d8", hefty: true }, { type: "shield", name: "Kite Shield", armor: 1, description: "Marked with a symbol of the truth" }, { type: "coat", name: "Chain Coat", armor: 1 }],
            actors: [{ type: "steed", name: "Petulant Steed", vigour: 10, clarity: 10, spirit: 5, guard: 5, biography: "Refuses to move if lied to." }],
            tables: [{ name: "Trigger", formula: "d6", results: [[1,1,"Lying about identity"], [2,2,"Giving false witness"], [3,3,"Malicious advice"], [4,4,"Lying while bearing shield"], [5,5,"Omitting key info"], [6,6,"Lying about intent"]] }, { name: "Effect", formula: "d6", results: [[1,1,"Golden Glow"], [2,2,"Turns Cold"], [3,3,"Gentle Hum"], [4,4,"Fragrant Aroma"], [5,5,"Distant Birdcall"], [6,6,"Loud Clang"]] }]
        },
        "The Snare Knight": {
            items: [{ type: "knight", flavor: "Knight & Companion", flavorLabel1: "History", flavorLabel2: "Type" }, { type: "weapon", name: "Short Bow", damage: "d6" }, { type: "misc", name: "Animal Trap" }, { type: "coat", name: "Leather Jerkin", armor: 1 }],
            actors: [{ type: "steed", name: "Tattered Steed", vigour: 8, clarity: 10, spirit: 5, guard: 2 }, { type: "npc", name: "Companion", vigour: 5, clarity: 10, spirit: 7, guard: 4, biography: "Partially understands human speech." }],
            tables: [{ name: "History", formula: "d6", results: [[1,1,"Exiled"], [2,2,"Feral"], [3,3,"Abandoned"], [4,4,"Lost"], [5,5,"Born here"], [6,6,"Hiding"]] }, { name: "Type", formula: "d6", results: [[1,1,"Otter"], [2,2,"Hare"], [3,3,"Rat"], [4,4,"Weasel"], [5,5,"Ferret"], [6,6,"Squirrel"]] }]
        },
        "The Tourney Knight": {
            items: [{ type: "knight", flavor: "Helm & Calling", flavorLabel1: "Calling", flavorLabel2: "Helm Design" }, { type: "weapon", name: "Greatlance", damage: "2d10", hefty: true }, { type: "weapon", name: "Javelin x2", damage: "d6" }, { type: "coat", name: "Arena Plate", armor: 1 }],
            actors: [{ type: "steed", name: "Horned Stallion", vigour: 12, clarity: 10, spirit: 5, guard: 4, biography: "d6 Trample" }],
            tables: [{ name: "Calling", formula: "d6", results: [[1,1,"Greed"], [2,2,"Bloodlust"], [3,3,"Glory"], [4,4,"Duty"], [5,5,"Pride"], [6,6,"Ambition"]] }, { name: "Helm Design", formula: "d6", results: [[1,1,"Lion"], [2,2,"Shark"], [3,3,"Great Crest"], [4,4,"Hawk"], [5,5,"Bull"], [6,6,"Demon"]] }]
        },
        "The Bloody Knight": {
            items: [{ type: "knight", flavor: "Rage Fuel", flavorLabel1: "Alcohol", flavorLabel2: "Hatred" }, { type: "weapon", name: "Longaxe", damage: "d10", long: true }, { type: "misc", name: "Sacks of Alcohol" }, { type: "coat", name: "Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Bullish Warhorse", vigour: 15, clarity: 5, spirit: 5, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Alcohol", formula: "d6", results: [[1,1,"Burning wine"], [2,2,"Strong mead"], [3,3,"Spiced ale"], [4,4,"Sour milk"], [5,5,"Fermented veg"], [6,6,"Blood brew"]] }, { name: "Hatred", formula: "d6", results: [[1,1,"The rich"], [2,2,"Knights"], [3,3,"The poor"], [4,4,"Seers"], [5,5,"The sea"], [6,6,"The sun"]] }]
        },
        "The Moss Knight": {
            items: [{ type: "knight", flavor: "Tattoos", flavorLabel1: "Design", flavorLabel2: "Effect" }, { type: "weapon", name: "Branch Cudgel", damage: "d8", hefty: true }, { type: "shield", name: "Buckler", armor: 1, description: "d4 damage" }, { type: "coat", name: "Mail Coif", armor: 1 }],
            actors: [{ type: "steed", name: "Pale Steed", vigour: 8, clarity: 12, spirit: 5, guard: 3 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Faded spirals"], [2,2,"Blue thorns"], [3,3,"Silver stars"], [4,4,"Colourful snakes"], [5,5,"Red bones"], [6,6,"Burnt rings"]] }, { name: "Effect", formula: "d6", results: [[1,1,"Points to water"], [2,2,"Burns before ambush"], [3,3,"A1 in saltwater"], [4,4,"A1 in moonlight"], [5,5,"A1 in rivers"], [6,6,"Conceals third eye"]] }]
        },
        "The War Knight": {
            items: [{ type: "knight", flavor: "Military Gear", flavorLabel1: "Polearm Trait", flavorLabel2: "Helm Style" }, { type: "weapon", name: "Special Polearm", damage: "d8", long: true }, { type: "misc", name: "Whalebone Chess Set" }, { type: "coat", name: "Splint", armor: 1 }],
            actors: [{ type: "steed", name: "Stocky Steed", vigour: 15, clarity: 8, spirit: 5, guard: 2 }],
            tables: [{ name: "Polearm Trait", formula: "d6", results: [[1,1,"+d10 vs mounted"], [2,2,"+d10 vs shielded"], [3,3,"+d10 vs armored"], [4,4,"+d10 vs unshielded"], [5,5,"+d10 vs beasts"], [6,6,"+d10 vs attackers"]] }, { name: "Helm Style", formula: "d6", results: [[1,1,"Veiled leather"], [2,2,"Mail hood"], [3,3,"Bucket"], [4,4,"Crow-beaked"], [5,5,"Caged visor"], [6,6,"Kettle cap"]] }]
        },
        "The Willow Knight": {
            items: [{ type: "knight", flavor: "Memories", flavorLabel1: "Place", flavorLabel2: "Disaster" }, { type: "weapon", name: "Old Sword", damage: "d8", hefty: true }, { type: "shield", name: "Half-shield", armor: 1 }, { type: "coat", name: "Gambeson", armor: 1 }],
            actors: [{ type: "steed", name: "Cautious Steed", vigour: 10, clarity: 15, spirit: 5, guard: 2 }],
            tables: [{ name: "Place", formula: "d6", results: [[1,1,"Riverside"], [2,2,"Coastal"], [3,3,"Mountain"], [4,4,"Pine forest"], [5,5,"Moor"], [6,6,"Castle"]] }, { name: "Disaster", formula: "d6", results: [[1,1,"Death"], [2,2,"War"], [3,3,"Famine"], [4,4,"Plague"], [5,5,"Fire"], [6,6,"Flood"]] }]
        },
        "The Gilded Knight": {
            items: [{ type: "knight", flavor: "The Cost", flavorLabel1: "Found At", flavorLabel2: "Left Behind" }, { type: "weapon", name: "Great Mace", damage: "d10", long: true }, { type: "coat", name: "Gold Cloaked Plate", armor: 1 }, { type: "misc", name: "Gold Mask" }],
            actors: [{ type: "steed", name: "Majestic Charger", vigour: 12, clarity: 9, spirit: 12, guard: 4, biography: "d6 Trample" }],
            tables: [{ name: "Found At", formula: "d6", results: [[1,1,"Lake"], [2,2,"Waterfall"], [3,3,"River"], [4,4,"Beach"], [5,5,"Cave"], [6,6,"Mountain"]] }, { name: "Left Behind", formula: "d6", results: [[1,1,"A farm"], [2,2,"A name"], [3,3,"Only graves"], [4,4,"A student"], [5,5,"A teacher"], [6,6,"A castle"]] }]
        },
        "The Saddle Knight": {
            items: [{ type: "knight", flavor: "Loyal Steed", flavorLabel1: "Appearance", flavorLabel2: "Temperament" }, { type: "weapon", name: "Rider's Axe x3", damage: "d6" }, { type: "misc", name: "Fine Saddle" }, { type: "coat", name: "Rider's Plate", armor: 1 }],
            actors: [{ type: "steed", name: "Beloved Steed", vigour: 12, clarity: 15, spirit: 7, guard: 4 }],
            tables: [{ name: "Appearance", formula: "d6", results: [[1,1,"Pristine"], [2,2,"Plaited"], [3,3,"Tall"], [4,4,"Golden"], [5,5,"Dark"], [6,6,"Stocky"]] }, { name: "Temperament", formula: "d6", results: [[1,1,"Silent"], [2,2,"Alert"], [3,3,"Valiant"], [4,4,"Fierce (d8 trample)"], [5,5,"Loved by beasts"], [6,6,"Perfect direction"]] }]
        },
        "The Riddle Knight": {
            items: [{ type: "knight", flavor: "False Form", flavorLabel1: "Body", flavorLabel2: "Visage" }, { type: "weapon", name: "Twisted Bow", damage: "d6", long: true }, { type: "misc", name: "Moon Pendant" }, { type: "coat", name: "Light Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Shadowy Horse", vigour: 8, clarity: 15, spirit: 5, guard: 2, biography: "Very quiet" }],
            tables: [{ name: "Body", formula: "d6", results: [[1,1,"Muscular"], [2,2,"Shrunken"], [3,3,"Stretched"], [4,4,"Skeletal"], [5,5,"Canine"], [6,6,"Feline"]] }, { name: "Visage", formula: "d6", results: [[1,1,"Elderly"], [2,2,"Youthful"], [3,3,"Hideous"], [4,4,"Amorphous"], [5,5,"Horned"], [6,6,"Regal"]] }]
        },
        "The Talon Knight": {
            items: [{ type: "knight", flavor: "Loyal Bird", flavorLabel1: "Breed", flavorLabel2: "Training" }, { type: "weapon", name: "Hookhammer", damage: "d8", hefty: true }, { type: "shield", name: "Shield-Gauntlet", armor: 1, description: "d6 damage" }, { type: "coat", name: "Mail", armor: 0 }],
            actors: [{ type: "steed", name: "Old Steed", vigour: 8, clarity: 8, spirit: 7, guard: 2 }, { type: "npc", name: "Bird", vigour: 5, clarity: 10, spirit: 5, guard: 4, biography: "d4 Talons" }],
            tables: [{ name: "Breed", formula: "d6", results: [[1,1,"Fisherhawk"], [2,2,"Cave Owl"], [3,3,"Grey Raven"], [4,4,"Red Eagle"], [5,5,"Rock Falcon"], [6,6,"Bog Vulture"]] }, { name: "Training", formula: "d6", results: [[1,1,"Singing"], [2,2,"Fighting Humans"], [3,3,"Silent Flight"], [4,4,"Delivery"], [5,5,"Stealing"], [6,6,"Fighting Birds"]] }]
        },
        "The Barbed Knight": {
            items: [{ type: "knight", flavor: "Bad Reputation", flavorLabel1: "Ally", flavorLabel2: "Enemy" }, { type: "weapon", name: "Jagged Spear", damage: "d8", hefty: true }, { type: "weapon", name: "Hunting Bow", damage: "d6", long: true }, { type: "coat", name: "Red Cloaked Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Vicious Charger", vigour: 12, clarity: 8, spirit: 5, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Ally", formula: "d6", results: [[1,1,"Eccentric Alchemist"], [2,2,"Humble Chronicler"], [3,3,"Surly Brewer"], [4,4,"Horse Breeder"], [5,5,"Elderly Innkeeper"], [6,6,"Petty Burglar"]] }, { name: "Enemy", formula: "d6", results: [[1,1,"Rich Merchant"], [2,2,"Master Blacksmith"], [3,3,"Admired Knight"], [4,4,"Bandit Leader"], [5,5,"Retired General"], [6,6,"Mercenary Captain"]] }]
        },
        "The Trail Knight": {
            items: [{ type: "knight", flavor: "Personal Code", flavorLabel1: "Value", flavorLabel2: "Forged By" }, { type: "weapon", name: "Crow-beak Axe", damage: "d8", hefty: true }, { type: "misc", name: "Sanguine Lens" }, { type: "coat", name: "Beaten Gambeson", armor: 1 }],
            actors: [{ type: "steed", name: "Serene Steed", vigour: 10, clarity: 13, spirit: 5, guard: 3 }],
            tables: [{ name: "Value", formula: "d6", results: [[1,1,"Honour"], [2,2,"Duty"], [3,3,"Loyalty"], [4,4,"Justice"], [5,5,"Respect"], [6,6,"Truth"]] }, { name: "Forged By", formula: "d6", results: [[1,1,"Battling Monster"], [2,2,"Raided Village"], [3,3,"Rescuing Helpless"], [4,4,"Killing Tyrant"], [5,5,"Long Journey"], [6,6,"Facing Temptation"]] }]
        },
        "The Amber Knight": {
            items: [{ type: "knight", flavor: "Pastime", flavorLabel1: "Hobby", flavorLabel2: "Taught By" }, { type: "weapon", name: "Ancient Greatblade", damage: "2d10", slow: true }, { type: "misc", name: "Amber Amulet" }, { type: "coat", name: "Ancient Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Loyal Steed", vigour: 10, clarity: 10, spirit: 5, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Hobby", formula: "d6", results: [[1,1,"Painting"], [2,2,"Miniature sculpture"], [3,3,"Embroidery"], [4,4,"Pottery"], [5,5,"Drawing"], [6,6,"Flower pressing"]] }, { name: "Taught By", formula: "d6", results: [[1,1,"Knight-Mentor"], [2,2,"Father"], [3,3,"Mother"], [4,4,"Brother"], [5,5,"Sister"], [6,6,"Self"]] }]
        },
        "The Horde Knight": {
            items: [{ type: "knight", flavor: "Taste of Home", flavorLabel1: "Flavour", flavorLabel2: "Substance" }, { type: "weapon", name: "Blunt Sword", damage: "d8", hefty: true }, { type: "misc", name: "Sack of Food" }, { type: "coat", name: "Ringed Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Beastly Steed", vigour: 15, clarity: 7, spirit: 5, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Flavour", formula: "d6", results: [[1,1,"Sour"], [2,2,"Salty"], [3,3,"Fiery"], [4,4,"Smoked"], [5,5,"Burnt"], [6,6,"Chewy"]] }, { name: "Substance", formula: "d6", results: [[1,1,"Skin"], [2,2,"Beans"], [3,3,"Insects"], [4,4,"Roots"], [5,5,"Cheese"], [6,6,"Honey"]] }]
        },
        "The Emerald Knight": {
            items: [{ type: "knight", flavor: "Hidden Action", flavorLabel1: "Action", flavorLabel2: "Sense" }, { type: "weapon", name: "Branchspear", damage: "d8", hefty: true }, { type: "shield", name: "Shield", armor: 1, description: "d4 damage" }, { type: "coat", name: "Cloaked Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Sable Steed", vigour: 10, clarity: 14, spirit: 5, guard: 4 }],
            tables: [{ name: "Action", formula: "d6", results: [[1,1,"Strike enemy"], [2,2,"Animal calls"], [3,3,"Throw stones"], [4,4,"Grab enemy"], [5,5,"Move slowly"], [6,6,"Whisper"]] }, { name: "Sense", formula: "d6", results: [[1,1,"Vision (detail)"], [2,2,"Vision (distance)"], [3,3,"Hearing"], [4,4,"Smell"], [5,5,"Weather"], [6,6,"Emotion"]] }]
        },
        "The Chain Knight": {
            items: [{ type: "knight", flavor: "Reaching Surface", flavorLabel1: "First", flavorLabel2: "Then" }, { type: "weapon", name: "Pronged Mace", damage: "d8", hefty: true }, { type: "misc", name: "Iron Chain" }, { type: "coat", name: "Oubliette Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Tired Steed", vigour: 10, clarity: 12, spirit: 3, guard: 3 }],
            tables: [{ name: "First", formula: "d6", results: [[1,1,"Darkness"], [2,2,"Smoke"], [3,3,"Cell"], [4,4,"Chains"], [5,5,"Stairs"], [6,6,"Fire"]] }, { name: "Then", formula: "d6", results: [[1,1,"Ice"], [2,2,"Dirt"], [3,3,"Mountain"], [4,4,"Tomb"], [5,5,"Well"], [6,6,"Lake"]] }]
        },
        "The Banner Knight": {
            items: [{ type: "knight", flavor: "Banner", flavorLabel1: "Design", flavorLabel2: "Topper" }, { type: "weapon", name: "Banner-pike", damage: "d10", long: true }, { type: "weapon", name: "Spikehammer", damage: "d6" }, { type: "coat", name: "Ornate Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Fat Steed", vigour: 10, clarity: 8, spirit: 5, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Diamonds"], [2,2,"Rings"], [3,3,"Spiral"], [4,4,"Chevrons"], [5,5,"Bars"], [6,6,"Waves"]] }, { name: "Topper", formula: "d6", results: [[1,1,"Antlers"], [2,2,"Jaws"], [3,3,"Tree"], [4,4,"Fishtail"], [5,5,"Wings"], [6,6,"Seashell"]] }]
        },
        "The Pigeon Knight": {
            items: [{ type: "knight", flavor: "Lost Home", flavorLabel1: "Hue", flavorLabel2: "Shape" }, { type: "weapon", name: "Bitterglaive", damage: "d10", long: true }, { type: "coat", name: "Tattered Mail", armor: 1 }, { type: "misc", name: "Hooded Cloak" }],
            actors: [{ type: "steed", name: "Grey Steed", vigour: 7, clarity: 8, spirit: 5, guard: 2 }],
            tables: [{ name: "Hue", formula: "d6", results: [[1,1,"Emerald"], [2,2,"Marble"], [3,3,"Silver"], [4,4,"Golden"], [5,5,"Ruby"], [6,6,"Violet"]] }, { name: "Shape", formula: "d6", results: [[1,1,"Towers"], [2,2,"Walls"], [3,3,"Flowers"], [4,4,"Ships"], [5,5,"Water"], [6,6,"Clouds"]] }]
        },
        "The Shield Knight": {
            items: [{ type: "knight", flavor: "Soothing Salve", flavorLabel1: "Aroma", flavorLabel2: "Side Effect" }, { type: "weapon", name: "Dull Sword", damage: "2d6", hefty: true }, { type: "shield", name: "Cracked Shield", armor: 1, description: "d4 damage" }, { type: "coat", name: "Tattered Gambeson", armor: 1 }],
            actors: [{ type: "steed", name: "Untested Steed", vigour: 12, clarity: 8, spirit: 4, guard: 2 }],
            tables: [{ name: "Aroma", formula: "d6", results: [[1,1,"Rosemary"], [2,2,"Mould"], [3,3,"Pepper"], [4,4,"Copper"], [5,5,"Garlic"], [6,6,"Meat"]] }, { name: "Side Effect", formula: "d6", results: [[1,1,"Hallucination"], [2,2,"Lethargy"], [3,3,"Stimulation"], [4,4,"Sorrow"], [5,5,"Giddiness"], [6,6,"Absent-mindedness"]] }]
        },
        "The Whip Knight": {
            items: [{ type: "knight", flavor: "Strange Herbs", flavorLabel1: "Effect", flavorLabel2: "Side Effect" }, { type: "weapon", name: "Spiny Mace", damage: "d8", hefty: true }, { type: "weapon", name: "Whip", damage: "d6" }, { type: "misc", name: "Strange Herbs" }],
            actors: [{ type: "steed", name: "Pampered Steed", vigour: 10, clarity: 8, spirit: 5, guard: 2 }],
            tables: [{ name: "Effect", formula: "d6", results: [[1,1,"Hearing"], [2,2,"Fire breath"], [3,3,"Speak remote"], [4,4,"No pain"], [5,5,"Restore Virtue"], [6,6,"Restore All"]] }, { name: "Side Effect", formula: "d6", results: [[1,1,"Nausea"], [2,2,"Mute"], [3,3,"Hazy"], [4,4,"Lose VIG"], [5,5,"Lose CLA"], [6,6,"Lose SPI"]] }]
        },
        "The Seal Knight": {
            items: [{ type: "knight", flavor: "Scrolls", flavorLabel1: "Subject", flavorLabel2: "Prophecy" }, { type: "weapon", name: "Stout Halberd", damage: "d10", long: true }, { type: "coat", name: "Siege Plate", armor: 1 }, { type: "misc", name: "Runic Scrolls x3" }],
            actors: [{ type: "steed", name: "Dusty Steed", vigour: 10, clarity: 8, spirit: 5, guard: 4 }],
            tables: [{ name: "Subject", formula: "d6", results: [[1,1,"Seer"], [2,2,"Seal Knight"], [3,3,"Knight"], [4,4,"Seer"], [5,5,"Myth"], [6,6,"Realm"]] }, { name: "Prophecy", formula: "d6", results: [[1,1,"Death"], [2,2,"Torment"], [3,3,"Rebirth"], [4,4,"Treachery"], [5,5,"Growth"], [6,6,"Glory"]] }]
        },
        "The Horn Knight": {
            items: [{ type: "knight", flavor: "Wild Horn", flavorLabel1: "Shape", flavorLabel2: "Sound" }, { type: "weapon", name: "Antler-halberd", damage: "d8", long: true }, { type: "weapon", name: "Bow", damage: "d6", long: true }, { type: "misc", name: "Wild Horn" }],
            actors: [{ type: "steed", name: "Rusty Warhorse", vigour: 13, clarity: 6, spirit: 5, guard: 2, biography: "d6 Trample" }],
            tables: [{ name: "Shape", formula: "d6", results: [[1,1,"Sharp"], [2,2,"Helix"], [3,3,"Sickle"], [4,4,"Intertwined"], [5,5,"Coiling"], [6,6,"Swollen"]] }, { name: "Sound", formula: "d6", results: [[1,1,"Dissonant"], [2,2,"Solemn"], [3,3,"Ghostly"], [4,4,"Beastly"], [5,5,"Droning"], [6,6,"Gravelly"]] }]
        },
        "The Dove Knight": {
            items: [{ type: "knight", flavor: "Winged Armour", flavorLabel1: "Ability", flavorLabel2: "Limitation" }, { type: "weapon", name: "Stout Blade", damage: "2d6", hefty: true }, { type: "coat", name: "Winged Scale", armor: 1 }, { type: "misc", name: "Bright Weeds" }],
            actors: [{ type: "steed", name: "Mountain Steed", vigour: 14, clarity: 5, spirit: 5, guard: 2 }],
            tables: [{ name: "Ability", formula: "d6", results: [[1,1,"Safe land"], [2,2,"Jump high"], [3,3,"Sprint silent"], [4,4,"Animals calm"], [5,5,"Enemies sad"], [6,6,"Real wings"]] }, { name: "Limitation", formula: "d6", results: [[1,1,"Sink"], [2,2,"Red glow"], [3,3,"Slow run"], [4,4,"Horses fear"], [5,5,"Lose SPI"], [6,6,"Daylight only"]] }]
        },
        "The Story Knight": {
            items: [{ type: "knight", flavor: "Book of Stories", flavorLabel1: "Style", flavorLabel2: "Twist" }, { type: "weapon", name: "Crook-blade", damage: "d10", long: true }, { type: "coat", name: "Brigandine", armor: 1 }, { type: "misc", name: "Book of Tales" }],
            actors: [{ type: "steed", name: "Sinister Steed", vigour: 10, clarity: 14, spirit: 5, guard: 3 }],
            tables: [{ name: "Style", formula: "d6", results: [[1,1,"Quest"], [2,2,"Romance"], [3,3,"Revenge"], [4,4,"Farce"], [5,5,"Nonsense"], [6,6,"Tragedy"]] }, { name: "Twist", formula: "d6", results: [[1,1,"Ghosts"], [2,2,"Twins"], [3,3,"Amnesia"], [4,4,"Reincarnation"], [5,5,"Animals"], [6,6,"Death"]] }]
        },
        "The Turtle Knight": {
            items: [{ type: "knight", flavor: "Drinking Horn", flavorLabel1: "Appearance", flavorLabel2: "Flavour" }, { type: "weapon", name: "Beakhammer", damage: "d6" }, { type: "shield", name: "Tower Shield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Drinking Horn" }],
            actors: [{ type: "steed", name: "Squat Steed", vigour: 14, clarity: 5, spirit: 6, guard: 2 }],
            tables: [{ name: "Appearance", formula: "d6", results: [[1,1,"Tiny"], [2,2,"Runic"], [3,3,"Ruby"], [4,4,"Volcanic"], [5,5,"Battle"], [6,6,"Huge"]] }, { name: "Flavour", formula: "d6", results: [[1,1,"Honey"], [2,2,"Salt"], [3,3,"Almond"], [4,4,"Ice"], [5,5,"Berries"], [6,6,"Meat"]] }]
        },
        "The Key Knight": {
            items: [{ type: "knight", flavor: "Valuables", flavorLabel1: "Valuable", flavorLabel2: "Keepsake" }, { type: "weapon", name: "Horned Axe", damage: "d8", hefty: true }, { type: "shield", name: "Kite Shield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Ring of Keys" }],
            actors: [{ type: "steed", name: "Jittery Steed", vigour: 12, clarity: 10, spirit: 3, guard: 3 }],
            tables: [{ name: "Valuable", formula: "d6", results: [[1,1,"Gems"], [2,2,"Coins"], [3,3,"Salt"], [4,4,"Diamond"], [5,5,"Hairpin"], [6,6,"Pearls"]] }, { name: "Keepsake", formula: "d6", results: [[1,1,"Poem"], [2,2,"Hair"], [3,3,"Ring"], [4,4,"Teeth"], [5,5,"Blood"], [6,6,"Figurine"]] }]
        },
        "The Moat Knight": {
            items: [{ type: "knight", flavor: "Difficult Steed", flavorLabel1: "Will Not", flavorLabel2: "But" }, { type: "weapon", name: "Spiked Flail", damage: "d10", long: true }, { type: "coat", name: "Barbed Mail", armor: 1 }, { type: "misc", name: "Moat Shovel" }],
            actors: [{ type: "steed", name: "Difficult Steed", vigour: 12, clarity: 6, spirit: 6, guard: 2 }],
            tables: [{ name: "Will Not", formula: "d6", results: [[1,1,"Jump"], [2,2,"Stop"], [3,3,"Carry others"], [4,4,"Listen"], [5,5,"Pull"], [6,6,"Travel dark"]] }, { name: "But", formula: "d6", results: [[1,1,"Eats all"], [2,2,"Beautiful"], [3,3,"Hears ambush"], [4,4,"Knows north"], [5,5,"Hums"], [6,6,"Tough"]] }]
        },
        "The Boulder Knight": {
            items: [{ type: "knight", flavor: "Fancy Armour", flavorLabel1: "Design", flavorLabel2: "Quirk" }, { type: "weapon", name: "Siege Hammer", damage: "d10", long: true }, { type: "coat", name: "Fancy Plate", armor: 1 }, { type: "misc", name: "Fortress Book" }],
            actors: [{ type: "steed", name: "Well-fed Steed", vigour: 14, clarity: 8, spirit: 6, guard: 3 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Bronze"], [2,2,"Flanged"], [3,3,"Scales"], [4,4,"Brigandine"], [5,5,"Rings"], [6,6,"Brass"]] }, { name: "Quirk", formula: "d6", results: [[1,1,"Floats"], [2,2,"Quick don"], [3,3,"Silent"], [4,4,"Scary"], [5,5,"Spiked"], [6,6,"Ignore fall"]] }]
        },
        "The Tankard Knight": {
            items: [{ type: "knight", flavor: "Scar Story", flavorLabel1: "Who", flavorLabel2: "Betrayal" }, { type: "weapon", name: "Eagle Axe", damage: "d8", hefty: true }, { type: "shield", name: "Roundshield", armor: 1, description: "d4 damage" }, { type: "coat", name: "Mail Shirt", armor: 1 }],
            actors: [{ type: "steed", name: "Aggressive Charger", vigour: 14, clarity: 5, spirit: 6, guard: 2, biography: "d8 Trample" }],
            tables: [{ name: "Who", formula: "d6", results: [[1,1,"Ruler"], [2,2,"Seat"], [3,3,"Knight"], [4,4,"Village"], [5,5,"Captain"], [6,6,"Company"]] }, { name: "Betrayal", formula: "d6", results: [[1,1,"Disloyalty"], [2,2,"Theft"], [3,3,"Argument"], [4,4,"Promise"], [5,5,"Slander"], [6,6,"Neglect"]] }]
        },
        "The Owl Knight": {
            items: [{ type: "knight", flavor: "Tomes", flavorLabel1: "Title Start", flavorLabel2: "Title End" }, { type: "weapon", name: "Blade-staff", damage: "2d8", long: true }, { type: "coat", name: "Ringmail", armor: 1 }, { type: "misc", name: "Sack of Books" }],
            actors: [{ type: "steed", name: "Peaceful Steed", vigour: 10, clarity: 10, spirit: 6, guard: 4 }],
            tables: [{ name: "Title Start", formula: "d6", results: [[1,1,"Light of"], [2,2,"Those who"], [3,3,"Death &"], [4,4,"Merits of"], [5,5,"Domain &"], [6,6,"Garden of"]] }, { name: "Title End", formula: "d6", results: [[1,1,"Sea Beasts"], [2,2,"Bread"], [3,3,"The City"], [4,4,"Meditations"], [5,5,"Coin"], [6,6,"Doom"]] }]
        },
        "The Hooded Knight": {
            items: [{ type: "knight", flavor: "Hood & Cloak", flavorLabel1: "Hood", flavorLabel2: "Cloak" }, { type: "weapon", name: "Glaive", damage: "d10", long: true }, { type: "weapon", name: "Throwing Axe x3", damage: "d6" }, { type: "misc", name: "Cloak & Hood" }],
            actors: [{ type: "steed", name: "Modest Steed", vigour: 10, clarity: 9, spirit: 5, guard: 4 }],
            tables: [{ name: "Hood", formula: "d6", results: [[1,1,"Veiled"], [2,2,"Shadowy"], [3,3,"Silken"], [4,4,"Tattered"], [5,5,"Fur-trimmed"], [6,6,"Threadbare"]] }, { name: "Cloak", formula: "d6", results: [[1,1,"Velvet"], [2,2,"Torn"], [3,3,"Weathered"], [4,4,"Layered"], [5,5,"Embroidered"], [6,6,"Faded"]] }]
        },
        "The Lance Knight": {
            items: [{ type: "knight", flavor: "Mystic Sight", flavorLabel1: "Can See", flavorLabel2: "Cannot See" }, { type: "weapon", name: "Lance", damage: "d10", long: true }, { type: "weapon", name: "Spiked Mace", damage: "d8", hefty: true }, { type: "shield", name: "Kite Shield", armor: 1, description: "d4 damage" }],
            actors: [{ type: "steed", name: "Weary Charger", vigour: 14, clarity: 6, spirit: 4, guard: 3, biography: "d6 Trample" }],
            tables: [{ name: "Can See", formula: "d6", results: [[1,1,"Fears"], [2,2,"Desires"], [3,3,"Hidden"], [4,4,"Regrets"], [5,5,"Loyalties"], [6,6,"Injuries"]] }, { name: "Cannot See", formula: "d6", results: [[1,1,"Colour"], [2,2,"Writing"], [3,3,"Birds"], [4,4,"Water"], [5,5,"Stars"], [6,6,"Gold"]] }]
        },
        "The Questing Knight": {
            items: [{ type: "knight", flavor: "Ancient Sword", flavorLabel1: "Appearance", flavorLabel2: "Source" }, { type: "weapon", name: "Ancient Sword", damage: "varies" }, { type: "shield", name: "Kite Shield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Cold Stone" }],
            actors: [{ type: "steed", name: "Reckless Charger", vigour: 14, clarity: 6, spirit: 6, guard: 1, biography: "d8 Trample" }],
            tables: [{ name: "Appearance", formula: "d6", results: [[1,1,"Massive"], [2,2,"Curved"], [3,3,"Jagged"], [4,4,"Hooked"], [5,5,"Shining"], [6,6,"Cruel"]] }, { name: "Source", formula: "d6", results: [[1,1,"Tide"], [2,2,"Tomb"], [3,3,"Tree"], [4,4,"Eagle"], [5,5,"Hermit"], [6,6,"Mountain"]] }]
        },
        "The Ring Knight": {
            items: [{ type: "knight", flavor: "Rings", flavorLabel1: "Design", flavorLabel2: "Effect" }, { type: "weapon", name: "Long Mace", damage: "d10", long: true }, { type: "coat", name: "Violet Mail", armor: 1 }, { type: "misc", name: "Pair of Rings" }],
            actors: [{ type: "steed", name: "Aloof Steed", vigour: 11, clarity: 8, spirit: 7, guard: 3, biography: "No trail" }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Snakes"], [2,2,"Skulls"], [3,3,"Thorns"], [4,4,"Rubies"], [5,5,"Gold"], [6,6,"Birds"]] }, { name: "Effect", formula: "d6", results: [[1,1,"Vision"], [2,2,"Hearing"], [3,3,"GD"], [4,4,"VIG"], [5,5,"CLA"], [6,6,"SPI"]] }]
        },
        "The Forge Knight": {
            items: [{ type: "knight", flavor: "Scars", flavorLabel1: "Visible", flavorLabel2: "Non-Visible" }, { type: "weapon", name: "Bolt-Guisarme", damage: "d10", long: true }, { type: "coat", name: "Iron Chestplate", armor: 1 }, { type: "misc", name: "Forge Dust" }],
            actors: [{ type: "steed", name: "Helmed Steed", vigour: 14, clarity: 4, spirit: 5, guard: 4, biography: "d6 Trample" }],
            tables: [{ name: "Visible", formula: "d6", results: [[1,1,"Burnt hands"], [2,2,"Scorched hair"], [3,3,"Faded eyes"], [4,4,"Missing teeth"], [5,5,"Blisters"], [6,6,"Brand"]] }, { name: "Non-Visible", formula: "d6", results: [[1,1,"Nightmares"], [2,2,"Noise sense"], [3,3,"Sky distrust"], [4,4,"Pain threshold"], [5,5,"Light sense"], [6,6,"Water fear"]] }]
        },
        "The Rune Knight": {
            items: [{ type: "knight", flavor: "Flask", flavorLabel1: "Shaken", flavorLabel2: "Smashed" }, { type: "weapon", name: "Stone Pillar", damage: "2d10", slow: true }, { type: "coat", name: "Iron Chestplate", armor: 1 }, { type: "misc", name: "Crystal Flask" }],
            actors: [{ type: "steed", name: "Muscular Charger", vigour: 13, clarity: 8, spirit: 5, guard: 3, biography: "d8 Trample" }],
            tables: [{ name: "Shaken", formula: "d6", results: [[1,1,"Warmth"], [2,2,"Darkness"], [3,3,"Light"], [4,4,"Repel birds"], [5,5,"Soothe dogs"], [6,6,"Ease pain"]] }, { name: "Smashed", formula: "d6", results: [[1,1,"Thunder"], [2,2,"Summer"], [3,3,"Night"], [4,4,"Scream"], [5,5,"Locusts"], [6,6,"Freeze water"]] }]
        },
        "The Gallows Knight": {
            items: [{ type: "knight", flavor: "Salvaged Armour", flavorLabel1: "Type", flavorLabel2: "Detail" }, { type: "weapon", name: "Neck-catcher", damage: "d10", long: true }, { type: "coat", name: "Salvaged Armour", armor: 1 }, { type: "misc", name: "Titan Beads" }],
            actors: [{ type: "steed", name: "Flea-bitten Steed", vigour: 9, clarity: 7, spirit: 4, guard: 3 }],
            tables: [{ name: "Type", formula: "d6", results: [[1,1,"Copper mail"], [2,2,"Cracked plate"], [3,3,"Brigandine"], [4,4,"Padded"], [5,5,"Leather"], [6,6,"Dented"]] }, { name: "Detail", formula: "d6", results: [[1,1,"Arrowhead"], [2,2,"Patched"], [3,3,"Burnt"], [4,4,"Claw marks"], [5,5,"Faded"], [6,6,"Blood"]] }]
        },
        "The Tome Knight": {
            items: [{ type: "knight", flavor: "Recall", flavorLabel1: "Blind Spot", flavorLabel2: "Condition" }, { type: "weapon", name: "Heavy Staff", damage: "d10", long: true }, { type: "coat", name: "Brigandine", armor: 1 }, { type: "misc", name: "Perfect Recall" }],
            actors: [{ type: "steed", name: "Small Steed", vigour: 9, clarity: 8, spirit: 5, guard: 2 }],
            tables: [{ name: "Blind Spot", formula: "d6", results: [[1,1,"Names"], [2,2,"Places"], [3,3,"Faces"], [4,4,"Geography"], [5,5,"Relationships"], [6,6,"Time"]] }, { name: "Condition", formula: "d6", results: [[1,1,"Crowds"], [2,2,"Combat"], [3,3,"Morning"], [4,4,"Night"], [5,5,"Alone"], [6,6,"Drinking"]] }]
        },
        "The Meteor Knight": {
            items: [{ type: "knight", flavor: "Trident", flavorLabel1: "Appearance", flavorLabel2: "Ability" }, { type: "weapon", name: "Elaborate Trident", damage: "d10", long: true }, { type: "coat", name: "Brass Mail", armor: 1 }, { type: "misc", name: "Moon Oil" }],
            actors: [{ type: "steed", name: "Limping Steed", vigour: 12, clarity: 8, spirit: 5, guard: 4 }],
            tables: [{ name: "Appearance", formula: "d6", results: [[1,1,"Rings"], [2,2,"Blackened"], [3,3,"Two-headed"], [4,4,"Glow"], [5,5,"Five prongs"], [6,6,"Telescopic"]] }, { name: "Ability", formula: "d6", results: [[1,1,"Thrown"], [2,2,"Recall"], [3,3,"Aquatic"], [4,4,"Anti-air"], [5,5,"Find water"], [6,6,"Unbreakable"]] }]
        },
        "The Gazer Knight": {
            items: [{ type: "knight", flavor: "Tapestry", flavorLabel1: "Event", flavorLabel2: "Subject" }, { type: "weapon", name: "Toothed Blade", damage: "d8", hefty: true }, { type: "coat", name: "Mail", armor: 1 }, { type: "misc", name: "Flickerlamp" }],
            actors: [{ type: "steed", name: "Blueish Steed", vigour: 12, clarity: 10, spirit: 5, guard: 3 }],
            tables: [{ name: "Event", formula: "d6", results: [[1,1,"Birth"], [2,2,"Deeds"], [3,3,"Ambitions"], [4,4,"Shame"], [5,5,"Glory"], [6,6,"Peace"]] }, { name: "Subject", formula: "d6", results: [[1,1,"Seer"], [2,2,"Knight"], [3,3,"Self"], [4,4,"Company"], [5,5,"Ruler"], [6,6,"Unknown"]] }]
        },
        "The Mule Knight": {
            items: [{ type: "knight", flavor: "Explosives", flavorLabel1: "Form", flavorLabel2: "Trigger" }, { type: "weapon", name: "Weighted Staff", damage: "d10", long: true }, { type: "coat", name: "Polished Chain", armor: 1 }, { type: "misc", name: "Explosives x3" }],
            actors: [{ type: "steed", name: "Tall Steed", vigour: 14, clarity: 7, spirit: 6, guard: 2 }],
            tables: [{ name: "Form", formula: "d6", results: [[1,1,"Pinecone"], [2,2,"Dust"], [3,3,"Oil"], [4,4,"Chestnut"], [5,5,"Gizzard"], [6,6,"Egg"]] }, { name: "Trigger", formula: "d6", results: [[1,1,"Water"], [2,2,"Fire"], [3,3,"Word"], [4,4,"Touch"], [5,5,"Light"], [6,6,"Ground"]] }]
        },
        "The Halo Knight": {
            items: [{ type: "knight", flavor: "Mistvial", flavorLabel1: "Material", flavorLabel2: "Requirement" }, { type: "weapon", name: "Crescent Axe", damage: "d8", hefty: true }, { type: "shield", name: "Kite Shield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Mistvial" }],
            actors: [{ type: "steed", name: "Wild Steed", vigour: 15, clarity: 5, spirit: 7, guard: 3 }],
            tables: [{ name: "Material", formula: "d6", results: [[1,1,"Blood"], [2,2,"Sand"], [3,3,"Smoke"], [4,4,"Milk"], [5,5,"Salt"], [6,6,"Silk"]] }, { name: "Requirement", formula: "d6", results: [[1,1,"Ritual"], [2,2,"Blessing"], [3,3,"Wounded"], [4,4,"Coin"], [5,5,"Sunrise"], [6,6,"Nest"]] }]
        },
        "The Iron Knight": {
            items: [{ type: "knight", flavor: "Blade Origin", flavorLabel1: "Source", flavorLabel2: "Time" }, { type: "weapon", name: "Cleavingblade", damage: "2d8", long: true }, { type: "coat", name: "Mail & Plate", armor: 1 }, { type: "misc", name: "Inscribed Scabbard" }],
            actors: [{ type: "steed", name: "Dark Steed", vigour: 11, clarity: 7, spirit: 6, guard: 3 }],
            tables: [{ name: "Source", formula: "d6", results: [[1,1,"Forest"], [2,2,"Waterfall"], [3,3,"Sea"], [4,4,"Boulder"], [5,5,"Cave"], [6,6,"Tree"]] }, { name: "Time", formula: "d6", results: [[1,1,"Contentment"], [2,2,"Desperation"], [3,3,"Victory"], [4,4,"Anger"], [5,5,"Sorrow"], [6,6,"Transition"]] }]
        },
        "The Mirror Knight": {
            items: [{ type: "knight", flavor: "Memories", flavorLabel1: "Knight", flavorLabel2: "Steed" }, { type: "weapon", name: "Hook-axe", damage: "d8", hefty: true }, { type: "weapon", name: "Throwing Axe x3", damage: "d6" }, { type: "shield", name: "Roundshield", armor: 1, description: "d4 damage" }],
            actors: [{ type: "steed", name: "Faded Steed", vigour: 9, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Knight", formula: "d6", results: [[1,1,"Treasure"], [2,2,"Revenge"], [3,3,"Tournament"], [4,4,"Escape"], [5,5,"Siege"], [6,6,"Rescue"]] }, { name: "Steed", formula: "d6", results: [[1,1,"Brave"], [2,2,"Galloped"], [3,3,"Ambush"], [4,4,"Death"], [5,5,"Lost eye"], [6,6,"Arrows"]] }]
        },
        "The Dusk Knight": {
            items: [{ type: "knight", flavor: "Poem", flavorLabel1: "Start", flavorLabel2: "End" }, { type: "weapon", name: "Longhammer", damage: "d10", long: true }, { type: "weapon", name: "Javelin x3", damage: "d6" }, { type: "misc", name: "Wolfnuts" }],
            actors: [{ type: "steed", name: "Auburn Steed", vigour: 12, clarity: 8, spirit: 6, guard: 2 }],
            tables: [{ name: "Start", formula: "d6", results: [[1,1,"Twins lost"], [2,2,"Rivals"], [3,3,"Ugly sons"], [4,4,"Hermit"], [5,5,"Chicken"], [6,6,"Poet"]] }, { name: "End", formula: "d6", results: [[1,1,"Eaten"], [2,2,"Plague"], [3,3,"City"], [4,4,"Nonsense"], [5,5,"Cliffhanger"], [6,6,"Happy"]] }]
        },
        "The Coin Knight": {
            items: [{ type: "knight", flavor: "Flute", flavorLabel1: "Loved By", flavorLabel2: "Hated By" }, { type: "weapon", name: "Morningstar", damage: "d8", hefty: true }, { type: "shield", name: "Roundshield", armor: 1, description: "d4 damage" }, { type: "coat", name: "Brigandine", armor: 1 }],
            actors: [{ type: "steed", name: "Arctic Steed", vigour: 14, clarity: 8, spirit: 7, guard: 3 }],
            tables: [{ name: "Loved By", formula: "d6", results: [[1,1,"Children"], [2,2,"Cats"], [3,3,"Nobles"], [4,4,"Knights"], [5,5,"Predators"], [6,6,"Sea creatures"]] }, { name: "Hated By", formula: "d6", results: [[1,1,"All"], [2,2,"Musicians"], [3,3,"Rodents"], [4,4,"Company"], [5,5,"Seers"], [6,6,"Songbirds"]] }]
        },
        "The Mock Knight": {
            items: [{ type: "knight", flavor: "Body", flavorLabel1: "Bones", flavorLabel2: "Skin" }, { type: "weapon", name: "War Flail", damage: "d10", long: true }, { type: "coat", name: "Plate Suit", armor: 1 }],
            actors: [{ type: "steed", name: "Well-groomed Steed", vigour: 12, clarity: 8, spirit: 6, guard: 2 }],
            tables: [{ name: "Bones", formula: "d6", results: [[1,1,"Ivory"], [2,2,"Bronze"], [3,3,"Sapling"], [4,4,"String"], [5,5,"Wood"], [6,6,"Chain"]] }, { name: "Skin", formula: "d6", results: [[1,1,"Leather"], [2,2,"Felt"], [3,3,"Silk"], [4,4,"Wool"], [5,5,"Parchment"], [6,6,"Clay"]] }]
        },
        "The Mask Knight": {
            items: [{ type: "knight", flavor: "Armour", flavorLabel1: "Appearance", flavorLabel2: "Design" }, { type: "weapon", name: "Splittingaxe", damage: "d10", long: true }, { type: "coat", name: "Mail", armor: 1 }, { type: "misc", name: "Star Ink" }],
            actors: [{ type: "steed", name: "Silver Steed", vigour: 12, clarity: 8, spirit: 5, guard: 4 }],
            tables: [{ name: "Appearance", formula: "d6", results: [[1,1,"Youthful"], [2,2,"Beautiful"], [3,3,"Misshapen"], [4,4,"Abstract"], [5,5,"Skull"], [6,6,"Elder"]] }, { name: "Design", formula: "d6", results: [[1,1,"Horned"], [2,2,"Two-faced"], [3,3,"Blindfolded"], [4,4,"Scarred"], [5,5,"Roaring"], [6,6,"Crowned"]] }]
        },
        "The Bone Knight": {
            items: [{ type: "knight", flavor: "Bones", flavorLabel1: "Box", flavorLabel2: "Content" }, { type: "weapon", name: "Needledagger", damage: "d6" }, { type: "shield", name: "Jagged Buckler", armor: 1, description: "d4 damage" }, { type: "misc", name: "Box of Bones" }],
            actors: [{ type: "steed", name: "Marsh Steed", vigour: 12, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Box", formula: "d6", results: [[1,1,"Silver"], [2,2,"Ivory"], [3,3,"Bronze"], [4,4,"Velvet"], [5,5,"Wood"], [6,6,"Shell"]] }, { name: "Content", formula: "d6", results: [[1,1,"Age"], [2,2,"Size"], [3,3,"Habitat"], [4,4,"Beauty"], [5,5,"Virtue"], [6,6,"Chaos"]] }]
        },
        "The Salt Knight": {
            items: [{ type: "knight", flavor: "Everflask", flavorLabel1: "Design", flavorLabel2: "Thirst" }, { type: "weapon", name: "Spined Mace", damage: "d8", hefty: true }, { type: "weapon", name: "Javelin", damage: "d6" }, { type: "coat", name: "Coraline Mail", armor: 1 }],
            actors: [{ type: "steed", name: "Scaled Steed", vigour: 12, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Leather"], [2,2,"Brass"], [3,3,"Silver"], [4,4,"Stone"], [5,5,"Wood"], [6,6,"Glass"]] }, { name: "Thirst", formula: "d6", results: [[1,1,"Story"], [2,2,"Blade"], [3,3,"Creature"], [4,4,"Fruit"], [5,5,"Honey"], [6,6,"Music"]] }]
        },
        "The Violet Knight": {
            items: [{ type: "knight", flavor: "Steed", flavorLabel1: "Why?", flavorLabel2: "Trait" }, { type: "weapon", name: "Grand Mace", damage: "d10", long: true }, { type: "coat", name: "Glossy Mail", armor: 1 }, { type: "misc", name: "Mirror" }],
            actors: [{ type: "steed", name: "Nameless Steed", vigour: 12, clarity: 8, spirit: 4, guard: 1 }],
            tables: [{ name: "Why?", formula: "d6", results: [[1,1,"Seer"], [2,2,"Fright"], [3,3,"Forgotten"], [4,4,"Unspeakable"], [5,5,"Death"], [6,6,"Power"]] }, { name: "Trait", formula: "d6", results: [[1,1,"Silent"], [2,2,"Water fear"], [3,3,"Night"], [4,4,"Arrow immune"], [5,5,"Sea walk"], [6,6,"Fealty"]] }]
        },
        "The Cosmic Knight": {
            items: [{ type: "knight", flavor: "Crossbow", flavorLabel1: "Form", flavorLabel2: "Twist" }, { type: "weapon", name: "Strange Crossbow", damage: "varies" }, { type: "misc", name: "Echostone" }, { type: "coat", name: "None", armor: 0 }],
            actors: [{ type: "steed", name: "Boneless Steed", vigour: 10, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Form", formula: "d6", results: [[1,1,"Handheld"], [2,2,"Lightwood"], [3,3,"Repeating"], [4,4,"Double"], [5,5,"Bronze"], [6,6,"Ironwood"]] }, { name: "Twist", formula: "d6", results: [[1,1,"No dark"], [2,2,"Owner only"], [3,3,"Loud"], [4,4,"No bolts"], [5,5,"Painful"], [6,6,"Melee"]] }]
        },
        "The Temple Knight": {
            items: [{ type: "knight", flavor: "Snake", flavorLabel1: "Voice", flavorLabel2: "Agenda" }, { type: "weapon", name: "Spear", damage: "d8", hefty: true }, { type: "shield", name: "Broadshield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Mummified Snake" }],
            actors: [{ type: "steed", name: "Moorland Steed", vigour: 11, clarity: 9, spirit: 6, guard: 3 }],
            tables: [{ name: "Voice", formula: "d6", results: [[1,1,"Pitiful"], [2,2,"Mocking"], [3,3,"Sinister"], [4,4,"Benevolent"], [5,5,"Ancient"], [6,6,"Loving"]] }, { name: "Agenda", formula: "d6", results: [[1,1,"Death"], [2,2,"Order"], [3,3,"Bloodshed"], [4,4,"Peace"], [5,5,"Chaos"], [6,6,"Ambition"]] }]
        },
        "The Fox Knight": {
            items: [{ type: "knight", flavor: "Hidden Blade", flavorLabel1: "Design", flavorLabel2: "Ability" }, { type: "weapon", name: "Jagged Blade", damage: "d8", hefty: true }, { type: "shield", name: "Buckler", armor: 1, description: "d4 damage" }, { type: "weapon", name: "Hidden Blade", damage: "d6" }],
            actors: [{ type: "steed", name: "Tunnel Steed", vigour: 10, clarity: 10, spirit: 5, guard: 2 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Ebony"], [2,2,"Feather"], [3,3,"Tapered"], [4,4,"Fang"], [5,5,"Wavy"], [6,6,"Bone"]] }, { name: "Ability", formula: "d6", results: [[1,1,"Shadow"], [2,2,"Thrown"], [3,3,"Betrayal"], [4,4,"Twig"], [5,5,"Split"], [6,6,"Harmless"]] }]
        },
        "The Gull Knight": {
            items: [{ type: "knight", flavor: "Patchwork Armour", flavorLabel1: "Source", flavorLabel2: "Mix" }, { type: "weapon", name: "Hooked Blade", damage: "d8", hefty: true }, { type: "coat", name: "Patchwork Mail", armor: 1 }, { type: "misc", name: "Blinding Bracelet" }],
            actors: [{ type: "steed", name: "Tempestuous Steed", vigour: 12, clarity: 8, spirit: 7, guard: 4 }],
            tables: [{ name: "Source", formula: "d6", results: [[1,1,"Soldiers"], [2,2,"Tomb"], [3,3,"Shipwreck"], [4,4,"Pit"], [5,5,"Knight"], [6,6,"Militia"]] }, { name: "Mix", formula: "d6", results: [[1,1,"Leather"], [2,2,"Bronze"], [3,3,"Steel"], [4,4,"Brass"], [5,5,"Coat"], [6,6,"Furs"]] }]
        },
        "The Magpie Knight": {
            items: [{ type: "knight", flavor: "Memento", flavorLabel1: "Item", flavorLabel2: "Memory" }, { type: "weapon", name: "Heavy Cudgel", damage: "d8", hefty: true }, { type: "weapon", name: "Javelin x3", damage: "d6" }, { type: "misc", name: "Twofold Pouch" }],
            actors: [{ type: "steed", name: "Ironclad Steed", vigour: 13, clarity: 5, spirit: 5, guard: 2, biography: "d6 Trample" }],
            tables: [{ name: "Item", formula: "d6", results: [[1,1,"Flower"], [2,2,"Hilt"], [3,3,"Pearl"], [4,4,"Banner"], [5,5,"Coin"], [6,6,"Collar"]] }, { name: "Memory", formula: "d6", results: [[1,1,"Victory"], [2,2,"Defeat"], [3,3,"Happy"], [4,4,"Sorrow"], [5,5,"Love"], [6,6,"Hate"]] }]
        },
        "The Reliquary Knight": {
            items: [{ type: "knight", flavor: "Relic", flavorLabel1: "Part", flavorLabel2: "Being" }, { type: "weapon", name: "War Sickle", damage: "d8", hefty: true }, { type: "coat", name: "Carved Plate", armor: 1 }, { type: "misc", name: "Reliquary" }],
            actors: [{ type: "steed", name: "Bearded Steed", vigour: 12, clarity: 8, spirit: 6, guard: 3 }],
            tables: [{ name: "Part", formula: "d6", results: [[1,1,"Hand"], [2,2,"Skull"], [3,3,"Heart"], [4,4,"Ribs"], [5,5,"Eye"], [6,6,"Organ"]] }, { name: "Being", formula: "d6", results: [[1,1,"Seer"], [2,2,"Knight"], [3,3,"Monarch"], [4,4,"Monster"], [5,5,"Bird"], [6,6,"Reptile"]] }]
        },
        "The Vulture Knight": {
            items: [{ type: "knight", flavor: "Armour", flavorLabel1: "Material", flavorLabel2: "Detail" }, { type: "weapon", name: "Black Axe", damage: "d10", long: true }, { type: "coat", name: "Sinister Mail", armor: 1 }, { type: "misc", name: "Spidernip" }],
            actors: [{ type: "steed", name: "Bright-eyed Steed", vigour: 12, clarity: 9, spirit: 5, guard: 2 }],
            tables: [{ name: "Material", formula: "d6", results: [[1,1,"Burned"], [2,2,"Bronze"], [3,3,"Bloody"], [4,4,"Iron"], [5,5,"Leather"], [6,6,"Scales"]] }, { name: "Detail", formula: "d6", results: [[1,1,"Bat wing"], [2,2,"Embroidery"], [3,3,"Shadow"], [4,4,"Tattered"], [5,5,"Bones"], [6,6,"Skulls"]] }]
        },
        "The Free Knight": {
            items: [{ type: "knight", flavor: "Shield", flavorLabel1: "Weakness", flavorLabel2: "Ability" }, { type: "weapon", name: "Hooked Flail", damage: "d8", hefty: true }, { type: "shield", name: "Hexshield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Tempest Chest" }],
            actors: [{ type: "steed", name: "Grassy Steed", vigour: 11, clarity: 8, spirit: 5, guard: 2 }],
            tables: [{ name: "Weakness", formula: "d6", results: [[1,1,"Axes"], [2,2,"Arrows"], [3,3,"Birds"], [4,4,"Spears"], [5,5,"Swords"], [6,6,"Blunt"]] }, { name: "Ability", formula: "d6", results: [[1,1,"Thrown"], [2,2,"Fall safe"], [3,3,"Seer pain"], [4,4,"Floats"], [5,5,"Sound block"], [6,6,"Bladed"]] }]
        },
        "The Silk Knight": {
            items: [{ type: "knight", flavor: "Steed Fear", flavorLabel1: "Distracted", flavorLabel2: "Scared" }, { type: "weapon", name: "Delicate Halberd", damage: "d10", long: true }, { type: "coat", name: "Woven Coat", armor: 1 }, { type: "misc", name: "Brass Puzzle" }],
            actors: [{ type: "steed", name: "Young Steed", vigour: 9, clarity: 8, spirit: 6, guard: 1 }],
            tables: [{ name: "Distracted", formula: "d6", results: [[1,1,"Animals"], [2,2,"Moss"], [3,3,"Water"], [4,4,"Salt"], [5,5,"Fruit"], [6,6,"Shiny"]] }, { name: "Scared", formula: "d6", results: [[1,1,"Steeds"], [2,2,"Fire"], [3,3,"Dark"], [4,4,"Children"], [5,5,"Music"], [6,6,"Alone"]] }]
        },
        "The Tiger Knight": {
            items: [{ type: "knight", flavor: "Tattoo", flavorLabel1: "Design", flavorLabel2: "Why" }, { type: "weapon", name: "Fang Blade x2", damage: "d6" }, { type: "coat", name: "Knotted Coat", armor: 1 }, { type: "misc", name: "Phoenix Feather" }],
            actors: [{ type: "steed", name: "Tattooed Steed", vigour: 12, clarity: 9, spirit: 5, guard: 5 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Abstract"], [2,2,"Runes"], [3,3,"Letters"], [4,4,"Skulls"], [5,5,"Thunder"], [6,6,"Thorns"]] }, { name: "Why", formula: "d6", results: [[1,1,"Service"], [2,2,"Bought"], [3,3,"Born"], [4,4,"Overnight"], [5,5,"Slowly"], [6,6,"Seer"]] }]
        },
        "The Leaf Knight": {
            items: [{ type: "knight", flavor: "Stick", flavorLabel1: "Use", flavorLabel2: "But" }, { type: "weapon", name: "Hooked Club", damage: "d8", hefty: true }, { type: "coat", name: "Verdant Leather", armor: 1 }, { type: "misc", name: "Murmur Box" }],
            actors: [{ type: "steed", name: "Patchy Steed", vigour: 12, clarity: 5, spirit: 5, guard: 3 }],
            tables: [{ name: "Use", formula: "d6", results: [[1,1,"Cools liquid"], [2,2,"Repels insects"], [3,3,"Rope"], [4,4,"Terrifies"], [5,5,"Sticky"], [6,6,"Blessing"]] }, { name: "But", formula: "d6", results: [[1,1,"Long"], [2,2,"Dogs want"], [3,3,"Plain"], [4,4,"Delicate"], [5,5,"Flammable"], [6,6,"Sunlight only"]] }]
        },
        "The Glass Knight": {
            items: [{ type: "knight", flavor: "Armour", flavorLabel1: "Hue", flavorLabel2: "Decoration" }, { type: "weapon", name: "Pike", damage: "d10", long: true }, { type: "coat", name: "Painted Mail", armor: 1 }, { type: "misc", name: "Witching Needle" }],
            actors: [{ type: "steed", name: "Chestnut Steed", vigour: 11, clarity: 8, spirit: 6, guard: 3 }],
            tables: [{ name: "Hue", formula: "d6", results: [[1,1,"Indigo"], [2,2,"Crimson"], [3,3,"Green"], [4,4,"Teal"], [5,5,"Gold"], [6,6,"Rose"]] }, { name: "Decoration", formula: "d6", results: [[1,1,"Faces"], [2,2,"Vines"], [3,3,"Stars"], [4,4,"Wolves"], [5,5,"Fire"], [6,6,"City"]] }]
        },
        "The Hive Knight": {
            items: [{ type: "knight", flavor: "Cocoon", flavorLabel1: "Condition", flavorLabel2: "Requirement" }, { type: "weapon", name: "Rootbow", damage: "d6", long: true }, { type: "weapon", name: "Daggers", damage: "d6" }, { type: "misc", name: "Tidal Resin" }],
            actors: [{ type: "steed", name: "Hooded Steed", vigour: 11, clarity: 10, spirit: 5, guard: 3 }],
            tables: [{ name: "Condition", formula: "d6", results: [[1,1,"Fed"], [2,2,"Clean"], [3,3,"Sung"], [4,4,"Alight"], [5,5,"Buried"], [6,6,"Beheaded"]] }, { name: "Requirement", formula: "d6", results: [[1,1,"Darkness"], [2,2,"Submersion"], [3,3,"Milk"], [4,4,"Smoke"], [5,5,"Leaves"], [6,6,"Embers"]] }]
        },
        "The Ghoul Knight": {
            items: [{ type: "knight", flavor: "Toy", flavorLabel1: "Animal", flavorLabel2: "Origin" }, { type: "weapon", name: "Bearded Axe", damage: "d10", long: true }, { type: "coat", name: "Dusty Mail", armor: 1 }, { type: "misc", name: "Cleaner Salt" }],
            actors: [{ type: "steed", name: "Faithful Steed", vigour: 12, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Animal", formula: "d6", results: [[1,1,"Turtle"], [2,2,"Elephant"], [3,3,"Lion"], [4,4,"Seahorse"], [5,5,"Unicorn"], [6,6,"Pigeon"]] }, { name: "Origin", formula: "d6", results: [[1,1,"Friend"], [2,2,"Stolen"], [3,3,"Made"], [4,4,"Parent"], [5,5,"Ruin"], [6,6,"River"]] }]
        },
        "The Weaver Knight": {
            items: [{ type: "knight", flavor: "Weapon", flavorLabel1: "Design", flavorLabel2: "Ability" }, { type: "weapon", name: "Two-headed Axe", damage: "d8", hefty: true }, { type: "shield", name: "Buckler", armor: 1, description: "d4 damage" }, { type: "weapon", name: "Thrown Weapon", damage: "d6" }],
            actors: [{ type: "steed", name: "Orchard Steed", vigour: 12, clarity: 9, spirit: 5, guard: 1 }],
            tables: [{ name: "Design", formula: "d6", results: [[1,1,"Club"], [2,2,"Disc"], [3,3,"Spike"], [4,4,"Bola"], [5,5,"Fork"], [6,6,"Ball"]] }, { name: "Ability", formula: "d6", results: [[1,1,"Duel"], [2,2,"Steeds"], [3,3,"Fleeing"], [4,4,"Mounted"], [5,5,"Flying"], [6,6,"No Shield"]] }]
        },
        "The Thunder Knight": {
            items: [{ type: "knight", flavor: "Bug", flavorLabel1: "Ability", flavorLabel2: "Manner" }, { type: "weapon", name: "Forked Spear", damage: "d8", hefty: true }, { type: "shield", name: "Oakshield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Caged Bug" }],
            actors: [{ type: "steed", name: "Overfed Steed", vigour: 12, clarity: 6, spirit: 5, guard: 2, biography: "d6 Trample" }],
            tables: [{ name: "Ability", formula: "d6", results: [[1,1,"Bite"], [2,2,"Eat metal"], [3,3,"Chirp"], [4,4,"Fetch"], [5,5,"Food"], [6,6,"Painful"]] }, { name: "Manner", formula: "d6", results: [[1,1,"Wild"], [2,2,"Trained"], [3,3,"Stupid"], [4,4,"Eager"], [5,5,"Hateful"], [6,6,"Noble"]] }]
        },
        "The Dust Knight": {
            items: [{ type: "knight", flavor: "Fish", flavorLabel1: "Flavour", flavorLabel2: "Side Effect" }, { type: "weapon", name: "Old Hammer", damage: "d8", hefty: false }, { type: "shield", name: "Inscribed Shield", armor: 1, description: "d4 damage" }, { type: "misc", name: "Beckoning Net" }],
            actors: [{ type: "steed", name: "Spotted Steed", vigour: 12, clarity: 9, spirit: 5, guard: 3 }],
            tables: [{ name: "Flavour", formula: "d6", results: [[1,1,"Salty"], [2,2,"Picante"], [3,3,"Sour"], [4,4,"Challenging"], [5,5,"Soapy"], [6,6,"Smoky"]] }, { name: "Side Effect", formula: "d6", results: [[1,1,"Numb"], [2,2,"Filling"], [3,3,"Addictive"], [4,4,"Vomit"], [5,5,"Blind"], [6,6,"Weep"]] }]
        },
        "The Fanged Knight": {
            items: [{ type: "knight", flavor: "Ancestor", flavorLabel1: "Place", flavorLabel2: "Relation" }, { type: "weapon", name: "Forked Blade", damage: "d8", hefty: true }, { type: "coat", name: "Shell Chain", armor: 1 }, { type: "misc", name: "Ancient Scroll" }],
            actors: [{ type: "steed", name: "Noble Steed", vigour: 12, clarity: 5, spirit: 7, guard: 4 }],
            tables: [{ name: "Place", formula: "d6", results: [[1,1,"Tower"], [2,2,"Water"], [3,3,"Peak"], [4,4,"Village"], [5,5,"River"], [6,6,"Cave"]] }, { name: "Relation", formula: "d6", results: [[1,1,"Ruler"], [2,2,"Knight"], [3,3,"Seer"], [4,4,"People"], [5,5,"You"], [6,6,"Company"]] }]
        },
        "The Pearl Knight": {
            items: [{ type: "knight", flavor: "Blade", flavorLabel1: "Knowledge", flavorLabel2: "Punishment" }, { type: "weapon", name: "Seablade", damage: "2d8", long: true }, { type: "coat", name: "Glossy Mail", armor: 1 }, { type: "misc", name: "Salincense" }],
            actors: [{ type: "steed", name: "Rose Steed", vigour: 12, clarity: 9, spirit: 5, guard: 3 }],
            tables: [{ name: "Knowledge", formula: "d6", results: [[1,1,"Nightmares"], [2,2,"Fish"], [3,3,"Cold"], [4,4,"Fear"], [5,5,"Storms"], [6,6,"Waves"]] }, { name: "Punishment", formula: "d6", results: [[1,1,"Creatures"], [2,2,"Swim"], [3,3,"Taste"], [4,4,"Sailors"], [5,5,"Salt"], [6,6,"Poison"]] }]
        },
        "The Rat Knight": {
            items: [{ type: "knight", flavor: "Modified Armour", flavorLabel1: "Type", flavorLabel2: "Mod" }, { type: "weapon", name: "Pole Sickle", damage: "d10", long: true }, { type: "weapon", name: "Dart x3", damage: "d6" }, { type: "misc", name: "Listening Horn" }],
            actors: [{ type: "steed", name: "Matted Steed", vigour: 12, clarity: 8, spirit: 5, guard: 3 }],
            tables: [{ name: "Type", formula: "d6", results: [[1,1,"Leather"], [2,2,"Velvet"], [3,3,"Fur"], [4,4,"Scales"], [5,5,"Hair"], [6,6,"Straw"]] }, { name: "Mod", formula: "d6", results: [[1,1,"Fast"], [2,2,"Fire"], [3,3,"Swim"], [4,4,"Fall"], [5,5,"Conceal"], [6,6,"Repel"]] }]
        },
    };
