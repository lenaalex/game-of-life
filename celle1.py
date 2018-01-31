"""
Klassen beskriver en celle i simulering. En celle skal ha en variabel som beskriver
status (levende/død).
"""
#lager klassen Celle
class Celle:
# i konstruktør definerer initialvariabel status lik død
    def __init__(self):
        self._status="doed"
# definerer metode som setter cellen til død
    def settDoed(self):
        self._status="doed"
# definerer en metode som setter cellen til levende
    def settLevende(self):
        self._status="levende"
# definerer metode erLevende
    def erLevende(self):
# hvis status lik levende, så returnere true, else blir false
        if self._status == "levende":
            return True
        else:
            return False
# definerer metode tegnerepresentasjon
    def tegnerepresentasjon(self):
            if  self._status == "levende":
# hvis status lik levende returnerer "o" men alle andre tilfeller ". "
                return "O"
            else:
                return "."
