"""
Universidad del Valle de Guatemala
Seccion 10 - Estructura de datos
Grupo 6
Mario Perdomo 18029
Josue Sagastume 18173
Andres Quan 17652
Main:
Muestra las opciones necesarias para hacer ajuestes en la base de datos Neo4j
"""
import sys
from time import sleep
from DBfunctions import *
#include <DBfunctions.py>


i = True
doctor_name = " "
doctor_specialty = " "
doctor_contact= " "
patient_name = " "
patient_age = 0
patient_gender= " "
date_visit = " "
medicine = " "

def main():
	print("Welcome to the program! \nWhat would you like to do?")
	database = DBfunctions("http://localhost:7687","neo4j","12345")
	while i is True:
		print("1. Check Doctors \n2. Check a Doctor's information \n3. Check patients \n4. Check a specific patient\n 5. Input data for a new doctor")
		sleep(3)
		option = input("Your option: ")
		#Information to have in mind when working with this:
		#	When it is "Check Doctors," release a list of available docotor names, not anything else
		#	When it is a "Check a Doctor's information," do release his doctor_name, doctor_specialty and doctor_contact
		#	When 3 is chosen, release a list of patients
		#	When 4 is chosen, release patient_name, patient_age, patient_gender, date_visit and medicine
		if option == 1:
			print("You've chosen to check the doctors")
			print("The current doctor list is:")
			with doctor_name as doc:
				for doc in database#DATABASE GOES HERE:
					print(doc)
					sleep(0.5)
			break
		elif option == 2:
			index = input("Would you like to use an index (1), or a name? (2): ")
			#HERE GOES THE METHOD FOR A DOCTOR RELEASE WITH INFORMATION
			print("Doctor: {}" + .format(#HERE GOES DATABASE NAME))
			print("Specialty: {}" .format(#HERE GOES THE DATABASE SPECIALTY))
			print("Contact: {}" .formt(#HERE GOES THE CONTACT))
		elif option == 3:
			print("You've chosen to check the patients")
			print("Your current patient list is: ")
			with patient_name as pat:
				for pat in #DATABASE GOES HERE:
					print(pat)
		elif option == 4:
			index = input("Would you like to use an index or a name? (1, 2): ")
			#Method to extract form the database?
			print("Patient: {} " .format(#HERE GOES DATABASE NAME))
			print("Age: {}" .format(#Here))
			print("Gender: {}" .format(#Here))
			print("Last date of visit: {}" .format(#Date))
			print("Medicine: {}" .format(#Meds))
		elif option == 5:
			#IN BETWEEN ALL OF THESE, THERE NEEDS TO BE SOMETHING TO ADD ALL THESE VALUES TO THE DATABASE
			doctor_name = input("What is the name of the new doctor?\n")
			print("Saving...")
			sleep(2)
			doctor_specialty = input("What is their Specialty?\n")
			print("Saving...")
			sleep(2)
			doctor_contact = input("What is their contact? \n")
			print("Saving...")
			sleep(2)
			try:
				DBfunctions.add_Doctor(doctor_name, doctor_contact, doctor_specialty, doctor_specialty)
			except:
				print("Invalid values. Could not be added to the database.")
			break
		elif option == 6:
			patient_name = input("What is their name? \n")
			print("Saving...")
			sleep(2)
			patient_contact = input("What is their phone contact?")
			sleep(2)
			try:
				DBfunctions.add_Patient(patient_name, patient_contact)
			except:
				print("Values could not be added to the database. Some values might be invalid.")
			break
		elif option == 7:
			print("You've chosen to add a relationships")
			try:
				name1 = input("What is the name of your patient?")
				erste = name1.rstrip()
				name2 = input("What is the name of your second patient?")
				zwitte = name2.rstrip()
				DBfunctions.add_PatientConnection(erste, zwitte)
			except Exception as e:
				raise print("Could not add the relationship. Exception: " + str(e))
