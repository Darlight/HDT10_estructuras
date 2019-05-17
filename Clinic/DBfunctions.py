
from neo4j import GraphDatabase
from neo4jrestclient import client

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

    def add_Patient(self,name,tel):
        #Creating a Patient node with its atributes
        self.patient.add(self._driver.nodes.create(name= name, telephone = tel))
        return "Done"

    def add_Doctor(self,name,tel,spec,colegiado):
        # Creating a Doctor node with its atributes
        self.doctor.add(self._driver.nodes.create(name=name, telephone=tel, scholarship = colegiado, specialty = spec))
        return "Done"

    def add_Drug(self,name,date1,date2,dose):
        # Creating a Drug node with its atributes
        self.drug.add(self._driver.nodes.create(name=name, dateassigned=date1, untildate=date2, dose=dose))
        return "Done"

    #Creates a list of doctors with the given specialty
    def find_DoctorsWithSpec(self,spec):
        doctors = []
        q = "MATCH (d:Doctor) WHERE d.specialty = \"{0}\" RETURN d".format(spec)
        results = self._driver.query(q, returns= client.Node)
        for node in results:
            doctors.append(node[0]["name"])  # adds doctor name
        return doctors
    #Creates a connection between two personss
    def add_PatientConnection(self,name1,name2):
        patient1 = "MATCH (p:Patient) WHERE p.name = \"{0}\" RETURN d".format(name1)
        patient2 = "MATCH (p:Patient) WHERE p.name = \"{0}\" RETURN d".format(name2)
        patient1.relationships.create("Knows", patient2)

    #Crates a session with a doctor created beforehand and prescribes the drug
    def apoint_Session(self,patientName,patientTel,doctorName,drugName,date1,date2,dose):
            self.add_Patient(patientName, patientTel)
            self.add_Drug(drugName,date1,date2,dose)
            q1 = "MATCH (d:Doctor) WHERE d.specialty = \"{0}\" RETURN d".format(doctorName)
            q2 = "MATCH (p:Patient) WHERE d.specialty = \"{0}\" RETURN p".format(patientName)
            q3 = "MATCH (m:Drug) WHERE d.specialty = \"{0}\" RETURN m".format(drugName)
            q2.relationships.create("Visits",q1)
            q1.relationships.create("Prescribes",q3)
            q2.relationships.create("Takes",q3)

    def recommend_Doctor(self):
        return "Assassin"
