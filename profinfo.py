import datetime
class demographics:
    #Sets to check for valid factions and races. Note: add more \
    factions = ("Phoenis", "Lupus", "Longun", "Corvus", "Gelon", "Vulpine")
    races = ("Upoza", "Esnon")

    def __init__(self, faction, race, sex):
        self._faction = faction
        self._race = race
        self._sex = sex

    def __repr__(self):
        return f"demographics({self._faction}, {self._race}, {self._sex})"

    def __str__(self):
        return ("Demographics: \n"
                f"Affiliated Faction: {self._faction}\n"
                f"Race: {self._race}\n"
                f"Sex: {self._sex}\n")

    #Getter and setter method. They are unique so change() isn't used
    def faction(self, *args):
        if len(args)!=0:
            if arg[0] not in factions:
                print(f"Failed because {arg[0]} is not a faction!\n")
            else:
                self._faction = arg[0]
                print(f"Faction succesfully changed to '{self._faction}'\n")
        return self._faction

    def race(self, *args):
        if len(args)!=0:
            if arg[0] not in factions:
                print(f"Failed because {arg[0]} is not a race!\n")
            else:
                self._faction = arg[0]
                print(f"Faction succesfully changed to '{self._race}'\n")
        return self._race

    def sex(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                if args[0].lower() == 'm' or args[0].lower() == 'male':
                    sex = "Male"
                    print(f"Sex succesfully changed to 'Male'\n")
                elif args[0].lower() == 'f' or args[0].lower() == 'female':
                    sex = "Female"
                    print(f"Sex succesfully changed to 'Female'\n")
                else:
                    print("Failed because invalid input was given\n")
            else:
                print(f"Failed because {arg[0]} is not a string\n")
        return self._sex

    

class description:

    def __init__(self, height, weight, hcolor, ecolor, scolor, other):
        self._height = height
        self._weight = weight
        self._hcolor = hcolor
        self._ecolor = ecolor
        self._scolor = scolor
        self._other = other

    def __repr__(self):
        return f"Description({self._height}, {self._weight}, {self._hcolor},{self._ecolor}, {self._scolor}, {self._other})"

    def __str__(self):
        return ("Description: "
                  f"{self._height} cm, "
                  f"{self._weight} kg, "
                  f"{self._hcolor} hair, "
                  f"{self._ecolor} eyes, "
                  f"{self._scolor} skin. "
                  f"{self._other}.\n")

    #More getter setters...yay

    def hgt(self, *args):
        if len(args)!=0:
            if isinstance(args[0], (int, float)):
                self._height = args[0]
                print(f"Height succesfully changed to {self._height}kg!")
            else:
                print(f"Operation aborted because {args[0]} was not a number")
        return self._height
    def wgt(self, *args):
        if len(args)!=0:
            if isinstance(args[0], (int, float)):
                self._weight = args[0]
                print(f"Weight succesfully changed to {self._weight}kg!")
            else:
                print(f"Operation aborted because {args[0]} was not a number")
        return self._weight

    def hclr(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._hcolor = args[0]
                print(f"Hair Color succesfully changed to {self._hcolor}!")
            else:
                print(f"Operation aborted because {args[0]} was not a string")
        return self._hcolor

    def eclr(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._ecolor = args[0]
                print(f"Eye Color succesfully changed to {self._ecolor}!")
            else:
                print(f"Operation aborted because {args[0]} was not a string")
        return self._ecolor

    def sclr(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._scolor = args[0]
                print(f"Skin Color succesfully changed to {self._scolor}!")
            else:
                print(f"Operation aborted because {args[0]} was not a string")
        return self._scolor

    def other(self, *args):
        if len(args)!=0:
            if isinstance(args[0], str):
                self._other = args[0]
                print(f"Other succesfully changed to {self._other}!")
            else:
                print(f"Operation aborted because {args[0]} was not a string")
        return self._other

class mission:

    def __init__(self, operation, name, status, start, end=None, fonia=[],
                 summary="", classLevel = 1):
        self.operation = operation
        self.name = name
        self.status = status
        self.start = start
        self.end = end
        self.fonia = fonia
        self.summary = summary
        self._classLevel = 1

    def __repr__(self):
        return (f"{self.operation},{self.name},{self.status}\n"
                f"{self.start},{self.end}\n"
                f"{self.fonia}\n"
                f"{self.summary}\n"
                f"{self._classLevel}\n")

    def __str__(self):
        return (f"Operation {self.operation}\n"
                f"{self.name}\n"
                f"Status: {self.status}\n"
                f"Start: {self.start}\n"
                f"End: {self.end}\n"
                f"Fonia: {self.fonia}\n"
                f"Summary: {self.summary}\n"
                f"AuthLevel: {self._classLevel}\n")

    #Now some other functionality
    def addFonia(self, fonia):
        self._fonia.append()

    def setEnd(self, time):
        if isinstance(time, datetime.datetime):
            self._end = time
        else:
            print("Invalid input: Must be a datetime object")

class missionHistory():

    def __init__(self):
        self.missions = []

    def addmission(self, mission):
        if isinstance(mission, profinfo.mission):
            self.missions.append()
            self.sortstart()
            print("Operation success!")
        else:
            print(f"Operation aborted because {mission} was not a mission!\n")

    def sortstart(self):
        if len(self.missions)<2:
            print("There is nothing to sort")
        else:
            temp = sorted(self.missions, key=lambda mission: mission.start)
            self.missions = temp
            print("Success!")

            

