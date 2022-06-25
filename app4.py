from dbcreds import *
import mariadb

inputName = input("enter a name: ")
names = []

while inputName != "*":
  # aCCEPT iNPUT fROM uSER
  names.append(inputName)
  inputName = input("enter a name: ")
  if inputName == "*":
    print(names)
