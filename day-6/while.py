# while loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


j = 0
while j < 4:
  j += 1
  if j == 3:
    continue
  print(j)  


k = 1
while k < 6:
  print(k)
  k += 1
else:
  print("i is no longer less than 6")  