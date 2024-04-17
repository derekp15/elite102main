import mysql.connector
import time
import unittest



page = ''

programended = False #to deternime if the program has ended

import tkinter as tk
root = tk.Tk()

root.geometry('500x500')
root.title('Bank')


def mainButtons(name):

    global inc #checks if something is incorrect, used later
    inc = False

    def check_balance():

        clearFrames()#clears ui

        connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        cursor = connection.cursor()

        query = f"SELECT * FROM people"
        cursor.execute(query)
        result = cursor.fetchall()

        #^^ conncect to database, I was going to make a function for each command, but this is easier for me

        for people in result:

            '''
            class testStringsMethods(unittest.TestCase):#unit testing
                def test_Status(self):
                    self.assertEqual(people[0],name)#Checks if the username matches

                if __name__ == '__main__':
                    unittest.main()
            '''
            if people[0] == name:
                balancelabel = tk.Label(root, text=f"Balance = {people[2]}", font=('Arial',18))
                balancelabel.pack()
        #^^ This finds the balance and makes it onto a label
        def back(): #The back button that sends back to the main
            clearFrames() #clears ui
            mainButtons(name)
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        root.mainloop()

        cursor.close()
        connection.close()

    def deposit():
        clearFrames()#clears frames
        def mDeposit():
            amount = entButton.get()
            #gets values from the entry
            if amount.isdigit(): #checks if it is a number
                connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
                cursor = connection.cursor()

                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()

                '''
                class testStringsMethods(unittest.TestCase):#unit testing
                    def test_Status(self):
                        self.assertEqual(people[0],name)#Checks if the username matches

                    if __name__ == '__main__':
                        unittest.main()
                '''

                for people in result:
                    if people[0] == name:
                        balance = people[2]
                #^gets balance
                final_bal = int(balance)+int(amount)
                #^Adds together balance and the amountin the entry
                query = f"UPDATE people SET balance = {final_bal} WHERE name = '{name}'"
                cursor.execute(query)
                connection.commit()
                #^commits it to balance

                clearFrames()
                mainButtons(name)

                connection.close()
                cursor.close()
            else:
                global inc
                inc = True
                #^bool for displaying incorrect label
                deposit()

        '''
            class testStringsMethods(unittest.TestCase):#unit testing
                def test_Status(self):
                    self.assertTrue(inc)#Checks if the value is equal to true

                if __name__ == '__main__':
                    unittest.main()
            '''
        if inc == True: #checks if incorrect, then prints the message for error
            incorrectLabel = tk.Label(root,text='PLEASE ENTER A NUMBER ONLY.',font=('Arial', 10))
            incorrectLabel.pack()

        entButton = tk.Entry(root, text="Back", font=('Arial',18))
        entButton.pack()
        #entry button^
        #At first i was going to ask yes or no if you wanted to deposit, and sent to different pages, but i simplifyed it
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
            amount = entButton.get()#gets entry button values

            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
            cursor = connection.cursor()

            query = f"SELECT * FROM people"
            cursor.execute(query)
            result = cursor.fetchall()

            for people in result:
                if people[0] == name:
                    balance = people[2]
                    '''
                class testStringsMethods(unittest.TestCase):#unit testing
                    def test_Status(self):
                        self.assertEqual(people[0],name)#Checks if the username matches

                    if __name__ == '__main__':
                        unittest.main()
                '''
            #^gets balance
            if amount.isdigit() and (int(balance)-int(amount))>=0: #checks if the number is less that or equal to your current balance

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
                global inc#incorrect bool
                inc = True
                withdraw()

        if inc == True:#displays error label
            incorrectLabel = tk.Label(root,text='PLEASE ENTER A NUMBER THAT IS WITHIN YOUR BALANCE.',font=('Arial', 10))
            incorrectLabel.pack()

        entButton = tk.Entry(root, text="Back", font=('Arial',18))#entry button
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

        #I was going to ask yes or no, and for the username, but i simplifyed into just the button

        def deletef():
            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')
        
            cursor = connection.cursor()
            drop = f"DELETE FROM people WHERE name = '{name}'"
            cursor.execute(drop)#deletes the row on sql
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

        #ask = input('Are you sure you want to change your password?(y/n) ') -- this was the original idea
        def change():
            if True:
                ask_password = passO.get()
                query = f"SELECT * FROM people"
                cursor.execute(query)
                result = cursor.fetchall()
                # gets original password from entry
                correct = False
                for peoples in result:
                    if peoples[1] == ask_password:
                        correct = True
                        '''
                class testStringsMethods(unittest.TestCase):#unit testing
                    def test_Status(self):
                        self.assertEqual(people[1],name)#Checks if the password matches

                    if __name__ == '__main__':
                        unittest.main()
                '''
                # checks if it matches with actual password
                new_pass = passb.get()
                #get created pass from entry
                if correct == True and (new_pass!=ask_password): #if they match and the created one isnt the same
                    query = f"UPDATE people SET password = {new_pass} WHERE name = '{name}'" #change password to new
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
        #Ui creation for modify:
        userlabel = tk.Label(root,text='Old Password: ',font=('Arial', 18))
        userlabel.pack()

        passO = tk.Entry(root, text="Enter t:", font=('Arial',18))
        passO.pack()


        passlabel = tk.Label(root,text='New Password: ',font=('Arial', 18))
        passlabel.pack()

        passb = tk.Entry(root, text="Enter:", font=('Arial',18))
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
    #main ui for the bank:
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
    for widget in root.winfo_children():#loops through widgets in the roots children and destroys them
        widget.destroy()

    #bg = tk.PhotoImage(file = "background.png").zoom(2,2)
    #label1 = tk.Label(root, image = bg)
    #label1.place(x = 0, y = 0)

    title = tk.Label(root,text='Bank',font=('Arial', 25))#recreates the title "bank"
    title.pack(padx=20,pady=20)

def begining():

    global inc #inc for incorrect bool
    inc = False 
    def login():
        
        def confirm():
            login_user = userb.get()
            login_pass = passb.get()
            #get username and password from the entry
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
            #checks if it exists, and makes logged = true
            if logged == False:
                global inc#sets bool to true if not
                inc = True
                login()

            cursor.close()
            connection.close()

        

        
        clearFrames()

        if inc == True: #incorrect message for wrong login information
            incorrectLabel = tk.Label(root,text='INCORRECT INFORMATION, PLEASE TRY AGAIN.',font=('Arial', 10))
            incorrectLabel.pack()

        #User ui below
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

        def back():#back button that clears the frames and sets to begining
            clearFrames()
            begining()
        backb = tk.Button(root, text="Back", font=('Arial',18), command=back)
        backb.pack()

        root.mainloop()


    def create():
        
        def confirm():
            login_user = userb.get()
            login_pass = passb.get()
            #gets created username and password
            connection = mysql.connector.connect(host = 'localhost', user='root', database='users', password='12488970')

            cursor = connection.cursor()

            query = f"SELECT * FROM people"
            cursor.execute(query)
            result = cursor.fetchall()
            exists = False
            for item in result: #check if the username already exists
                if item[0] == login_user:
                    exists = True
            #print(result)
            if exists == True:
                global inc #if it exists then set error bool to true and reask
                inc = True
                create()

            #------------------------------------------------------

            if exists == False: #if the username doesnt exist then creates a new row for the user in sql database
                query = f"INSERT INTO people (name,password,balance,type) VALUES ('{login_user}','{login_pass}',0,'none')"
                cursor.execute(query)
                connection.commit()

                mainButtons(login_user)

            cursor.close()
            connection.close()
        
        clearFrames()

        if inc == True: #incorrect label
            incorrectLabel = tk.Label(root,text='NAME ALREADY TAKEN, PLEASE TRY AGAIN.',font=('Arial', 10))
            incorrectLabel.pack()
        #ui below
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
    
    #ui for the begining page
    loginb = tk.Button(root, text="Login", font=('Arial',18), command=login)
    loginb.pack()

    createb = tk.Button(root, text="Sign up", font=('Arial',18), command=create)
    createb.pack()

    root.mainloop()
'''
class testStringsMethods(unittest.TestCase):#unit testing
    def test_Status(self):
        self.assertRaises(begining())#Checks the status of the function

    if __name__ == '__main__':
        unittest.main()
'''
begining() #mainloop
















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