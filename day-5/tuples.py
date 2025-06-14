# tuples

tuple1= ("mercury", "venus", "earth", "mars", "jupiter")
tuple2= tuple(("saturn", "urianus", "neptune"))

print(tuple1)
print(tuple2)

planet1= tuple1[0]
print(planet1)

planet5= tuple1[-1]
print(planet5)

planets= tuple1[0:]
planets

skipping= tuple1[::2] + tuple2[1::2]
print(skipping)

allPlanets= tuple1 + tuple2
print(allPlanets)

times2= tuple1 * 2
print(times2)



# you cannot perform .functions on tuple, but to do that there is 1 way

tuple3= list(tuple2)
tuple3.append("pluto")                 # can add new items
tuple2= tuple(tuple3)
print(tuple2)

tuple4= list(tuple1)
tuple4.insert(5, "moon")               # can insert new items
tuple1= tuple(tuple4)
print(tuple1)

tuple5= list(tuple1)
tuple5.remove("moon")                  # can remove items
tuple1= tuple(tuple5)
print(tuple1)

tuple6= list(tuple2)
tuple6.pop()                           # can delete items
tuple2= tuple(tuple6)
print(tuple2)

tuple7= list(tuple1)
tuple7.reverse()                       # can reverse the order
tuple1= tuple(tuple7)
print(tuple1)

tuple8= list(tuple1)
tuple8.sort()                          # can sort the order`
tuple1=tuple(tuple8)
print(tuple1)

# now i am reassigning the tuples

tuple1= ("mercury", "venus", "earth", "mars", "jupiter")
tuple2= tuple(["saturn", "urianus", "neptune"])

del tuple1
del tuple2

