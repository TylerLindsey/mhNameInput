# # from dbcreds import *
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

# while inputName != "*":
#   # aCCEPT iNPUT fROM uSER
#   names.append(inputName)
#   inputName = input("enter a name: ")
# print(names)
    

# query = (f"INSERT INTO user(name)"+
#               "VALUES ('{names}')") 

# cursor.execute(query)
# print(f"Tyler you updated the db")
# conn.commit()
# conn.close
