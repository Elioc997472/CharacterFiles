import Profile
import Users
import profinfo
import Mission
import datetime
import myGUI
import time
import Permissions
import System
from tkinter import *
from tkinter import ttk
def main():
    #Elliott = Users.Admin("Elioc997472", "test")
    #Ivan = Users.user("FroggyMore", "12345")
    #print(Elliott, Ivan)
    #testing = Elliott.add_profile()
    #demo = profinfo.demographics("Phoenis", "Esnon", "M")
    #desc = profinfo.description(11, 11, "Black", "Brown", "Tan", "Help")
    #test = ['Chen', 'Elliott', 'Engineer', 'Cursed', '6/11/2003', demo, desc,'needs apples', 82062]
    #testing = Profile.profile(test)
    #print(testing._ID)
    #print(str(testing))
    #print(testing.last_name("Dumb"))
    
    #m = Mission.mission("Test", "System Warmup", "Ongoing", datetime.datetime(2102, 1, 16, 8, 40))
    #print(m)
    #print(repr(Elliott))
    #p = Permissions.permissions()
    #print(p)

    myGUI.start()
    print(System.current_user)
    #myGUI.teststart()
    #s = System.system()
    #s.log_in("FroggyMore","12345")
    #print(s.current_user)
    #System.new_user("lolol", "why")
main()
