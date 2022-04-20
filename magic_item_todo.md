# Magic Item Shop Generator To-Do

## JSON Data
- [ ] Add variation rolls to items with a search expression of: `"notes": "[a-z].*"`. (Progress: Line 4847)
- [x] Create a basic Avrae Discord alias
- [x] Create a basic terminal app  
- [x] Add Legendary Items
- [ ] Add Potions
- [ ] Add Spell Scrolls
- [ ] Create a basic **Focus** list
- [ ] Document JSON data types with rough idea of what each field is and how it's meant to be used
- [ ] Figure out a way to handle rolls for spells; might need to create a new object or just leave those to be the one manual rolls



```json
,
      "variation": [
        {
          "type": "Aberrations",
          "cost_in_gold": 1500,
          "roll_id": 1
        },
        {
          "type": "Celestials",
          "cost_in_gold": 1500,
          "roll_id": 2
        },
        {
          "type": "Constructs",
          "cost_in_gold": 1500,
          "roll_id": 3
        },
        {
          "type": "Dragons",
          "cost_in_gold": 1500,
          "roll_id": 4
        },
        {
          "type": "Elementals",
          "cost_in_gold": 1500,
          "roll_id": 5
        },
        {
          "type": "Fey",
          "cost_in_gold": 1500,
          "roll_id": 6
        },
        {
          "type": "Fiends",
          "cost_in_gold": 1500,
          "roll_id": 7
        },
        {
          "type": "Giants",
          "cost_in_gold": 1500,
          "roll_id": 8
        },
        {
          "type": "Monstrosities",
          "cost_in_gold": 1500,
          "roll_id": 9
        },
        {
          "type": "Undead",
          "cost_in_gold": 1500,
          "roll_id": 10
        }
      ],
      "dice_rolls": {
        "variation": "1d10"
      }
```
