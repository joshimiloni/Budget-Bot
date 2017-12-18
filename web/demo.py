 # -*- coding: utf-8 -*-
import json

r = [{'update1': '28% slab pruning cost to government 20,000 crore'}, {'update2': '1 % composition rate for manufacturers & traders '}, {'update3': 'Reduced from 28% to 18% W.e.f. 15th Nov 2017 – Shampoo, Perfume, tiles, watches'}, {'update4': 'Reduced from 28% to 12% – Wet grinders, tanks'}, {'update5': 'Reduced from 18% to 12% – Condensed milk, refined sugar, diabetic food'}, {'update6': 'Reduced from 12% to 5% – Desiccated coconut, idli dosa batter, coir products'}, {'update7': 'Reduced from 5% to Nil – Duar meal, khandsari sugar, dried vegetables'}, {'update8': 'Restaurants within hotels (room tariff <7,500- 5% without ITC'}, {'update9': 'Restaurants within hotels (room tariff >7,500 ) still 18% with ITC'}, {'update10': 'Outdoor catering 18% with ITC'}]

f = open("jsondump1.json","w+")
jsonFile = open("demo.json","r+")
data = json.load(jsonFile)
tmp = data["updates"]
data["updates"]=r
f.write(json.dumps(data))


