# 5e-Magic-Item-Shop
A soon-to-be robust 5e magic item shop generator!

Right now the [shop generator](https://github.com/glynyon-5020/5e-Magic-Item-Shop/blob/main/versions/terminal/basic_terminal_shop_generator.0.02.0.py) is pretty basic. You should be able to clone this repo and, if you have python installed on your machine, run it out of the box. Just open up the _basic_terminal_shop_generator.0.02.0.py_ with Python.

All it currently does is snag an item from a list of items. 20% chance at a common item, 60% chance at an uncommon item, 11% chance at a rare item, 5% chance at a very rare item, and 1% chance at a legendary item.

```py
COMMON_RANGE = (1,21)
UNCOMMON_RANGE = (21,82)
RARE_RANGE = (82,94)
VERY_RARE_RANGE = (94,100)
LEGENDARY_RANGE = (100,101)
```
