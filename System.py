import Users
import Profile
import Mission
import Permissions
from tkinter import *
from tkinter import ttk

#Creating a universal dictionary
global profile_list
profile_list = []
global profileID
profileID = {}

current_user = None
user_list = set()
f = open("user_data.txt")
for line in f.readlines():
    if line == "\n":
        continue
    else:
        user_list.add(line[0:line.index(",")])
f.close()

def verify(target):
    """Checks if the System.current_user has access to target"""
    if current_user.auth()>=target.authLevel():
        return True
    else:
        return False

def log_in(username, password):
    """Takes a username and a password. Reads user_data.txt and chacks
    for user registration and permissions, creates a user object, and sets
    System.current_user to generated user"""
    global current_user
    global user_list
    if username in user_list:
        f = open("user_data.txt")
        for line in f.readlines():
            args = line.split(",")
            if password == args[1]:
                perms = (Permissions.permissions(args[2],
                        args[3], args[4], args[5]))
                if args[6] == "<class 'Users.Admin'>":
                    current_user = Users.Admin(args[0], args[1], perms)
                else:
                    current_user = Users.user(args[0], args[1], perms)
                print("Yay")
                print(current_user)
                break
    else:
        print("Failed. Incorrect username or password")
            
def new_user(user, pwd):
    """Creates a new user object, stores username and password in
    user_data.txt, and sets current_user to user. Returns False if
    username is taken"""
    global current_user
    global user_list
    print(str(user in user_list))
    if user in user_list:
        print("Username taken!")
        return False
    else:
        f = open("user_data.txt", 'a')
        current_user = Users.user(user, pwd)
        f.write(repr(current_user))
        f.close()
        print(user, pwd)
        return True
    
        
            
