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



# inputName = input("enter a name: ")
# names = []
# inputEmail = input("enter email: ")
# emails = []


# while inputName != "*":
#   names.append(inputName)
#   inputName = input("enter a name: ")
#   emails.append(inputEmail)
#   inputEmail = input("enter email: ")
# print(names)
# print(emails)

# for name in names:
# # name = input('enter name: ')

#   cursor.execute("INSERT INTO user (name) VALUES (?)", [name])
#   if(cursor.rowcount == 1):
#     conn.commit()
#     print(f"Tyler you updated the db")
#   else:
#     print("error, not added")
    
# for email in emails:
#   cursor.execute("INSERT INTO user (emails) VALUES (?)", [emails])
#   if(cursor.rowcount == 1):
#     conn.commit()
#     print(f"Tyler you updated the db")
#   else:
#     print("error, not added")
# conn.close
