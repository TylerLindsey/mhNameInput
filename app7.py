import dbcreds
import mariadb

conn = mariadb.connect(
  user=dbcreds.user,
  password=dbcreds.password,
  host=dbcreds.host,
  port=dbcreds.port,
  database=dbcreds.database
  )

cursor = conn.cursor()

users = []
userInput = input('Enter your Name and then email:\n ')

# users = tuple(int(val) for val in userInput.split())
while userInput != "*":
  # users.append(userInput)
  users.append(tuple(userInput.split()))
  userInput = input("Enter your Name and then email:\n ")
print(users)

# for user in users:
# name = input('enter name: ')

  # cursor.execute("INSERT INTO user (name, email) VALUES (?,?)", [])
  # if(cursor.rowcount == 1):
  #   conn.commit()
  #   print(f"Tyler you updated the db")
  # else:
  #   print("error, not added")
    
conn.close


# need 1 array of tuples (users)
# end data structure will be an array of tuples
# iterate over that and then take every memeber of that and put into DB




