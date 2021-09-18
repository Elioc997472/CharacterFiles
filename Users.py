import Permissions
import Profile
import profinfo
import datetime
import System
class user:
    #This is just a parent class
    def __init__(self, username, password, permissions = Permissions.permissions()):
        self.username = username
        self.password = password
        self.permissions = permissions
    #Set profile-Implement in a different class maybe?
    """def set_profile(self, profile):
        #I use try: and except: just in case specified profile doesn't exist
        try:
            if profile.claimed:
                print("Operation aborted. Profile already claimed, \n")
            else:
                self.profile = profile
                profile.claimed = True
                print("Claim profile was succesful!\n")
        except:
            print("Either the profile doesn't exist or the test dun goofed\n")
    """
    def __repr__(self):#For file writing
        return (f"{self.username},{self.password},{self.permissions},{type(self)}\n")

    def auth(self):
        return self.permissions.viewUser()

class Admin(user):
    #Privilege to add profiles, view permissions, and change user values
    
    def add_profile(self):
        """Gives a series of prompts which returns a Profile object and generates
        a file storing all the values of Profile"""
        #Array to store arguments
        user_args = []
        #Now let's go through every object value...
            
        #Last Name
        while True:
            lname = input("Last Name: ")
            if isinstance(lname, str):
                break
            else:
                print("Please input a string!")
        user_args.append(lname)
            
        #First Name
        while True:
            fname = input("First Name: ")
            if isinstance(fname, str):
                break
            else:
                print("Please input a string!")
        user_args.append(fname)
        
        #Role
        while True:
            role = input("User Role: ")
            if isinstance(role, str):
                break
            else:
                print("Please input a string!")
        user_args.append(role)
        
        #Talent
        while True:
            talent = input("User Talent: ")
            if isinstance(talent, str):
                break
            else:
                print("Please input a string!")
        user_args.append(talent)
        
        #DOB
        while True:
            try:
                month = int(input("Birth Month: "))
                day = int(input("Birth Day: "))
                year = int(input("Birth Year: "))
                dob = datetime.date(year, month, day)
                break
            except ValueError:
                print("Please enter in a valid date.")
            #except:
            #print("Enter in dates as integers")
        user_args.append(dob)

        #Demographics
        while True:
            faction = input("Enter affiliated faction: ")
            if faction not in profinfo.demographics.factions:
                print("Please enter a valid faction!")
            else:
                break
        while True:
            race = input("Enter race: ")
            if race not in profinfo.demographics.races:
                print("Please enter a valid race!")
            else:
                break
        while True:
            sex = input("Enter sex: ")
            if isinstance(sex, str):
                if sex.lower() == 'm' or sex.lower() == 'male':
                    sex = "Male"
                    break
                elif sex.lower() == 'f' or sex.lower() == 'female':
                    sex = "Female"
                    break
                else:
                    print("Please enter either male or female!")
            else:
                print("Please enter a string!")
        demographics = profinfo.demographics(faction, race, sex)
        user_args.append(demographics)
                
        #Description
        while True:
            height = int(input("Height (cm): "))
            if isinstance(height, (float, int)):
                break
            else:
                print("Please enter in  a number!")
        while True:
            weight = int(input("Weight (kg): "))
            if isinstance(weight, (float, int)):
                break
            else:
                print("Please enter in  a number!")
        while True:
            hcolor = input("Hair Color: ")
            if isinstance(hcolor, str):
                break
            else:
                print("Please enter in a string!")
        while True:
            ecolor = input("Eye Color: ")
            if isinstance(ecolor, str):
                break
            else:
                print("Please enter in a string!")
        while True:
            scolor = input("Skin Color: ")
            if isinstance(scolor, str):
                break
            else:
                print("Please enter in a string!")
        other = input("Other Details: ")
        desc = profinfo.description(height, weight, hcolor,
                                       ecolor, scolor, other)
        user_args.append(desc)

        #Bio (Should be optional) Figure out way to get bio to be multlinear
        while True:
            bio = input("Insert a brief biography: ")
            if bio == '':
                bio = "None given"
                break
            elif isinstance(bio, str):
                break
            else:
                print("Please enter a string or leave field empty\n")
        user_args.append(bio)

        #ID
        name = lname+fname
        ID = str(abs(hash(name)))[:5]
        user_args.append(ID)
        profile_list.append(name)
        profileID[name] = str(ID)
        return Profile.profile(user_args)
        
