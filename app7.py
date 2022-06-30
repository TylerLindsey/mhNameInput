import dbcreds
import mariadb

# clean up code, 
# i currently am creating a new connection everytime I am running the loop
# connection creation is in the loop which is inefficient 
# pull out the conection to be outside the loop and then at the end of the loopclose the connection
# find in slides

# name = []
# email = []

# users = list(zip(name, email))
users = []
userInput = input('Enter your Name and then email:\n ')
# uSE sPLIT iNSTEAD oF tUPLES
# users = tuple(int(val) for val in userInput.split())

conn = mariadb.connect(
      user=dbcreds.user,
      password=dbcreds.password,
      host=dbcreds.host,
      port=dbcreds.port,
      database=dbcreds.database
      )

cursor = conn.cursor()  

while userInput != "*":
  # users.append(userInput)
  users.append(tuple(userInput.split()))
  userInput = input("Enter your Name and then email:\n ")
  
  if userInput == "*":
    for user in users:
      print(user)
      cursor.execute("INSERT INTO user (name, email) VALUES (?,?)", user)
      if(cursor.rowcount == 1):
        print(f"Tyler you updated the db")
      else:
        print("error, not added")
print(users)

conn.commit()

cursor.close()
conn.close






