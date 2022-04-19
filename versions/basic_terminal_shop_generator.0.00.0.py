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

COMMON_WEIGHT = 20
UNCOMMON_WEIGHT = 61
RARE_WEIGHT = 12
VERY_RARE_WEIGHT = 6
LEGENDARY_WEIGHT = 1
stock = []

def check_rarity():
  rarity = ''
  d100 = randint(1,100)
  if d100 <= 20:
    rarity = 'common'
    stock.append(choice(common_items))
  elif d100 <= 81:
    rarity = 'uncommon'
    stock.append(choice(uncommon_items))
  elif d100 <= 93:
    rarity = 'rare'
    stock.append(choice(rare_items))
  elif d100 <= 99:
    rarity = 'very rare'
    stock.append(choice(very_rare_items))
  else:
    rarity = 'legendary'
    stock.append(choice(legendary_items))
  
  return [rarity, d100]

for _ in range(number_of_items):
  test = check_rarity()
  print(f"{test[0]}: 1d100 --> {test[1]}\n{stock[_]}\n\n")
