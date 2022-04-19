import json
from random import randint, choice

with open(r'items\the_source\magic_items.json', 'r', encoding='utf8') as data_file:
  data = data_file.read()

obj = json.loads(data)

common_items = [item['name'] for item in obj['common_items']]
uncommon_items = [item['name'] for item in obj['uncommon_items']]
rare_items = [item['name'] for item in obj['rare_items']]
very_rare_items = [item['name'] for item in obj['very_rare_items']]
legendary_items = [item['name'] for item in obj['legendary_items']]

number_of_items = int(input("How many items would you like in your shop? "))

COMMON_RANGE = (1,21)
UNCOMMON_RANGE = (21,82)
RARE_RANGE = (82,94)
VERY_RARE_RANGE = (94,100)
LEGENDARY_RANGE = (100,101)
stock = []

def roll_for_rarity():
  """Uses the constant values to determine a range on a scale of 1-100 for the differing tiered magic items in 5th edition

  Returns:
      dict: returns a dictionary that has a string value for 'rarity' and an integer (value between 1-100) for 'd100'.
  """
  roll_and_result = {
    "rarity": '',
    "d100": randint(1,100)
  }

  if roll_and_result['d100'] in range(COMMON_RANGE[0], COMMON_RANGE[1]):
    roll_and_result['rarity'] = 'common'
  elif roll_and_result['d100'] in range(UNCOMMON_RANGE[0], UNCOMMON_RANGE[1]):
    roll_and_result['rarity'] = 'uncommon'
  elif roll_and_result['d100'] in range(RARE_RANGE[0], RARE_RANGE[1]):
    roll_and_result['rarity'] = 'rare'
  elif roll_and_result['d100'] in range(VERY_RARE_RANGE[0], VERY_RARE_RANGE[1]):
    roll_and_result['rarity'] = 'very rare'
  elif roll_and_result['d100'] in range(LEGENDARY_RANGE[0], LEGENDARY_RANGE[1]):
    roll_and_result['rarity'] = 'legendary'
  return roll_and_result

def get_item_based_on_rarity(obj):
  item = ''
  if obj['rarity'] == 'common':
    item = f"{choice(common_items)} ({obj['rarity']})"
  if obj['rarity'] == 'uncommon':
    item = f"{choice(uncommon_items)} ({obj['rarity']})"
  if obj['rarity'] == 'rare':
    item = f"{choice(rare_items)} ({obj['rarity']})"
  if obj['rarity'] == 'very rare':
    item = f"{choice(very_rare_items)} ({obj['rarity']})"
  if obj['rarity'] == 'legendary':
    item = f"{choice(legendary_items)} ({obj['rarity']})"
  return item

for _ in range(number_of_items):
  rarity = roll_for_rarity()
  stock.append(get_item_based_on_rarity(rarity))
  print(f"1d00 --> {rarity['d100']} results in a {rarity['rarity']} item.")

  
print("\nThe following items have been generated for your shop!\n")
print("------"*20)
for item in stock:
  print(item)
print("------"*20)
