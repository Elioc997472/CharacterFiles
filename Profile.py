import profinfo
from datetime import date
class profile:
    #Setting a class set to check whether desired edit can be done easily
    profile_tags = {"lname", "fname", "mname", "role", "talent", "bio"}
    
    
    def __init__(self, args):
        """Getting the string attributes out of the way first
        The only call to this constructor is protected, and will set
        default values by itself if the field is optional"""
        self._lname = args[0]
        self._fname = args[1]
        self._role = args[2]
        self._talent = args[3]
        self._dob = args[4]
        #Assigning custom object attributes
        self._demo = args[5]
        self._desc = args[6]
        #Big long string
        self._bio = args[7]
        #self._equipment = kwargs["equipment"] Will add later once I finish class
        #Profile ID to make stuff anonymous
        self._ID = args[8]
        #New profiles will generally not have Mission History
        self._history = None
        #Has a User claimed the profile?
        self.claimed = False
        self._authLevel = 1 #Only Admin can change authLevel of a profile they can see
        #Create the .txt file. Shuffle ID if file already exists
        while True:
            try:
                f = open(f"{self.ID()}.txt", "x")
                f.write(repr(self))
                f.close()
                break
            except: #If filename with ID already exists, change the ID
                self.ID(True)
                
    #Different __repr() to write to files.
    def __repr__(self):
        return (f"{self.last_name()},{self.first_name()}\n"
                f"{self.role()},{self.talent()}\n"
                f"{self.dob()}\n"
                f"{self.demo()}"#No newline. str includes newline
                f"{self.desc()}"#Look at above
                f"{self.bio()}\n"
                f"{self.ID()}\n"
                f"{self.history()}\n"
                f"{self.claimed}\n")
    #Separate __str__() to display to user.
    def __str__(self):
        return (f"Name: {self.first_name()} {self.last_name()}\tClaimed: {self.claimed}\n"
                f"Role: {self.role()}\tTalent: {self.talent()}\n"
                f"DOB: {self.dob()}\tSex: {self.demo().sex()}\n"
                f"Race: {self.demo().race()}\tFaction: {self.demo().faction()}\n"
                f"Desc: {self.desc().hgt()}cm,{self.desc().wgt()}kg,"
                f"{self.desc().hclr()} hair,{self.desc().eclr()} eyes,"
                f"{self.desc().sclr()} skin.\n"
                f"Bio: {self.bio()}\n"
                )

    #Getter Setter
    def last_name(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._lname = args[0]
                print(f"Last name succesfully changed to {self._lname}!")
            else:
                print(f"Operation aborted because {args[0]} was not a str")
        return self._lname

    def first_name(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._fname = args[0]
                print(f"First name succesfully changed to '{self._fname}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a string \n")
        return self._fname
    
    def dob(self): #Getter only. Who changes their DOB?
        return self._dob

    def role(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._role = args[0]
                print(f"Role succesfully changed to '{self._role}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a string \n")
        return self._role

    def talent(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._role = args[0]
                print(f"Talent succesfully changed to '{self._talent}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a string \n")
        return self._talent

    def demo(self, *args):
        if len(args)!=0:
            if isinstance(args[0], profinfo.demo):
                self._demo = args[0]
                print(f"Demographics succesfully changed to '{self._demo}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a demographic\n")
        return self._demo

    def desc(self, *args):
        if len(args)!=0:
            if isinstance(args[0], profinfo.description):
                self._description = args[0]
                print(f"Description succesfully changed to '{self._description}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a description\n")
        return self._desc

    def bio(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._bio = args[0]
                print(f"Bio succesfully changed to '{self._bio}'\n")
            else:
                print(f"Operation aborted because {args[0]} was not a string \n")
        return self._bio

    def history(self, *args):
        """Accesses the missionHistory object associated with each profile. Sorts missions by date
        and adds it to missionHistory"""
        if len(args)!=0:
            try:
                args.sort()
                for m in args:
                    if isinstance(m, profinfo.mission):
                        self._history.addmission(m)
                    else:
                        print("A mission failed to add because it was not a mission!")
                self._history.sortstart()
            except:
                print("Input was invalid!")
        return self._history

    def ID(self, *args):
        """If changeID is true, shuffle profile ID. Returns ID"""
        if len(args)!=0:
            newHash = self.first_name()+self.last_name()+self.role()
            self._ID = str(abs(hash(newHash)))[:5]
        return self._ID


    
