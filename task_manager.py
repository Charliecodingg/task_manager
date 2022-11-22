#=====importing libraries===========
from datetime import datetime

#this is imported to allow the program to find the current date.
#====Login Section====
usernames = list()
passwords = list()
#Empty lists are created to be appended to later and login defaults to false so the loop begins
login = False
#the login process repeats until the user logs in correctly
while login == False:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    usernamefile = open('user.txt', 'r+')
#the file is then looped through to check if the entered values are correct.
    for line in usernamefile:
        #data from the file is converted into a list to be checked.
        currentline = line
        currentline = currentline.replace("\n","")
        currentline = currentline.split(", ")
        #by adding the names that have been checked to a new list
        #an error message can be displayed at the end of checking rather than on every line
        usernames.append(currentline[0])
        passwords.append(currentline[1])
        if currentline[0] == username_input:
            if currentline[1] == password_input:
                print("Login Successful ")
                login = True
                currentuser = username_input
                #this is used to check if the user is an admin      
    if not username_input in usernames:
        print("Username not found, Please enter a valid username ")
    if username_input in usernames and not password_input in passwords:
        print("Password incorrect, Please enter the correct password ")
usernamefile.close()
#the file is then closed as it will be opened in a different way when needed.
while login == True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    # different options are visible to admin and normal users
    if currentuser == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - display statistics
e - Exit
''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
''').lower()

    #registers a new user and writes the entered data to the user.txt file
    #the register user function is only avaliable to the administrator.
    if menu == 'r': 
        new_username = input("Please enter the username to be registered: ")
        user_registered = False
        #this loop repeats the password input procedure until both passwords match
        while user_registered != True:
            new_user_password = input("Please enter the new user's password: ")
            password_confirmation = input("Please confirm entered password: ")
            if new_user_password == password_confirmation:
                user_registered = True
            else:
                print("The entered passwords do not match ")
            #the user file is opened in append mode as we are only adding information at the end        
            usernamefile = open('user.txt', 'a')
            usernamefile.write(' \n')
            usernamefile.write(f"{new_username}, {new_user_password}")
            usernamefile.close()

    #Creates a new task from entered data and writes it to the tasks.txt file
    elif menu == 'a':
        currentdate = datetime.now()
        taskfile = open('tasks.txt', 'a')
        taskfile.write("\n")
        taskfile.write(input("Please enter the user to whom the task is assigned: ") + (", "))
        taskfile.write(input("Please enter the title of the task:" ) + (", "))
        taskfile.write(input("Please enter the description of the task: ") + (", "))
        #to write the date in the desired format the month will be converted to the shortened str
        month_num = currentdate.month
        #this takes the month number from the current date and %m to return the current month
        month_datetime = datetime.strptime(str(month_num), "%m")
        #%b format returns the short name of the month taken form the current time
        month_name = month_datetime.strftime("%b")
        taskfile.write(f"{currentdate.day} {month_name} {currentdate.year}, ")
        taskfile.write(input("Please enter the due date of this task: ") + (", "))
        taskfile.write("No \n") #marks the task as incomplete by default
        taskfile.close()
        #the file is opened in append mode as we are only adding data to the end of the file.

    #displays all tasks in the tasks.txt file in a user friendly manner
    elif menu == 'va':
        taskfile = open('tasks.txt', 'r')
        
        for line in taskfile:
            #checks if the line is empty
            if line != "\n":
                #prints the data for each task in the desired format
                print("____________________________\n")
                currentline = line
                currentline = currentline.replace("\n", "")
                currentline = currentline.split(", ")
                print(f"Task: \t\t {currentline[1]} ")
                print(f"Assigned to:     {currentline[0]} ")
                print(f"Date assigned:   {currentline[3]} ")
                print(f"Due Date: \t {currentline[4]} ")
                print(f"Task Complete?   {currentline[5]} ")
                print(f"Task Description: \n {currentline[2]}")
        print("\n ____________________________\n")
        taskfile.close()
        #adds a gap after the tasks have displayed to improve clarity for the user

    #displays all tasks for the current user, or prints a message if they have none.
    elif menu == 'vm':
        taskfile = open('tasks.txt', 'r')
        mytask = False
        #this boolean statement is only set to true if the user has a task in the file
        for line in taskfile:
            #checks if the line is empty
            if line != "\n":
                #prints the data for each task in the desired format
                
                currentline = line
                currentline = currentline.replace("\n", "")
                currentline = currentline.split(", ")
                if currentline[0] == currentuser:
                    print("____________________________\n")
                    print(f"Task: \t\t {currentline[1]} ")
                    print(f"Assigned to:     {currentline[0]} ")
                    print(f"Date assigned:   {currentline[3]} ")
                    print(f"Due Date: \t {currentline[4]} ")
                    print(f"Task Complete?   {currentline[5]} ")
                    print(f"Task Description: \n {currentline[2]}")
                    mytask = True
        if mytask == False:
            print("\nYou do not have any tasks assigned to you\n")
        else:
            print("\n ____________________________\n")
        taskfile.close()

    #displays statistics for the admin including total tasks and total users
    elif menu == 's':
        number_of_tasks = 0
        number_of_users = 0
        taskfile = open("tasks.txt","r")
        usernamefile = open("user.txt","r")
        #loops through each file, adding one to the count for each non empty line
        for line in taskfile:
            if line != "\n":
                number_of_tasks += 1
        for line in usernamefile:
            if line != "\n":
                number_of_users += 1
        print("__________________________\n")
        print(f"Current user count: {number_of_users} ")
        print(f"Current task count: {number_of_tasks} ")
        print("__________________________\n")
        taskfile.close()
        usernamefile.close()

    #exits the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")