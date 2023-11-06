def NextMonthSales(month, sales):
  if (month == "jan" or month == "feb" or month == "mar"):
    return 0.10
  elif (month == "apr" or month == "may" or month == "jun"):
    return 0.15
  elif (month == "jul" or month == "aug" or month == "sep"):
    return 0.20
  elif (month == "oct" or month == "nov" or month == "dec"):
    return 0.25


answer = input("Do you want to continue the program? Yes or No")

while (answer == "Yes"):
  lastname = input ("Enter last name")
  month = input("Enter month first 3 letters")
  sales = int(input("Enter sales"))

  forcasted_sales = sales * (1 + NextMonthSales(month, sales))


  print ("The forcasted sales for next month are ", forcasted_sales)

  answer = input("Do you want to continue? type 'No' to quit")