# Add a connection to DB and then the DB should have a table with names and that is going to store those names


inputName = input("enter a name: ")
names = []

while inputName != "*":
  # aCCEPT iNPUT fROM uSER
  names.append(inputName)
  inputName = input("enter name a name: ")
  if inputName == "*":
    print(names)





# while inputName != "*":
#   # aCCEPT iNPUT fROM uSER
#   inputName.append()
#   inputName = input("enter name a name: ")
# else:
#   print(inputName)




# while the input is not * print the name
# use a loop to put the names into "storage" 
# when inpt = * exit the loop and print all the names/