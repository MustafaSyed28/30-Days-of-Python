# tuples

# -> assigning
tuple1 = ("max", "jane", "alex", 100, 80, 95)
print(tuple1)
print(len(tuple1))
print(type(tuple1))
print(tuple1[::-1])

tuple2 = tuple(("adam", "john", "sam", 70, 85, 96))
print(tuple2)
print(tuple2[:3])


# -> updating
list1 = list(tuple1)
print(list1)

list1 = list(tuple1)
list1[3] = 99
tuple1 = tuple(list1)
print(tuple1)


# -> packing & unpacking

marks = tuple((100, 95, 99, 86, 80, 79))
(*topper, acer, acer, average ) = marks

print(topper)
print(acer)
print(average)


# -> joining tuples

fruits = ("apple", "mango", "avocado", "melon", "grapes")
vegetables = ("spinach", "lettuce", "cucumber", "onion")
mix = fruits + vegetables
print(mix)
print(type(mix))

twins = fruits * 2
print(twins)


# -> .functions

count = twins.count("mango")
print(count)

place = fruits.index("avocado")
print(place)

