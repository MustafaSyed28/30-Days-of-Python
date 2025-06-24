# if-else conditions

a= input("enter your age: ")
a= int(a)

if a>= 18:
  print("YOU ARE AN ADULT")
else:
  print("YOU ARE MINOR")



num = 7

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")



num = -3

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")



pizza= 0

if pizza > 1:
  print(f"{pizza} slices are left")
elif pizza == 1:
  print(f"{pizza} slice left")
else:
  print(f"pizza is finished")   



myGrades= input("type your grades ")
myGrades= int(myGrades)

if myGrades >= 95:
  print("CONGRATULATIONS YOU GOT A+")
elif myGrades >= 89:
  print("YOU GOT A")
elif myGrades >= 80:
  print("YOU GOT B+")
elif myGrades >= 75:
  print("you gor B")  
elif myGrades >= 70:  
  print("YOU GOT C")
elif myGrades >= 60:
  print("YOU GOT D")
elif myGrades >= 50:
  print("YOU GOT E") 
else:
  print("YOU FAILED")



MyBalance= input("enter your balance: $")
MyBalance= int(MyBalance)
xboxSeriesX= 499
ps5= 599
nintendo= 399
ps4= 299

if MyBalance >= 600:
  print("you can by xbox series x")
  print("you can by ps5")
  print("you can by nintendo")
  print("you can by ps4")

elif MyBalance >= 500:
  print("you cannot buy ps5")
  print("but you can buy")
  print("series x")
  print("nintendo")
  print("ps4")

elif MyBalance >= 400:
  print("you cannot buy ps5")
  print("you cannot buy XboxSeriesX")
  print("but you can buy")
  print("nintendo")
  print("ps4")

elif MyBalance >= 300:
  print("you cannot buy ps5")
  print("you cannot buy XboxSeriesX")
  print("you cannot buy nintendo")
  print("but you can buy")
  print("ps4")

else:
  print("you cannot buy anything")     
