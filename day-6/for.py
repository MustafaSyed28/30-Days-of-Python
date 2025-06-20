# for loops

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num + 10)



word = "hello"
for string in word:
    print(string)



set = {100, 200, 300, 400}
for item in set:
    print(item)



student = {"name": "Ali", "age": 20, "grade": "A"}
for key in student:
    print(key)



set1 = {10, 20, 30, 40,  50}
set2 = {30, 40, 50, 60, 70}

for item in set1:
    if item in set2:
        print(item) 


set1= {1,2,3,4,5,6,7,8,9,10}
set2= {7,8,9,10,11,12,13,14,15}
set_union = set()

for x in set1:
  if x in set2:
    set_union.update(set1.union(set2))

print(set_union)        