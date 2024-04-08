import mysql.connector

def check_balance():
    pass

def deposit():
    pass
    
def withdraw():
    pass

def delete_account():
    pass

def modify_account():
    pass 

def main():
    login_user = ''
    login_pass = ''
    listof = [
        '1. Login',
        '2. Create account',
    ]
    print(int(5.7))
    listofoptions = [
        '1. Balance',
        '2. Deposit',
        '3. Withdraw',
        '4. Modify Account',
        '5. Delete Account',
    ]
    print(listof)
    ask = input('Choose an option: ')
    while True:
        if ask == '1' or ask == '2':
            if ask == '1':
                login_user = input('Enter your username: ')
                login_pass = input('Enter your password: ')

                #loop through tables and check if username is there, if it is then check if password matches username
                connection = mysql.connector.connect(user='root', database='users', password='12488970')

                cursor = connection.cursor()

                testQuery = f"SHOW TABLES"
                cursor.execute(testQuery)
                list_of_tables = cursor.fetchall()

                for item in list_of_tables:
                    getPassQ = f"SELECT password FROM {item[0]}"
                    cursor.execute(getPassQ)
                    passcode = cursor.fetchall()
                    print(passcode)
                    if item[0] == login_user and passcode == login_pass:
                        print('same')

                cursor.close()
                connection.close()


                #if not then use : continue
                break
            else:
                login_user = input('Create a username: ')
                #check if username is there, if it is then reask
                #if not then use : continue

                login_pass = input('Create your password: ')
                #make a new table that has the users name, and password, etc..
                #if not then use : continue
                break
    
    while True:
        print(listofoptions)
        ask = int(input('Choose an option: '))
        if ask >= 1 and ask <= 5:
            if ask == 1:
                check_balance()
            elif ask == 2:
                deposit()
            elif ask == 3:
                withdraw()
            elif ask == 4:
                modify_account()
            elif ask == 5:
                delete_account()
main()