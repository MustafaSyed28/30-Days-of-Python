# match

day= 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


person = ("Alice", 25)

match person:
    case (name, 25):
        print(f"{name} is 25 years old.")
    case _:
        print("No match.")    


colors = ["red", "blue", "green"]

match colors:
    case [a, b, c]:
        print(f"Three colors: {a}, {b}, {c}")
    case _:
        print("Color list doesn't have 3 items")        