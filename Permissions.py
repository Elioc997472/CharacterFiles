class permissions:

    def __init__(self, missionHistory = 0,  getEquipment = False,
                 viewUser = 0, requestUser = False):
        self._missionHistory = missionHistory #Can user see mission history?
        self._getEquipment = getEquipment #Can user see equipment?
        self._viewUser = viewUser #What level can user see profiles?s?
        self._requestUser = requestUser #Can user request profile?

    def __repr__(self):
        return f"{self._missionHistory},{self._getEquipment},{self._viewUser},{self._requestUser}"
    """Now a whole list of annoying getter and mutator methods...
    For every method below, if user inputs argument, change value and return value
    else just return the value
    """
    def missionHistory(self, n = None):
        if isinstance(n, int):
            self._missionHistory = n
        return self._missionHistory

    def getEquipment(self, n = None):
        if isinstance(n, bool):
            self._getEquipment = n
        return self._getEquipment

    def viewUser(self, n = None):
        if isinstance(n, int):
            self._viewUser = n
        return self._viewUser
    
    def requestUser(self, n = None):
        if isinstance(n, bool):
            self._requestUser = n
        return self._requestUser

        
