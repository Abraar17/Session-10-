def CalcSqft(length, width, height):

  return ((2 * length * width) + (2 * length * height) + (2 * width * height))


answer = input("Do you want to do this program? Yes or No")

while (answer == "Yes"):

  length = int(input("Enter length"))
  width = int(input("Enter width"))
  height = int(input("Enter height"))

  sqft = CalcSqft(length, width, height)
  gallons = sqft / 50

  print("You need ", gallons, " gallons of paint to paint this room")

  answer = input("Do you want to continue this program? Yes or No")
