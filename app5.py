# def type_username():
#   conn=None
#   cursor=None
  
#   try:
#     conn= mariadb.connect(host=host,port=port,database=database,user=user, password=password)
#     cursor = conn.cursor()
#     return (conn, cursor)
#   except mariadb.OperationalError as e:
#     print('got an operational error')
#     if(("Access Denied" in e.msg)):
#       print("failed to login")
#     disconnect_db()
    
# def disconnect_db(conn,cursor):
#   if(cursor != None):
#     cursor.close()
#   if(conn != None):
#     conn.rollback()
#     conn.close()
    
# def run_query(statement,args=None):
#   try:
#     (conn, cursor) = type_username()
#     if statement.startswith("SELECT"):
#       cursor.execute(statement, args)
#       result = cursor.fetchall()
#       print("total of {} users".format(cursor.rowcount))
#       return(result)
#     else:
#       cursor.execute(statement, args)
#       if cursor.rowcount == 1:
#         conn.commit()
#         print("query successful")
#       else: 
#         print("query failed")
      
#       # conn.commit()
      
#   except mariadb.OperationalError as e:
#     print('got an operational error')
#     if(("Access Denied" in e.msg)):
#       print("failed to login")
      
        
#   except mariadb.IntegrityError as e:
#     if("CONSTRAINT `user_CHECK_username`" in e.msg):
#       print("error, all usernames should start with J")
#     elif("CONSTRAINT `user_CHECK_age`" in e.msg):
#       print("error, user is out of acceptable range")
#     elif("DUPLICATE ENTRY" in e.msg):
#       print("user already exists")
#     else:
#     # print("Integrity error")
#       print(e.msg)

#   except mariadb.ProgrammingError as e:
#     if("SQL syntax" in e.msg):
#       print("You probably have a typo")
#     else:
#       print("got a differnet programming error")
#     print(e.msg)
    
#   except RuntimeError as e:
#     print('caught a runtime error')
#     e.with_traceback
#   # always have a catch all statement at the end, and give it an alias
#   except Exception as e:
#     print(e.with_traceback)
#     print(e.msg)
    
#   finally:
#     disconnect_db(conn, cursor)