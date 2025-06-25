dic1= {
    "name": "iris",
    "year": 2000,
    "month": "october",
}

dic2= dict({"name": "jacob", "year": 2002, "month": "april"})              # 2-ways to assign dictionary

print(dic1)
print(dic2)
print(len(dic1))
print(type(dic2))


valDic1= dic1["name"]             # access value of provided key
print(valDic1)

valDic1= dic1.get("month")        
print(valDic1)

valDic2= dic2["month"][0:3]
print(valDic2)

valDic2= dic2.values()            # print all dic2 valuse
print(valDic2)

# you cannot access key from dictionary

keyDic1= dic1.keys()              # print all dic1 keys
print(keyDic1)

keyDic2= dic2.keys()              # print all dic2 keys
print(keyDic2)

itemDic1= dic1.items()            # print all dic1 items
print(itemDic1)

itemDic2= dic2['year']= list([2001, 2002])   # changing item of keys in dictionary
print(dic2)

itemDic1= dic1.update({"year": 1999})        # changing item of keys in dictionary
print(dic1)

dic3= {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}

print(dic3)

dic3.popitem()               # removes the last key-value pair from dictionary
print(dic3)

dic3.pop("d")                # removes the specified(key-value) pair from dictionary
print(dic3)

dic1.clear()                # clear the dictionary
print(dic1)

del dic2                    # delete the dictionary

dic1= {
    "name": "iris",
    "year": 2000,
    "month": "october",
}

dic2= dict({"name": "jacob", "year": 2002, "month": "april"})


for x in dic1:
  print(x)

for y in dic2:
  print(dic2[y])

for z in dic2.values():
  print(z)

for m in dic1.items():  
  print(m)

school= {
    "principle":{
        "name": "trump",
        "age": 50,
        "salary": 100000,
    },

    "Viceprinciple":{
        "name": "obama",
        "age": 40,
        "salary": 80000,
    },

    "professor":{
        "name": "putin",
        "age": 30,
        "salary": 60000,
    },
}

print(school)
print(school["principle"])
print(school["professor"]["age"])
print(school["Viceprinciple"]["name"][-1])

school={
   "principle": {"level": [90,100], 
                 "class":{12: ["a","b"], 
                           11: ["a","b"]
                          }
                          } ,
   "vicePrinciple": {"level": [70,90], 
                     "class":{10: ["a","b"], 
                              9: ["a","b"]
                              }
                              },
   "teacher": {"level": [60,70], 
               "class":{8: ["a","b"], 
                        7: ["a","b"], 
                        "extra":{5: "all", 
                                 6: "a and b"
                                 }
                                 }
                                 },
}


print(school["principle"]["level"][1])
print(school["teacher"]["class"])
print(school["teacher"]["class"]["extra"])

