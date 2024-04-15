import mysql.connector
import time

page = ''

programended = False

import tkinter as tk
root = tk.Tk()

root.geometry('500x500')
root.title('Bank')


def mainButtons(name):

    global inc
    inc = False

    def check_balance():

        clearFrames()

        connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        cursor = connection.cursor()

        query = f"SELECT * FROM people"
        cursor.execute(query)
        result = cursor.fetchall()

        for people in result:
            if people[0] == name:
                balancelabel = tk.Label(root, text=f"Balance = {people[2]}", font=('Arial',18))
                balancelabel.pack()
                
        def back():
            clearFrames()
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        root.mainloop()

        cursor.close()
        connection.close()

    def deposit():
        clearFrames()
        def mDeposit():
            amount = entButton.get()
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

                clearFrames()
                mainButtons(name)

                connection.close()
                cursor.close()
            else:
                global inc
                inc = True
                deposit()

        if inc == True:
            incorrectLabel = tk.Label(root,text='PLEASE ENTER A NUMBER ONLY.',font=('Arial', 10))
            incorrectLabel.pack()

        entButton = tk.Entry(root, text="Back", font=('Arial',18))
        entButton.pack()

        depButton = tk.Button(root, text="Deposit", font=('Arial',18), command=mDeposit)
        depButton.pack()
        def back():
            clearFrames()
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()
        root.mainloop()
    def withdraw():
        clearFrames()
        def mWithdraw():
            amount = entButton.get()

            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
            cursor = connection.cursor()

            query = f"SELECT * FROM people"
            cursor.execute(query)
            result = cursor.fetchall()

            for people in result:
                if people[0] == name:
                    balance = people[2]

            if amount.isdigit() and (int(balance)-int(amount))>=0:

                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()

                final_bal = int(balance)-int(amount)

                query = f"UPDATE people SET balance = {final_bal} WHERE name = '{name}'"
                cursor.execute(query)
                connection.commit()

                clearFrames()
                mainButtons(name)

                connection.close()
                cursor.close()
            else:
                global inc
                inc = True
                withdraw()

        if inc == True:
            incorrectLabel = tk.Label(root,text='PLEASE ENTER A NUMBER THAT IS WITHIN YOUR BALANCE.',font=('Arial', 10))
            incorrectLabel.pack()

        entButton = tk.Entry(root, text="Back", font=('Arial',18))
        entButton.pack()

        depButton = tk.Button(root, text="Withdraw", font=('Arial',18), command=mWithdraw)
        depButton.pack()
        def back():
            clearFrames()
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()
        root.mainloop()

    def delete_account():
        clearFrames()

        

        def deletef():
            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        
            cursor = connection.cursor()
            drop = f"DELETE FROM people WHERE name = '{name}'"
            cursor.execute(drop)
            connection.commit()

            connection.close()
            cursor.close()
            clearFrames()
            begining()
            
        delb = tk.Button(root, text="Delete account", font=('Arial',18), command=deletef)
        delb.pack()
        def back():
            clearFrames()
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        
        

    def modify_account():
        connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        cursor = connection.cursor()
        clearFrames()

        #ask = input('Are you sure you want to change your password?(y/n) ')
        def change():
            if True:
                ask_password = passO.get()
                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()

                correct = False
                for peoples in result:
                    if peoples[1] == ask_password:
                        correct = True
                new_pass = passb.get()
                if correct == True and (new_pass!=ask_password):
                    query = f"UPDATE people SET password = {new_pass} WHERE name = '{name}'"
                    cursor.execute(query)
                    connection.commit()  

                    clearFrames()
                    mainButtons(name)
                else:
                    global inc
                    inc = True
                    modify_account()
        #else:
            #modify_account()

        if inc == True:
            incorrectLabel = tk.Label(root,text='YOUR CREATED PASSWORD MUST BE DIFFERENT, OR CHECK YOUR OLD PASSWORD.',font=('Arial', 8))
            incorrectLabel.pack()

        userlabel = tk.Label(root,text='Old Password: ',font=('Arial', 18))
        userlabel.pack()

        passO = tk.Entry(root, text="Enter username:", font=('Arial',18))
        passO.pack()


        passlabel = tk.Label(root,text='New Password: ',font=('Arial', 18))
        passlabel.pack()

        passb = tk.Entry(root, text="Enter password:", font=('Arial',18))
        passb.pack()


        confirmb = tk.Button(root, text="Change password", font=('Arial',18), command=change)
        confirmb.pack()



        def back():
            clearFrames()
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()
        root.mainloop()

        cursor.close()
        connection.close() 





    
    clearFrames()

    balance_button = tk.Button(root, text="Check Balance", font=('Arial',18), command=check_balance)
    balance_button.pack()

    deposit_button = tk.Button(root, text="Deposit", font=('Arial',18), command=deposit)
    deposit_button.pack()

    withdraw_button = tk.Button(root, text="Withdraw", font=('Arial',18), command=withdraw)
    withdraw_button.pack()

    delete_button = tk.Button(root, text="Delete", font=('Arial',18), command=delete_account)
    delete_button.pack()

    modify_button = tk.Button(root, text="Modify", font=('Arial',18), command=modify_account)
    modify_button.pack()

    root.mainloop()



def clearFrames():
    for widget in root.winfo_children():
        widget.destroy()

    #bg = tk.PhotoImage(file = "background.png").zoom(2,2)
    #label1 = tk.Label(root, image = bg)
    #label1.place(x = 0, y = 0)

    title = tk.Label(root,text='Bank',font=('Arial', 25))
    title.pack(padx=20,pady=20)

def begining():

    global inc
    inc = False 
    def login():
        
        def confirm():
            login_user = userb.get()
            login_pass = passb.get()

            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
            cursor = connection.cursor()

            query = f"SELECT * FROM people"
            cursor.execute(query)
            result = cursor.fetchall()

            logged = False
            for peoples in result:
                if peoples[0] == login_user and peoples[1] == login_pass:
                    mainButtons(login_user)
                    logged = True

            if logged == False:
                global inc
                inc = True
                login()

            cursor.close()
            connection.close()

        

        
        clearFrames()

        if inc == True:
            incorrectLabel = tk.Label(root,text='INCORRECT INFORMATION, PLEASE TRY AGAIN.',font=('Arial', 10))
            incorrectLabel.pack()

        userlabel = tk.Label(root,text='Username: ',font=('Arial', 18))
        userlabel.pack()

        userb = tk.Entry(root, text="Enter username:", font=('Arial',18))
        userb.pack()


        passlabel = tk.Label(root,text='Password: ',font=('Arial', 18))
        passlabel.pack()

        passb = tk.Entry(root, text="Enter password:", font=('Arial',18))
        passb.pack()


        confirmb = tk.Button(root, text="Login", font=('Arial',18), command=confirm)
        confirmb.pack()

        def back():
            clearFrames()
            begining()
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        root.mainloop()


    def create():
        
        def confirm():
            login_user = userb.get()
            login_pass = passb.get()

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
                global inc
                inc = True
                create()

            #------------------------------------------------------

            if exists == False:
                query = f"INSERT INTO people (name,password,balance,type) VALUES ('{login_user}','{login_pass}',0,'none')"
                cursor.execute(query)
                connection.commit()

                mainButtons(login_user)

            cursor.close()
            connection.close()
        
        clearFrames()

        if inc == True:
            incorrectLabel = tk.Label(root,text='NAME ALREADY TAKEN, PLEASE TRY AGAIN.',font=('Arial', 10))
            incorrectLabel.pack()

        userlabel = tk.Label(root,text='Create username: ',font=('Arial', 18))
        userlabel.pack()

        userb = tk.Entry(root, text="Enter username:", font=('Arial',18))
        userb.pack()


        passlabel = tk.Label(root,text='Create password: ',font=('Arial', 18))
        passlabel.pack()

        passb = tk.Entry(root, text="Enter password:", font=('Arial',18))
        passb.pack()


        confirmb = tk.Button(root, text="Create Account", font=('Arial',18), command=confirm)
        confirmb.pack()

        def back():
            clearFrames()
            begining()
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        root.mainloop()

    clearFrames()
    
    loginb = tk.Button(root, text="Login", font=('Arial',18), command=login)
    loginb.pack()

    createb = tk.Button(root, text="Sign up", font=('Arial',18), command=create)
    createb.pack()

    root.mainloop()

begining()
















'''
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
'''