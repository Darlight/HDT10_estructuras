import sys
from time import sleep


i = True
doctor_name = " "
doctor_speciality = " "
doctor_contact= " "
patient_name = " "
patient_age = 0
patient_gender= " "
date_visit = " "
medicine = " "

def main():
	print("Welcome to the program! \nWhat would you like to do?")
	while i is True:
		print("1. Check Doctors \n2. Check a Doctor's information \n3. Check patients \n4. Check a specific patient\n 5. Input data for a new doctor")
		sleep(3)
		option = input("Your option: ")
		#Information to have in mind when working with this:
		#	When it is "Check Doctors," release a list of available docotor names, not anything else
		#	When it is a "Check a Doctor's information," do release his doctor_name, doctor_specialty and doctor_contact
		#	When 3 is chosen, release a list of patients
		#	When 4 is chosen, release patient_name, patient_age, patient_gender, date_visit and medicine
		if option = 1:
			print("You've chosen to check the doctors")
			print("The current doctor list is:")
			with doctor_name as doc:
				for doc in #DATABASE GOES HERE:
					print(doc)
					sleep(0.5)
			break
		elif option = 2:
			index = input("Would you like to use an index (1), or a name? (2): ")
			#HERE GOES THE METHOD FOR A DOCTOR RELEASE WITH INFORMATION
			print("Doctor: {}" + .format(#HERE GOES DATABASE NAME))
			print("Specialty: {}" .format(#HERE GOES THE DATABASE SPECIALTY))
			print("Contact: {}" .formt(#HERE GOES THE CONTACT))
		elif option = 3:
			print("You've chosen to check the patients")
			print("Your current patient list is: ")
			with patient_name as pat:
				for pat in #DATABASE GOES HERE:
					print(pat)
		elif option = 4:
			index = input("Would you like to use an index or a name? (1, 2): ")
			#Method to extract form the database?
			print("Patient: {} " .format(#HERE GOES DATABASE NAME))
			print("Age: {}" .format(#Here))
			print("Gender: {}" .format(#Here))
			print("Last date of visit: {}" .format(#Date))
			print("Medicine: {}" .format(#Meds))
		elif option = 5:
			doctor_name = input("What is the name of the new doctor?\n")
			print("Saving...")
			sleep(2)
			doctor_specialty = input("What is their Specialty?\n")
			print("Saving...")
			sleep(2)
			doctor_contact = input("What is their contact? \n")
			print("Saving...")
			sleep(2)