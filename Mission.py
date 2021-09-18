import datetime
class mission:

    def __init__(self, operation, name, status, officer, start, end=None, fonia=[],
                 summary="", classLevel = 1):
        self._operation = operation
        self._name = name
        self._status = status
        self._start = start
        self._end = end
        self._officer = officer
        self._fonia = fonia
        self._summary = summary
        self._classLevel = 1

    def __repr__(self):
        return (f"{self._operation},{self._name},{self._status}\n"
                f"{self._start},{self._end}\n"
                f"{self._fonia}\n"
                f"{self._summary}\n"
                f"{self._classLevel}\n")

    def __str__(self):
        return (f"Operation {self._operation}\n"
                f"{self._name}\n"
                f"Status: {self._status}\n"
                f"Start: {self._start}\n"
                f"End: {self._end}\n"
                f"Officer: {self._officer}\n"
                f"Fonia: {self._fonia}\n"
                f"Summary: {self._summary}\n"
                f"AuthLevel: {self._classLevel}\n")

    #Now some other functionality
    def addFonia(self, fonia):
        self._fonia.append()
        
