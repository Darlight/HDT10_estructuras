
from neo4j import GraphDatabase

class DBHospital(object):

    def __init__(self, uri, user, password):
        #Uses the database with the username called ne04j, the database link and the password
        #Password is 12345.
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        #Creates the nodes of the patient, doctor and the drug required.
        self.doctor = self._driver.lavels.create("Doctor")
        self.patient = self._driver.lavels.create("Patient")
        self.drug = self._driver.lavels.create("Drug")

    def close(self):
        #Just closes the driver
        self._driver.close()
        return "Hello there!"

    def add_Patient(self,name,tel):
        #Creating a Patient node with its atributes
        self.patient.add(self._driver.nodes.create(name= name, telephone = tel))
        return "Done"

    def add_Doctor(self,name,tel,spec,colegiado):
        # Creating a Doctor node with its atributes
        self.doctor.add(self._driver.nodes.create(name=name, telephone=tel, scholarship = colegiado, specialty = spec))
        return "Done"
    def asign_Drug(self,name,date1,date2,dose):
        # Creating a Doctor node with its atributes
        self.drug.add(self._driver.nodes.create(name=name, dateassigned=date1, untildate=date2, dose=dose))
        return "Done"
    def find_Doctorswithspec(self):
        return "missing"
    def add_PatientConnection(self):
        return "hello there"
    def apoint_Session(self):
        return "Hi there"
    def recommend_Doctor(self):
        return "Assassin"
