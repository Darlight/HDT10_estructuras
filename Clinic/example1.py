from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

# Create some nodes with labels
doctor = db.labels.create("Doctor")
u1 = db.nodes.create(name="Marco")
doctor.add(u1)
u2 = db.nodes.create(name="Daniela")
doctor.add(u2)

patient = db.labels.create("Patient")
b1 = db.nodes.create(name="Punk IPA")
b2 = db.nodes.create(name="Hoegaarden Rosee")
# You can associate a label with many nodes in one go
patient.add(b1, b2)