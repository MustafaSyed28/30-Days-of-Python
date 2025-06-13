# sets

set1= {1, 2, 3, "hello", "hi", "bye"}
set2= { 100, 200, 500, 100, 100, 100}
set3= set({100, True, 0, False, 1, 3.20})
print(set1)
print(set2)
print(set3)

set2.add(300)
print(set2)

set2.update(set3)
print(set2)
