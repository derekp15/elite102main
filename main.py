import mysql.connector
import time

programended = False

def check_balance(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')

    cursor = connection.cursor()

    show_tables_query = f"SHOW TABLES"
    cursor.execute(show_tables_query)
    list_of_tables = cursor.fetchall()

    for item in list_of_tables:
        getPassQ = f"SHOW COLUMNS FROM {item[0]}"
        cursor.execute(getPassQ)
        passq = cursor.fetchall()[2][4]
        if item[0] == name:
            print(f'Here is your balance: {passq}')

    cursor.close()
    connection.close()

def deposit(name):
    pass
    
def withdraw(name):
    pass

def delete_account(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
    cursor = connection.cursor()

    ask = input('Are you sure you want to delete your account?(y/n) ')
    if ask == 'y' or ask == 'n':
        if ask == 'y':
            drop = f"DROP TABLE {name};"
            cursor.execute(drop)

            global programended
            programended = True
            connection.commit()
    else:
        delete_account(name)

    cursor.close()
    connection.close()

def modify_account(name, password):
    pass 

def main():
    listof = [
        '1. Login',
        '2. Create account',
    ]
    listofoptions = [
        '1. Balance',
        '2. Deposit',
        '3. Withdraw',
        '4. Modify Account',
        '5. Delete Account',
    ]
    print(listof)
    ask = input('Choose an option: ')
    def login_create_account():
        if ask == '1' or ask == '2':
            if ask == '1':
                login_user = input('Enter your username: ')
                login_pass = input('Enter your password: ')

                #loop through tables and check if username is there, if it is then check if password matches username
                connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')

                cursor = connection.cursor()

                show_tables_query = f"SHOW TABLES"
                cursor.execute(show_tables_query)
                list_of_tables = cursor.fetchall()

                can = False
                for item in list_of_tables:
                    #print(item[0])

                    getPassQ = f"SHOW COLUMNS FROM {item[0]}"
                    cursor.execute(getPassQ)
                    passq = cursor.fetchall()[1][4]

                    #print(passq)
                    if item[0] == login_user and str(passq) == login_pass:
                        can = True
                    else:
                        pass

                if can == True:
                    print('You have logged in')
                else:
                    print('Incorrect information, please try again')
                    login_create_account()

                cursor.close()
                connection.close()


                #if not then use : continue
            else:
                login_user = input('Create a username: ')
                #check if username is there, if it is then reask
                #if not then use : continue

                connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')

                cursor = connection.cursor()

                show_tables_query = f"SHOW TABLES"
                cursor.execute(show_tables_query)
                list_of_tables = cursor.fetchall()

                exists = False
                for item in list_of_tables:
                    if item[0] == login_user:
                        exists = True
                if exists == False:
                    pass
                else:
                    print('That username already exists')
                    login_create_account()

                login_pass = input('Create your password: ')

                #------------------------------------------------------
                create_table_query = f"""
                    CREATE TABLE {login_user}(
                        type char(255) DEFAULT 'none',
                        password char(255) DEFAULT {login_pass},
                        balance int DEFAULT 0
                    )
                """
                cursor.execute(create_table_query)
                #list_of_tables = cursor.fetchall()
                connection.commit()

                #print(login_user) DOESNT WORK___DOESN WORK SDOENSE WORK
                #addData = f"INSERT INTO {login_user} (type, password, balance) VALUES ('none',{login_pass},0)"
                #cursor.execute(addData)
                #list_of_tables = cursor.fetchall()
                #connection.commit()

                getPassQ = f"SHOW COLUMNS FROM {login_user}"
                cursor.execute(getPassQ)
                passq = cursor.fetchall()
                #print(passq)
                
                #-----------------------------------------------------------
                #make a new table that has the users name, and password, etc..
                #if not then use : continue
                cursor.close()
                connection.close()
            return login_user,login_pass
    login_user,login_pass = login_create_account()

    while programended == False:
        print(listofoptions)
        ask = int(input('Choose an option: '))
        if ask >= 1 and ask <= 5:
            if ask == 1:
                check_balance(login_user)
            elif ask == 2:
                deposit(login_user)
            elif ask == 3:
                withdraw(login_user)
            elif ask == 4:
                modify_account(login_user,login_pass)
            elif ask == 5:
                delete_account(login_user)
main()