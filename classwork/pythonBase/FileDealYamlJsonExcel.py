# -*- coding :UTF-8
# @Time     :2020/11/1 16:35
# @autor    :cxf
# @File     :FileDealYamlJsonExcel.py

"""
excel第三方官方库
http://www.python-excel.org/
https://openpyxl.readthedocs.io/en/stable/usage.html


json库
https://docs.python.org/3/library/json.html

yaml

"""
 # json
# import io
import json
from io import StringIO
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

# json.dump(['streaming API'], io)
# io.getvalue()


# yaml
import yaml
print(yaml.load("""
 name: Vorlin Laruknuzum
 sex: Male
 class: Priest
 title: Acolyte
 hp: [32, 71]
 sp: [1, 13]
 gold: 423
 inventory:
 - a Holy Book of Prayers (Words of Wisdom)
 - an Azure Potion of Cure Light Wounds
 - a Silver Wand of Wonder
 """))

#打印结果
# {'name': 'Vorlin Laruknuzum', 'gold': 423, 'title': 'Acolyte', 'hp': [32, 71],
# 'sp': [1, 13], 'sex': 'Male', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)',
# 'an Azure Potion of Cure Light Wounds', 'a Siver Wand of Wonder'], 'class': 'Priest'}

print(yaml.dump({'name': "The Cloak 'Colluin'", 'depth': 5, 'rarity': 45,
'weight': 10, 'cost': 50000, 'flags': ['INT', 'WIS', 'SPEED', 'STEALTH']}))

# yaml文件转换成字典或者列表
print(yaml.load(open("yaml.yml"),Loader=yaml.FullLoader))

# 字段或者列表转换成yaml格式
with open("yamlchange.yml","w") as f:
    yaml.dump(data = {'a':[1, 2]},stream = f)