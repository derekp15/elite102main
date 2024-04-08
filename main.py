import mysql.connector

connection = mysql.connector.connect(user='root', database='users', password='12488970')

cursor = connection.cursor()

testQuery = ("SELECT * FROM guy")

cursor.execute(testQuery)
data = cursor.fetchall()

for item in data:
    print(item)

cursor.close()
connection.close()



def check_balance(name):
    pass

    #print(val)
check_balance('guy')

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