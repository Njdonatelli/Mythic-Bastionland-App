The details section needs to have its contents display the association to any items, actors, or actions.


<<Example 1>>

{

      "name": "The True Knight",

      "items": [

        {

          "type": "knight",

          "name": "The True Knight",

          "description": "A pact to uphold truth. The false slung broken upon their lies.",

          "flavor": "Symbol of Truth", 

          "flavorLabel1": "Trigger",

          "flavorLabel2": "Effect"
## Find reference to Trigger and Effect, context: Symbol of Truth

        },

        {

          "type": "shield",

          "name": "kite shield",

          "damage": "d4",

          "armor": 1,

          "description": "Marked with a symbol of the truth" 

## Symbol of Truth is associated to the kite shield. Deduce that the kite shield has trigger and effect.

        }

      ]

    },

<<END>>

<<Example 2>>

{

      "name": "The Snare Knight",

      "items": [

        {

          "type": "knight",

          "name": "The Snare Knight",

          "description": "Immersed within the woods. A sheriff of natural order",

          "flavor": "Knight & Companion",

          "flavorLabel1": "History",

          "flavorLabel2": "Type"
## Find reference to History and Type, context: Knight & Companion
        },
 {

      "name": "The Snare Knight",

      "items": [

        {

          "type": "steed",

          "name": "Tattered steed",

          "vigour": 8,

          "clarity": 10,

          "spirit": 5,

          "guard": 2

        },

        {

          "type": "npc",

          "name": "Companion",

## Companion Found. Deduce that History and/or type relates to companion.

          "biography": "Partially understands human speech.",

          "vigour": 5,

          "clarity": 10,

          "spirit": 7,

          "guard": 4

        }

      ]

    },
{
      "name": "The Snare Knight",
      "items": [
        {
          "name": "History",
          "formula": "d6",
          "results": [
            [ 1, 1, "Exiled" ],
            [ 2, 2, "Feral" ],
            [ 3, 3, "Vengeful" ],
            [ 4, 4, "Shamed" ],
            [ 5, 5, "Jovial" ],
            [ 6, 6, "Artistic" ]
## Assess history context
## History table contents share relationship with knight description. Deduce that history pertains to knights background. Add to background details.
          ]
        },
        {
          "name": "Type",
          "formula": "d6",
          "results": [
            [ 1, 1, "Otter" ],
            [ 2, 2, "Hare" ],
            [ 3, 3, "Rat" ],
            [ 4, 4, "Weasel" ],
            [ 5, 5, "Ferret" ],
            [ 6, 6, "Squirrel" ]
## Assess type context
## Type table contents share relationship with companion. Deduce that type pertains to companion. Add to companion details.
          ]
        }
      ]
    },

<<END>>

<<Example 3>>

 {

      "name": "The Tourney Knight",

      "items": [

        {

          "type": "knight",

          "name": "The Tourney Knight",

          "description": "A calling brought a life of combat. Nay a protector, in fact a competitor.",

          "flavor": "Calling and Helm",

          "flavorLabel1": "Call to Battle",

          "flavorLabel2": "Fancy Helm"
## Find Call to Battle and Fancy Helm, context: Calling and Helm

        },

        {

          "type": "ability",

          "name": "Champion Vow",
## Vow shares relationship with Calling. Deduce that calling relates to knight background. Add to background details.
          "description": "Use immediately before a combat where there is a prize at stake. +[[/roll d6 #damage]] to melee attacks for the whole combat."

        },

        {

          "type": "passion",

          "name": "Hatred",

          "description": "Restore SPI when you refuse a plea for forgiveness."

        },

        {

          "type": "helm",

          "name": "Fancy helm",

## Fancy Helm found. Deduce that Fancy Helm table contents relate to helm. Add to helm details.

          "armor": 1

        },

        {

          "type": "plate",

          "name": "Arena plate",

          "armor": 1

        },

        {

          "type": "coat",

          "name": "Gambeson",

          "armor": 1

        },

        {

          "type": "weapon",

          "name": "Greatlance",

          "damage": "2d10",

          "slow": true,

          "description": "Hefty when mounted, slow on foot"

        },

        {

          "type": "weapon",

          "name": "Javelin",

          "damage": "d6"

        },

        {

          "type": "weapon",

          "name": "Javelin",

          "damage": "d6"

        }

      ]

    },

 {

      "name": "The Tourney Knight",

      "items": [

        {

          "name": "Call to Battle",

          "formula": "d6",

          "results": [

            [ 1, 1, "Greed" ],

            [ 2, 2, "Bloodlust" ],

            [ 3, 3, "Glory" ],

            [ 4, 4, "Duty" ],

            [ 5, 5, "Pride" ],

            [ 6, 6, "Ambition" ]

          ]

        },

        {

          "name": "Fancy Helm",

          "formula": "d6",

          "results": [

            [ 1, 1, "Lion" ],

            [ 2, 2, "Shark" ],

            [ 3, 3, "Great Crest" ],

            [ 4, 4, "Hawk" ],

            [ 5, 5, "Bull" ],

            [ 6, 6, "Demon" ]

          ]

        }

      ]

    },

{

      "name": "The Tourney Knight",

      "items": [

        {

          "type": "steed",

          "name": "Horned Stallion",

          "vigour": 12,

          "clarity": 10,

          "spirit": 5,

          "guard": 4,

          "trample": "d6"

        }

      ]

    },

<<END>>

<<Example 4>>

{

      "name": "The Bloody Knight",

      "items": [

        {

          "type": "knight",

          "name": "The Bloody Knight",

          "description": "Some were born to fight. This one birthed from the very blood of battle.",

          "flavor": "Rage Fuel",

          "flavorLabel1": "Alcohol",

          "flavorLabel2": "Hatred"
## Find Alcohol and Hatred, context: rage fuel
        },

        {

          "type": "ability",

          "name": "Bloody Echo",

          "description": "Use immediately after defeating an opponent. Your next melee attack in this combat gains Blast."

        },

        {

          "type": "passion",

          "name": "Justice",
## Hatred and Justice may have some narrative or linguistic association. Continue scanning for any other options.
          "description": "Restore SPI when you restore the balance of justice."

        },

        {

          "type": "helm",

          "name": "Helm",

          "armor": 1

        },

        {

          "type": "plate",

          "name": "Brutal plate",

          "armor": 0,

          "description": "A1 only when Wounded"

        },

        {

          "type": "coat",

          "name": "Mail",

          "armor": 1

        },

        {

          "type": "misc",

          "name": "Sacks of very strong alcohol, to which you're largely resistant",
## Alcohol found. Deduce that Alcohol table contents relate to alcohol. Update alcohol name.

          "quantity": 1

        },

        {

          "type": "weapon",

          "name": "Longaxe",

          "damage": "d10",

          "long": true

        }

      ]

    },
    {
      "name": "The Bloody Knight",
      "items": [
        {
          "type": "steed",
          "name": "Bullish warhorse",
          "vigour": 15,
          "clarity": 5,
          "spirit": 5,
          "guard": 3,
          "trample": "d6"
        }
      ]
    },
     {
      "name": "The Bloody Knight",
      "items": [
        {
          "name": "Alcohol",
          "formula": "d6",
          "results": [
            [ 1, 1, "Burning Wine" ],
            [ 2, 2, "Strong Mead" ],
            [ 3, 3, "Spiced Ale" ],
            [ 4, 4, "Sour Milk" ],
            [ 5, 5, "Fermented Vegetable" ],
            [ 6, 6, "Blood Brew" ]
          ]
        },
        {
          "name": "Hatred",
          "formula": "d6",
          "results": [
            [ 1, 1, "The Rich" ],
            [ 2, 2, "Knights" ],
            [ 3, 3, "The Poor" ],
            [ 4, 4, "Seers" ],
            [ 5, 5, "The Sea" ],
            [ 6, 6, "The Sun" ]
## Justice and the rich, knights, the poor, and seers make linguistic sense. However, Justice and The Sea or The Sun makes little linguistic sense. 
## Deduce hatred must relate to knight background. Add Hatred to background details.

<<END>>

<<Example 5>>

{
      "name": "The Moss Knight",
      "items": [
        {
          "type": "knight",
          "name": "The Moss Knight",
          "description": "The tree and stone had no need to be taught. The wisest knew to study beneath them.",
          "flavor": "Full body Tattoos",
          "flavorLabel1": "Design",
          "flavorLabel2": "Effect"
## Find Design and Effect, context: Full body tattoos.
        },
        {
          "type": "ability",
          "name": "Mosstongue",
          "description": "Speak with uncut stones and particularly old trees. If you push them for too much knowledge they rebuke you, shunning you for the rest of the day."
        },
        {
          "type": "passion",
          "name": "Naturality",
          "description": "Restore SPI when you reject an opportunity to sleep indoors, sleeping in nature instead."
        },
        {
          "type": "helm",
          "name": "Mail coif",
          "armor": 1
        },
        {
          "type": "shield",
          "name": "Buckler",
          "armor": 1,
          "damage": "d4"
        },
        {
          "type": "weapon",
          "name": "Branch cudgel",
          "damage": "d8",
          "hefty": true
        }
      ]
    },
    {
      "name": "The Moss Knight",
      "items": [
        {
          "type": "steed",
          "name": "Pale steed",
          "vigour": 8,
          "clarity": 12,
          "spirit": 5,
          "guard": 3
        }
      ]
    },
    {
      "name": "The Moss Knight",
      "items": [
        {
          "name": "Design",
          "formula": "d6",
          "results": [
            [ 1, 1, "Faded Spirals" ],
            [ 2, 2, "Blue Thorns" ],
            [ 3, 3, "Silver Stars" ],
            [ 4, 4, "Pale Snakes" ],
            [ 5, 5, "Red Bones" ],
            [ 6, 6, "Burnt Rings" ]
          ]
        },
        {
          "name": "Effect",
          "formula": "d6",
          "results": [
            [ 1, 1, "Points to Water" ],
            [ 2, 2, "Burns before an ambush" ],
            [ 3, 3, "A1 in saltwater" ],
            [ 4, 4, "A1 under moonlight" ],
            [ 5, 5, "A1 in rivers or streams" ],
            [ 6, 6, "Conceals a third eye" ]
          ]
        }
      ]
    },
## No specific context found. Deduce Full Body Tattoos are ability. Add Full Body Tattoos to features.
<<END>>

## Based on the examples, knight profiles should have space for knight backgrounds.






I need this document cleaned up and formatted for improved human and LLM readability. Keep all writing style the same, there is a lot of old english and poetry in the text that does not follow modern grammatical rules.


张 Characters need to be removed

"![](_page_66_Picture_2.jpeg)" strings need to be removed

## 2 Residual page numbers need to be removed