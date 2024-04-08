import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'main', password = '12488970')

cursor = connection.cursor()
testQuery = (“SELECT * FROM users”)
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()

def check_balance():
    pass

def deposit():
    pass
    
def withdraw():
    pass 

def create_account():
    pass

def delete_account():
    pass

def modify_account():
    pass       