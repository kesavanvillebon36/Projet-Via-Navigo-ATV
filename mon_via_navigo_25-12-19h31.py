#################################################
#Institut Villebon UE 5.I4
#Projet Via Navigo
#Auteurs: Mansour Abdoulakime, Kesavan Thirusittampalam et Julie Vong 
#Date de creation: 25/12/15
#Date de derniere modification: 25/12/15 a 19h31
#################################################


class Station:
    """
    Class which will represent every station, contains differents methods to
    Attributes:
    name: string
    position: couple of float for the coordinates on the map
    in_line: belonging to a line

    """

    def __init__(self,line = ""):
        self.name = ""
        self.position = (float, float)
        self.in_line = line


    def __eq__(self, station):
        """Decides if 2 stations are equal"""
        bool = 0
        if self.name == station.name:
            return True


    def __lt__(self, station):
        """Decide which station is the smallest in terms of alphabetic order of the name, then of the line if it is the same station"""
        pass


    def __hash__(self):
        """Return the station and its line"""
        return hash(self.name + self.in_line)


    def __str__(self):
        """Represent the station"""
        txt = ""
        return txt




class Line:
    def __init__(self):
        self.station = []
        self.mode = ""
        self.name = ""

    def __repr__(self):
        return str


class PublicTransportationNetwork:
    def __init__(self):
        self.name = ""
        self.scale = ""
        self.lines = []

    def save(self, file_name):
        pass

    def load_(self, file_name):
        pass



    def __str__(self):
        txt = ""
        return txt



