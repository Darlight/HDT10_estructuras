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
doctor_phone= " "
doctor_code = " "
patient_name = " "
patient_age = 0
patient_gender= " "
date_visit = " "
medicine = " "
menu = "1. Add relationship\n2. Get doctors by specialty\n3. Check recommended doctors by patients\n4. Add visit\n5. Add doctor\n6. Add patient"

def main():
	print("Welcome to the program! \nWhat would you like to do?")
	database = DBfunctions("http://localhost:7687","neo4j","12345")
	while i is True:
		print(menu)
		sleep(3)
		option = input("Your option: ")
		if option == 1:
			#Add relationship
                        print("RELATIONSHIP BETWEEN PATIENTS\n")
                        patient1 = input("What is the name of the first patient?\n")
                        patient2 = input("What is the name of the second patient?\n")
                        DBfunctions.add_PatientPatientConnection(patient1, patient2)
		elif option == 2:
                        #Get doctos by specialty
                        spec = input("What is the specialty you are looking for?\n")
                        doctors = find_DoctorsWithSpec(spec)
			print("Doctors: {0}".format(len(doctors)))
			for i in doctors:
                                print("Dr {0}".format(i))
		elif option == 3:
                        #Get doctors recommended by patients
			spec = input("What is the specialty you want the recommendation?\n")
			friend = input("What is the name of your friend?\n")
			doctors = recommend_Doctor(patientName, spec)

			print("Doctors: {0}".format(len(doctors)))
			for doctor in doctors:
                                print("Dr. {0}".format(doctor))
		elif option == 4:
			#Add visit
                        patient = input("What is the name of the patient?\n")
                        print("Saving...")
                        sleep(2)
                        doctor = input("What is the name of the doctor?\n")
                        print("Saving...")
                        sleep(2)
                        drug = input("What is the name of the drug?\n")
                        print("Saving...")
                        sleep(2)
                        dose = input("What is the dose for the patient?\n")
                        print("Saving...")
                        sleep(2)
                        try:
                                DBfunctions.add_visit(patient, doctor, drug, dose)
                        except:
                                print("Invalid values")
                        break
		elif option == 5:
			#Add doctor
			doctor_name = input("What is the name of the new doctor?\n")
			print("Saving...")
			sleep(2)
			doctor_specialty = input("What is their Specialty?\n")
			print("Saving...")
			sleep(2)
			doctor_phone = input("What is their phone number? \n")
			print("Saving...")
			sleep(2)
			doctor_code = input("What is their phone code? \n")
			print("Saving...")
			sleep(2)
			try:
                                DBfunctions.add_Doctor(doctor_name, doctor_phone, doctor_specialty, doctor_code)
                        except:
                                print("Invalid values")
			break
		elif option == 6:
                        #Add patient
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
                        
			
