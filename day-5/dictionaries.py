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