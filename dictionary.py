cat = {"age" : 5,
       "size": "fat",
       "color": "gray", 
       "noise": "loud"}
cat2 = {"age" : 3,
       "size": "thin",
       "color": "white", 
       "noise": "loud"}
cat3 = {"age" : 1, 
       "size": "thin",
       "color": "black", 
       "noise": "quiet"}
cats= [cat, cat2, cat3]

for c in cats:
    for key in c.keys():
        print(key, " = ", c[key])
    print("=============")
'''
print("age of cat: " + str(cat["age"]) + " and " + 
      "size: " + cat["size"])
print(cat.keys())
print(cat.values())
for key in cat.keys():
    print(key," = ", cat[key])