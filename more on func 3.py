
def fp(msrp, model, evcode, make):
  disc=0
  if make=="Honda" and model=="accord": 
    disc=.10
  if make=="Toyota" and model=="Rav4": 
    disc=0.15
  if evcode=="Y":
    disc=.30
  else:
    disc=.05
  return disc 

answer = input("Do you want to do this program? Yes or No")

while (answer == "Yes"):

  make = (input("Enter make"))
  model = (input("Enter model"))
  evcode = (input("Enter evcode"))
  msrp= int(input( "Enter mrsp"))

  price = fp(msrp, model, evcode, make)*msrp
  b=(msrp*0.07) +msrp
  
  

  print (b) 
  tmsrp=tmsrp+msrp
  tsalesprice=tsalesprice+b

  answer = input("Do you want to continue this program? Yes or No")
