import dbcreds
import mariadb


# name = []
# email = []

# users = list(zip(name, email))
users = []
userInput = input('Enter your Name and then email:\n ')

# users = tuple(int(val) for val in userInput.split())
while userInput != "*":
  # users.append(userInput)
  users.append(tuple(userInput.split()))
  userInput = input("Enter your Name and then email:\n ")
  
  # if userInput == "*":
  #   for user in users:
  #     conn = mariadb.connect(
  #     user=dbcreds.user,
  #     password=dbcreds.password,
  #     host=dbcreds.host,
  #     port=dbcreds.port,
  #     database=dbcreds.database
  #     )

  #     cursor = conn.cursor()  
  #     cursor.execute("INSERT INTO user (name, email) VALUES (?,?)", [])
  #     if(cursor.rowcount == 1):
  #       conn.commit()
  #       print(f"Tyler you updated the db")
  #     else:
  #       print("error, not added")
print(users)


    
# conn.close


# need 1 array of tuples (users)
# end data structure will be an array of tuples
# iterate over that and then take every memeber of that and put into DB




