# import dbcreds
# import mariadb

# conn = mariadb.connect(
#   user=dbcreds.user,
#   password=dbcreds.password,
#   host=dbcreds.host,
#   port=dbcreds.port,
#   database=dbcreds.database
#   )

# cursor = conn.cursor()


# userInput = input('Enter your Name and then email: ')
# names = []
# emails = []

# while users != "*":
#   users.append(userInput)
#   userInput = input("enter a name & email: ")
#   emails.append(inputEmail)
#   inputEmail = input("enter email: ")
# print(names)
# print(emails)
# # for user in users:
# # # name = input('enter name: ')

# #   cursor.execute("INSERT INTO user (name, email) VALUES (?,?)", [])
# #   if(cursor.rowcount == 1):
# #     conn.commit()
# #     print(f"Tyler you updated the db")
# #   else:
# #     print("error, not added")
    


# # # inputName, inputEmail = input("enter a name/email: ").split()
# # # print("the user's name is:", inputName + " and their email is:", inputEmail)
# # # print("name is: ", inputName)
# # # print("email is: ", inputEmail)


# # # need 1 array of tuples (users)
# # # end data structure will be an array of tuples
# # # iterate over that and then take every memeber of that and put into DB


    
# # # for email in emails:
# # #   cursor.execute("INSERT INTO user (emails) VALUES (?)", [emails])
# # #   if(cursor.rowcount == 1):
# # #     conn.commit()
# # #     print(f"Tyler you updated the db")
# # #   else:
# # #     print("error, not added")

# # conn.close
# array1 = []
# array2 = []
# for j in range(20):
#     for i in range(10):
#         array1.append(0)
#     array2.append(array1)
#     array1 = []
# print(array2)