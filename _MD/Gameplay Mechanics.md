---
ID: character_creation
TITLE: "Character Creation & Advancement"
TYPE: engine
TAGS: [core, creation, progression]
---
# Character Creation & Advancement
 
## Algorithm
 
### 1. Define Start
**Input:** Player Choice (Start Type)
**Process:**
IF Start IS "Wanderer":
 * **Rank:** Knight-Errant (0 Glory)
 * **Guard (GD):** Roll 1d6
 * **Virtues:** Roll d12 + d6 for each (VIG, CLA, SPI)
 * **Context:** Seek Glory, seek Seer's counsel
 
ELSE IF Start IS "Courtier":
 * **Rank:** Knight-Gallant (3 Glory)
 * **Guard (GD):** Roll 2d6
 * **Virtues:** Roll d12 + 6 for each (VIG, CLA, SPI)
 * **Context:** Place in Court, receive Omen as news
 
ELSE IF Start IS "Ruler":
 * **Rank:** Knight-Tenant (6 Glory)
 * **Guard (GD):** Roll 1d6 + 6
 * **Virtues:** Roll d12 + 6 for each (VIG, CLA, SPI)
 * **Context:** Rule a Holding, Seat of Power under wicked influence
 
### 2. Determine Attributes
**Virtues:**
* **VIG (Vigour):** Strength,  physical stamina.
* **CLA (Clarity):** Instinct, senses, wits.
* **SPI (Spirit):** Charm, will, heart.
**Guard (GD):** Skill at avoiding Wounds.
**Limit:** Virtues cannot exceed 19 or drop below 0.
 
### 3. Assign Knight & Equipment
* **Roll:** d6 (Page Group) and d12 (Specific Knight).
* **Inventory:** Dagger (d6), torches, rope, dry rations, camping gear.
* **Feats:** All Knights know Smite, Focus, Deny.
* **Oath:** Seek the Myths, Honour the Seers, Protect the Realm.
 
### 4. Squire Generation (Optional)
IF Company Size <= 2 Knights:
 * **Virtues:** 2d6 each.
 * **Guard:** 1.
 * **Equipment:** Pony + Dagger + 1d6 Roll on Equipment Table (Cudgel, Axe, Hatchet, Shortbow, Shield, or Javelins).
 * **Progression:** When Knighted, gain +d6 to all Virtues.
 
### 5. Progression (Glory & Rank)
**Gain Glory (+1) IF:**
* Myth Resolved.
* Won Duel/Joust (Staked Glory).
* Won Tournament (Significant spectacle).
* Won Large Battle.
* New Age begins.
 
**Rank Thresholds:**
* **0 Glory:** Knight-Errant (Lead Warband).
* **3 Glory:** Knight-Gallant (Council/Court Seat).
* **6 Glory:** Knight-Tenant (Rule Holding).
* **9 Glory:** Knight-Dominant (Rule Seat of Power).
* **12 Glory:** Knight-Radiant (City Quest).
 
===END_FILE===
---
ID: core_resolution
TITLE: "Core Resolution Mechanics"
TYPE: engine
TAGS: [core, checks, time]
---
# Core Resolution Mechanics
 
## Algorithm
 
### 1. Saves
**Trigger:** Risky action with uncertain outcome.
**Process:** Roll d20.
**Outcome:**
* IF Roll <= Virtue: Success.
* IF Roll > Virtue: Failure (negative consequences).
 
### 2. Turns (Time)
**Sequence:**
1. **Surprise Check:** IF unreadied, Pass CLA Save OR miss first turn.
2. **Player Phase:** Players act in any order.
3. **Referee Phase:** NPCs react/act.
4. **Reaction Check:** IF NPC uncertain, Pass SPI Save OR unfavourable reaction.
 
**Action Economy:**
* **Turn:** Move + Action (Strict order).
* **Minor Actions:** Changing weapons, dismounting (Do not consume Action).
 
### 3. States
* **Exposed:** Caught off guard/defenceless. Treat GD as 0.
* **Impaired:** Attack rolls become d4. Cannot gain bonus dice or Feats.
* **Fatigued:** Cannot use Feats until Rest.
 
===END_FILE===
---
ID: combat_procedure
TITLE: "Combat & Damage"
TYPE: engine
TAGS: [combat, Damage]
---
# Combat & Damage
 
## Algorithm
 
### 1. Attack Sequence
1. **Roll:** Attackers roll Weapon Dice + Bonus Dice.
2. **Defend:** Target/Allies may use **Deny** (Feat).
3. **Maneuver:** Attackers may execute **Gambits**.
4. **Resolve:**
  * Take **Highest Die**.
  * Add **Bolster** bonuses.
  * Subtract **Armour**.
  * Result = **Total Damage**.
 
### 2. Apply Damage
**Input:** Total Damage
**Process:**
1. Subtract Damage from **Guard (GD)**.
2. IF GD >= 1 AND Remaining GD >= 0: **Evade** (No further effect).
3. IF GD reduced to exactly 0: **Scar** (Roll Damage Die on Scar Table).
4. IF Damage > GD:
  * Remaining Damage deducted from **VIGOUR (VIG)**.
  * **Effect:** Wounded.
5. IF VIG Loss >= Half Current VIG: **Mortal Wound**.
  * **Effect:** Down and dying. Die in 1 hour if untended.
6. IF VIG reduced to 0: **Slain**.
 
### 3. Virtue Loss (Non-Damage)
**VIG 0:** Exhausted (Cannot Attack if Moved).
**CLA 0:** Exposed (Treat GD as 0).
**SPI 0:** Impaired (Attacks roll d4 only).
 
### 4. Recovery
* **Guard:** Fully restored after moment of peace.
* **VIG:** Consume *Sustenance* OR Full day hospitality.
* **CLA:** Consume *Stimulant* OR Seer guidance.
* **SPI:** Consume *Sacrament* OR Indulge Passion.
* **All Virtues:** Fully restored at new Season.
 
===END_FILE===
---
ID: combat_feats
TITLE: "Feats & Gambits"
TYPE: engine
TAGS: [combat, abilities]
---
# Feats & Gambits
 
## Mechanics
 
**Constraint:** Feats risk Fatigue. If Fatigued, cannot use Feats.
**Usage:** Once per Attack per combatant.
 
## Algorithm
 
### 1. Smite
**Trigger:** Before rolling Melee Attack.
**Effect:** Gain +d12 OR Blast.
**Cost:** Pass VIG Save OR become Fatigued.
 
### 2. Focus
**Trigger:** After rolling Attack.
**Effect:** Perform Gambit without spending a die.
**Cost:** Pass CLA Save OR become Fatigued.
 
### 3. Deny
**Trigger:** After Attack roll against self/ally.
**Effect:** Discard one Attack die.
**Cost:** Pass SPI Save OR become Fatigued.
 
### 4. Gambits
**Input:** Discard Attack Die >= 4.
**Effects:**
* **Bolster:** +1 Total Damage.
* **Move:** Move after Attack.
* **Control:** Repel, Stop Move, Impair Weapon, Trap Shield, Dismount.
**Defense:** Target rolls VIG Save to ignore (except Bolster/Move).
 
### 5. Strong Gambits
**Input:** Discard Attack Die >= 8 (Melee only).
**Effect:** As Gambit, BUT Target gets **NO SAVE** OR **Greater Effect** (Disarm/Break/etc).
 
===END_FILE===
---
ID: warfare
TITLE: "Warfare & Structures"
TYPE: engine
TAGS: [combat, warband, siege]
---
# Warfare & Structures
 
## Algorithm
 
### 1. Warband Logic
**Definition:** ~24 combatants acting as one unit.
**Stats:**
* **Damage Scale:** Attacks vs Individuals get +d12 AND Blast.
* **Immunity:** Immune to individual attacks (unless Blast/Large Scale).
* **Leadership:** Individual can add Attack Dice to Warband roll (Lead from Front).
  * *Risk:* Leader suffers Warband Damage.
**States:**
* **Mortal Wound:** Routed.
* **VIG 0:** Wiped Out.
* **SPI 0:** Broken (Will not follow orders).
 
### 2. Structures
**Durability:** Destroyed at 0 GD.
**Immunities:** Wooden structures ignore attacks except Fire/Siege/Monsters. Stone walls immune to conventional attacks.
**Repair:** 1 Day to recover GD.
 
### 3. Siege & Ships
**Structures:**
* **Gate:** 5 GD, A2
* **Rampart:** 10 GD, A2
* **Castle Wall:** 10 GD, A3
 
**Vehicles:**
* **Rowboat:** 4 GD (6 passengers)
* **Longship:** 7 GD, A1 (1 Warband)
* **Warship:** 10 GD, A2 (2 Warbands)
* **Collision:** d12 Damage (d6 if size mismatch).
 
**Artillery:**
* **Ram:** d12
* **Stone Thrower:** d12 Blast
* **Bolt Launcher:** 2d12
* **Trebuchet:** 3d12 Blast (Immobile)
 
===END_FILE===
 
---
ID: equipment_and_trade
TITLE: "Equipment & Trade"
TYPE: engine
TAGS: [economy, gear, weapons, armour]
---
# Equipment & Trade
 
## Mechanics
 
**Trade Logic:** Exchange of materials/goods/service. Coins used only by rich.
**Question:** "What can I offer that they would value?"
 
### 1. Weapon Mechanics
* **Hefty:** One-handed. Only one Hefty item at a time.
* **Long:** Two-handed. Impaired in confined spaces.
* **Slow:** Cannot Attack if moved this turn. Also counts as Long.
 
### 2. Armour Mechanics
* **Layering:** Wear one of each TYPE simultaneously (Coat + Plates + Helm + Shield).
* **Total Armour:** Sum of all worn layers.
 
### 3. Equipment List
| Category | Item | Stats | Notes || :--- | :--- | :--- | :--- || **Common** | Hand Weapon | d6 | Dagger, club, handaxe || **Common** | Hefty Weapon | d8 | Spear, mace, axe (Hefty) || **Common** | Long Weapon | d10 | Poleaxe, billhook (Long) || **Common** | Shield | d4, A1 | Round, kite, heater || **Common** | Shortbow | d6 | Long || **Uncommon** | Shortsword | 2d6 ||| **Uncommon** | Lance | d10 | Long (Hefty if mounted) || **Uncommon** | Brutal | 2d10 | Slow (Greataxe, maul) || **Uncommon** | Coat | A1 | Mail, gambeson || **Uncommon** | Helm | A1 | Kettle, nasal, bucket || **Rare** | Longsword | 2d8 | Hefty || **Rare** | Greatsword | 2d10 | Long || **Rare** | Plates | A1 | Cuirass, scale (Slow to don) |
### 4. Remedies (Uncommon)
* **Sustenance:** Restores **VIG**. (Feast).
* **Stimulant:** Restores **CLA**. (Herbal).
* **Sacrament:** Restores **SPI**. (Ritual props).
 
===END_FILE===
 
---
ID: services_and_society
TITLE: "Services & Social Roles"
TYPE: engine
TAGS: [economy, hirelings, npc]
---
# Services & Social Roles
 
## Algorithm
 
### 1. Hiring Services
**Input:** Player Request
**Logic:**
IF Service is Common -> Available everywhere.
IF Service is Uncommon -> Requires specialist/larger Holding.
IF Service is Rare -> Requires lifetime dedication/specific location.
 
**Cost:** Favor or Trade ("What can I offer?").
 
### 2. Service Roster
* **Common:** Servant (2 GD), Guide (4 GD), Sentry (3 GD).
* **Uncommon:** Herbalist (2 GD, treatments), Soldier-at-Arms (6 GD, A2), Archer (3 GD).
* **Rare:** Sage (2 GD, immense knowledge), Alchemist (2 GD), Sellsword (7 GD, A4, 2d8 weapon).
 
### 3. Social Roles
* **Vassal:** Serves a ruler for protection.
* **Vagabond:** Roams, protects self.
* **Knight:** Sworn Oath, holds TITLE/arms.
* **Seer:** Glimpses future, directs Knights/Myths.
 
===END_FILE===
---
ID: realm_generation
TITLE: "Realm & Site Generation"
TYPE: engine
TAGS: [hexcrawl, map, world_building]
---
# Realm & Site Generation
 
## Algorithm: Realm Map
 
**Objective:** Generate a 12x12 Hex Grid Map and populate specific Hexes with Myths and Landmarks.

1. **Grid Setup:** Create a Hex map (typ. 12x12). Scale: 1 Hex = "Hecksleague" (Return hike).
2. **Wilderness Generation:** Roll d12 to cluster hexes by terrain type (e.g., Forest, Swamp using Spark Tables).
3. **Barriers:** Mark 1/6th of Hex edges as impassable (cliffs/deep water).
4. **Holdings:** Populate 4 specific Hexes with Castles/Towns. Designate one as the **Seat of Power**.
5. **Myths:** Populate exactly 6 Remote Hexes with distinct Myths.
6. **Landmarks:** Populate Wilderness with 3-4 of each: Dwelling, Sanctum, Monument, Hazard, Curse, Ruin.
 
## Algorithm: Site Generation (Hex Method)
 
1. **Points:** Draw 6 corners + 1 center. Erase one corner (Exit/Entrance).
2. **Nodes:**
  * 3 Circles (Features/Info).
  * 2 Triangles (Dangers).
  * 1 Diamond (Treasure).
3. **Routes:** Connect neighbors.
  * 3 Open (Solid line).
  * 2 Closed (Crossed line, needs creativity).
  * 1 Hidden (Dotted line, needs exploration).
 
===END_FILE===
---
ID: referee_procedures
TITLE: "Referee Procedures"
TYPE: engine
TAGS: [core, gm_tools, loops]
---
# Referee Procedures
 
## Algorithm: Action Procedure
 
1. **Intent:** What are you trying to do?
2. **Leverage:** What makes it possible?
3. **Cost:** Resource/Virtue loss/Side-effect?
4. **Risk:** IF No Risk -> No Roll. ELSE -> Save or Luck Roll.
5. **Impact:** Show consequences.
 
## Algorithm: Outcome Resolution
 
**IF Success:**
* **Advance:** Move forward.
* **Disrupt:** Lessen threat.
* **Resolve:** End problem.
 
**IF Failure:**
* **Threaten:** New problem.
* **Escalate:** Worsen problem.
* **Execute:** Deliver threat.
 
## Algorithm: Luck Roll
**Input:** d6
* **1:** Crisis (Bad immediately).
* **2-3:** Problem (Potentially bad).
* **4-6:** Blessing (Welcome result).
 
## Algorithm: Primacy of Action
**Rule:** Past actions supersede random prompts/rules. Player deeds are reality.
 
===END_FILE===
---
ID: time_and_seasons
TITLE: "Time, Seasons & Ages"
TYPE: engine
TAGS: [time, calendar, downtime]
---
# Time, Seasons & Ages
 
## Structure
 
**Day Phases:** Morning -> Afternoon -> Night.
**Seasons:** Spring (Green) -> Harvest (Gold) -> Winter (Grey).
**Ages:** Young (Green) -> Mature (Gold) -> Old (Grey).
 
## Algorithm: Advancing Time
 
**Trigger:** End of session OR Natural break.
**Decision:** Agree on time passed (Weeks/Months/Years).
**IF Uncertain:** Roll d6.
* 1: Turn Season/Age NOW.
* 2-3: Turn after NEXT session.
* 4-6: Continue current.
 
## Algorithm: Ageing
 
* **Become Mature:** Reroll Virtues (d12+d6). Keep if Higher.
* **Become Old:** Reroll Virtues. Keep if Lower. Lose d12 VIG at end of Age.
 
## Algorithm: Downtime Activities
 
**Between Seasons:**
1. Restore Virtues.
2. Choose: **Pilgrimage** (Learn), **Courtesy** (Contact/Favor), **Service** (Improve Realm).
 
**Between Ages:**
1. Restore Virtues.
2. Gain 1 Glory.
3. Choose: **Duty** (Great improvement), **Succession** (New Knight), **Legacy** (Successor gains half Glory).
 
===END_FILE===
---
ID: travel_and_exploration
TITLE: "Travel & Exploration"
TYPE: engine
TAGS: [hexcrawl, movement, omens]
---
# Travel & Exploration
 
## Algorithm: Travel Move
 
**Cost:** 1 Phase.
**Modes:**
* **Trek:** 1 Hex.
* **Gallop:** 2 Hexes (Steed loses d6 VIG).
* **Cruise:** 3 Hexes (Boat/Road).
 
## Algorithm: Wilderness Event
 
**Trigger:** End phase in Wilderness.
**Roll:** d6.
* **1:** Omen (Random Myth).
* **2-3:** Omen (Nearest Myth).
* **4-6:** Landmark Encounter (OR Clear).
 
**Modifiers:**
* **Myth Hex:** Always reveal next Omen. No roll.
* **Barrier:** Attempt wastes Phase. Still roll Event.
* **Winter:** Lose d6 VIG if camping/night travel.
* **Night:** Lose d6 SPI. Blind if no light.
 
## Algorithm: Gathering Folklore
 
**Source -> Knowledge:**
* **Vassal:** Nearest Myth + Direction. Specific location if adjacent.
* **Knight/Vagabond:** Random Myth + Direction. Nearest Landmark.
* **Seer:** All Myths (Rules/Secrets/Weaknesses/Cures). All Landmarks.
 
===END_FILE===
---
ID: dominion_management
TITLE: "Dominion & Authority"
TYPE: engine
TAGS: [domain, stronghold, politics]
---
# Dominion & Authority
 
## Structure: The Council
 
* **Steward:** Treasury/Rule in absence.
* **Marshall:** Soldiers/War.
* **Sheriff:** Internal threats.
* **Envoy:** Neighbours/Hospitality.
* **The Circle:** Visiting Knights.
 
## Algorithm: Crisis Check
 
**Trigger:** Start of Season OR Return from absence.
**Roll:** d6.
* **1:** Calamity (Gain 2 Crises).
* **2-3:** Dilemma (Choose 1 of 2 Crises).
* **4-6:** Prosperity.
 
**Crisis List:** Chaos, Debt, Famine, Misery, Panic, Doubt.
**Failure State:** 3+ Unresolved Crises at Season end = **Misrule** (Revolt).
 
## Algorithm: Authority Actions
 
* **Muster:** Seat of Power (3 Warbands), Holding (2 Warbands).
* **Projects:**
  * Repair/Renovate: 1 Season.
  * Grand Project (Castle/Road): 1 Age.
* **Tax:** Midspring.
* **Tithe:** Midharvest.
* **Levy:** Midwinter.
* **Squeeze:** Demand extra. Roll d6:
  * 1: Misrule.
  * 2-3: Gain funds, take Crisis.
  * 4-6: Success.
 
===END_FILE===


