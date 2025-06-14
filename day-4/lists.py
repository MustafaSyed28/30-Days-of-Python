# lists

list1= ["father", "mother", "child1", "child2", "child3", "child4"]                    # 2-ways to assing list
list2= list(["joseph", "rose", "andrey", "abigel", "zain", "amir"])

list3= ["hi", 2, 8.88, '5', False, [1,2]]            # list can have any variable and duplicates



print(list1)
print(list2)

a= list1[0]          # print list index0
print(a)

b= list2[1:]         # print from list index1-----end
print(b)

c= len(list1)        # length of list
print(c)

d= type(list2)       # type of list
print(d)

e= list1[5]= "girl"       # it will change the (index of list1, also variable-e) to girl
print(e)                    # also you can assign it any thing like even (list2[5])
print(list1)         # note how it prints "child4" its changed it to girl (but we just change the variable)

f= list2[2:] = ["boy", "boy", "boy", "girl"]          # what ever range you are changing should in list[here]
print(f)                                              # also you can put any thing is list
print(list2)

# for not complicating things i am assigning the list again
list1= ["father", "mother", "child1", "child2", "child3", "child4"]
list2= list(["joseph", "rose", "andrey", "abigel", "zain", "amir"])



g= list1.append("no5")            # appends anything you assign to the end
print(list1)

h= list2.insert(5, "bill")       # insert "bill" at index5
print(list2)

i= list1.pop()                    # remove last index in the list
print(list1)

j= list2.remove("amir")          # removes the variable which you provided [note: you have to write the variable you want to remove]
print(list2)

m= list1.count("rose")
print(m)

k= list1.reverse()                # reverse the list
print(list1)

l= list2.sort()                   # sort the list
print(list2)

z= list2.extend(list1)            # add list to another list
print(list2)

list4= list3                      # copies list to another list
print(list4)

list3= list1.copy()               # another way of copying list
print(list3)

join= list1 + list2               # join two list
print(join)

clear1= list1.clear()              # clear the list
print(list1)

clear2= list2.clear()
print(list2)




