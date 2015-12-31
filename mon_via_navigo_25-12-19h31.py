#################################################
#Institut Villebon UE 5.I4
#Projet Via Navigo
#Auteurs: Mansour Abdoulakime, Kesavan Thirusittampalam et Julie Vong 
#Date de creation: 25/12/15
#Date de derniere modification: 31/12/15 a 1h36
#################################################
import csv

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
        if self < station:
            return self
        else:
            return station


    def __hash__(self):
        """Return the station and its line"""
        return hash(self.name + self.in_line)


    def __str__(self):
        """Represent the station"""
        txt = __hash__(self)
        txt+= 'Coordinates:'.join(self.position)
        return txt



class Line:
    """Creates and represents a line of transportation
    Attribute:
        station: list of the stations which compose the line
        mode: string (RER, metro, bus or velib)
        name: string"""
    def __init__(self):
        self.station = []
        self.mode = ""
        self.name = ""
        """Change the attribute in_line of each station of the line"""
        for station in self.station:
            station.in_line = self

    def __repr__(self):
        txt = "Line",self,":"
        txt+= ','.join(station for station in self.station) 
        return txt


class PublicTransportationNetwork:
    """Represents a line of public transport. A line is oriented
    Attributes:
        stations: list of stations of a line
        node: type of transport : bus, umetro, RER, velib
        name : string, name of the line"""
        
    def __init__(self):
        self.name = ""
        self.scale = ""
        self.lines = []

    def add_a_line(self, line):
        """Add a line the the attributes lines"""
        self.lines.append(line)
        
    def save(self, file_name):
        network = open("network.csv", "wb")
        file_write = csv.writer(network, MyDialect())
        file_write.writerow(["Line","Station","Coordinates"])
        for line in self.lines:
            for station in line.station:
                file_write.writerow([line, station, station.position])
        file_write.close()
        

    def load_(self, file_name):
        file_read = open(file_name, "rb")
        reader = csv.reader(file_name)
        #for row in reader:
        #Stocker les lignes dans qch mais je ne sais pas quoi
        file.close()



    def __str__(self):
        txt = ""
        return txt
        
    class MyDialect(csv.Dialect):
        """Define a dialect with ":" as separator instead of default "," """
        # Field separator
        delimiter = ":"
        # ''chain'' separator
        quotechar = None
        # ''chaînes'' separator management
        escapechar = None
        doublequote = None
        # End of line
        lineterminator = "\r\n"
        # Systematic automatic addition of chain separator (for ''writer'')
        quoting = csv.QUOTE_NONE
        # Not ignore spaces between chaine delimitator
        # and the text
        skipinitialspace = False



