import mysql.connector
import time

'''

import tkinter as tk
root = tk.Tk()

root.geometry('500x500')
root.title('Bank')

title = tk.Label(root,text='Bank',font=('Arial', 25))
title.pack(padx=20,pady=20)

balance_button = tk.Button(root, text="Check Balance", font=('Arial',18))
balance_button.pack()

root.mainloop()

'''

programended = False

def check_balance(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
    cursor = connection.cursor()

    query = f"SELECT * FROM people"
    cursor.execute(query)
    result = cursor.fetchall()

    for people in result:
        if people[0] == name:
            print(f'Here is your balance: {people[2]}')

    cursor.close()
    connection.close()

def deposit(name):
    amount = input('How much would you like to deposit?')
    if amount.isdigit():
        connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        cursor = connection.cursor()

        query = f"SELECT * FROM people"
        cursor.execute(query)
        result = cursor.fetchall()

        for people in result:
            if people[0] == name:
                balance = people[2]

        final_bal = int(balance)+int(amount)

        query = f"UPDATE people SET balance = {final_bal} WHERE name = '{name}'"
        cursor.execute(query)
        connection.commit()

        connection.close()
        cursor.close()
    else:
        deposit(name)
    
def withdraw(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
    cursor = connection.cursor()
    amount = input('How much would you like to withdraw?')

    query = f"SELECT * FROM people"
    cursor.execute(query)
    result = cursor.fetchall()

    for people in result:
        if people[0] == name:
            balance = people[2]

    if amount.isdigit() and int(amount) <= int(balance):

        final_bal = int(balance)-int(amount)

        query = f"UPDATE people SET balance = {final_bal} WHERE name = '{name}'"
        cursor.execute(query)
        connection.commit()  
    else:
        print('This amount is more than you have in your bank.')
        withdraw(name)
    connection.close()
    cursor.close()

def delete_account(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
    cursor = connection.cursor()

    ask = input('Are you sure you want to delete your account?(y/n) ')
    if ask == 'y' or ask == 'n':
        if ask == 'y':
            drop = f"DELETE FROM people WHERE name = '{name}'"
            cursor.execute(drop)

            global programended
            programended = True
            connection.commit()
    else:
        delete_account(name)

    cursor.close()
    connection.close()

def modify_account(name):
    connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
    cursor = connection.cursor()

    ask = input('Are you sure you want to change your password?(y/n) ')
    if ask == 'y' or ask == 'n':
        if ask == 'y':
            ask_password = input('What is your current password?')
            query = f"SELECT * FROM people"
            cursor.execute(query)
            result = cursor.fetchall()

            correct = False
            for peoples in result:
                if peoples[1] == ask_password:
                    correct = True
            if correct == True:
                new_pass = input('What do you want to change your password to?')
                query = f"UPDATE people SET password = {new_pass} WHERE name = '{name}'"
                cursor.execute(query)
                connection.commit()  
            else:
                print('Your passwords do not match.')
    else:
        modify_account(name)

    cursor.close()
    connection.close() 

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

                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()

                logged = False
                for peoples in result:
                    if peoples[0] == login_user and peoples[1] == login_pass:
                        print('You have logged in')
                        logged = True

                if logged == False:
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

                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()
                exists = False
                for item in result:
                    if item[0] == login_user:
                        exists = True
                #print(result)
                if exists == True:
                    print('That username already exists')
                    login_create_account()

                login_pass = input('Create your password: ')

                #------------------------------------------------------
                query = f"INSERT INTO people (name,password,balance,type) VALUES ('{login_user}',{login_pass},0,'none')"
                cursor.execute(query)
                connection.commit()

                cursor.close()
                connection.close()
            return login_user,login_pass
    login_user,login_pass = login_create_account()

    while programended == False:
        print(listofoptions)
        ask = input('Choose an option: ')
        if True:
            if ask == '1':
                check_balance(login_user)
            elif ask == '2':
                deposit(login_user)
            elif ask == '3':
                withdraw(login_user)
            elif ask == '4':
                modify_account(login_user)
            elif ask == '5':
                delete_account(login_user)
            else:
                print('Invalid option.')
main()