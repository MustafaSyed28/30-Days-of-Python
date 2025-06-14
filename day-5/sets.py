# sets

set1= {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
set2= set(["dad", "mom", "zain", "mohd", "john", "alex"])
set3= {True, 0, False, 1, 3.8, 25, 'ab'}

print(set1)
print(set2)
print(set3)
print(len(set1))

set2.add("georg")             # adding new items
print(set2)
set2.add("chris")
print(set2)

set1.update(set3)           # adding new set into set
print(set1)

set2.remove("georg") 
set2.remove("chris")         # removing items from set
print(set2)

set1.discard(5)             # removing items from set
print(set1)

set1.pop()                  # removes one item randomly
set1

set1.clear()               # clear the set (it shows empty set)
print(set1)

del set2                  # erease the set from data
del set1


# forming new sets
# sets .functions

a= {1,2,3,4,5}
b= {4,5,"a","b","c","d","e"}

l= a.union(b)            # set union 2-ways
x= a | b
print(l)
print(x)

m= a.intersection(b)     # set intersection 2-ways
y= a & b
print(m)
print(y)

n= a.difference(b)       # set difference 2-ways
z= a - b
print(n)
print(z)

o= a.symmetric_difference(b)     # set symmetric difference 2-ways
w= a ^ b
print(o)
print(w)
