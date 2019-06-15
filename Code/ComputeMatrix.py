import pandas as pd
import numpy as np
import csv

def computeTransitionMatrix(home):
	home = './Dataset/datasetCSV/labeled'+home+'.csv'
	return calculateT(home)

def computeOsservationMatrix(home):
	home = './Dataset/datasetCSV/labeled'+home+'.csv'
	return calculateO(home)

def calculateT(csv_file):
	column_name='ACTIVITY'
	df = pd.read_csv(csv_file, sep=';')
	saved_column = df[column_name]
	homeA = False

	mylist = list( dict.fromkeys(saved_column) )
	ml = sorted(mylist)
	# print(ml)

	#['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
	if 'labeledA' in csv_file:
		sor = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
		homeA = True
	else:
		sor = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']

	#dictionary for indexing in T
	my_dict = {}
	index = 0
	for name in sor:
		my_dict[name] = index
		index += 1

	#create the Transition Matrix
	T = np.zeros([len(sor),len(sor)])
	times = np.zeros([1,len(sor)])
	prev = ''

	for activity in saved_column:
		if prev == '':
			# print('first')
			prev = activity
		else:	
			T[my_dict[prev], my_dict[activity]] +=1
			times[0, my_dict[prev]] += 1
			prev = activity
	# print(sor)
	if homeA:
		with open("./Data/HomeAactivity.csv", "w") as csvData:
			writer = csv.writer(csvData, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting'])
			writer.writerow([int(times[0][0]), int(times[0][1]), int(times[0][2]), int(times[0][3]), int(times[0][4]), int(times[0][5]), int(times[0][6]), int(times[0][7]), int(times[0][8])])
	else:
		with open("./Data/HomeBactivity.csv", "w") as csvData:
			writer = csv.writer(csvData, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting'])
			writer.writerow([int(times[0][0]), int(times[0][1]), int(times[0][2]), int(times[0][3]), int(times[0][4]), int(times[0][5]), int(times[0][6]), int(times[0][7]), int(times[0][8]), int(times[0][9])])  	
				
	# print(times)

	for row in range(0, len(T)):
		for column in range(0, len(T[row])):
			if T[row][column] == 0:
				T[row][column] = 1
				times[0][row] += 1
	
	# print(T)
	# print(times)

	#Normalize the matrix 
	for i in range(0,T.shape[0]):
		T[i,:]=T[i,:]/times[0,i]
	# print(T)
	# print(times)

	#Create start probabilities
	denominator = sum(times[0])

	check = 0
	for i in range(0, len(times[0])):
		times[0][i] = times[0][i]/denominator
		check += times[0][i]
	
	# print(check)
	# print(times)

	return T, times

def calculateO(csv_file):
	activity='ACTIVITY'
	df = pd.read_csv(csv_file, sep=';')
	activity_column = df[activity]
	mylist = list( dict.fromkeys(activity_column) )
	ml = sorted(mylist)
	# print(ml)

	location='LOCATION'
	location_column = df[location]

	act_type='TYPE'
	type_column = df[act_type]

	place ='PLACE'
	place_column = df[place]

	oss = location_column + type_column + place_column
	# print(len(activity_column))
	# print(len(oss))


	mylist = list( dict.fromkeys(oss) )
	ml = sorted(mylist)
	# print('oservations: ')
	# print(ml)

	#Osservazioni ordinate senza duplicati
	if 'labeledA' in csv_file:
		oss_sor = ['BasinPIRBathroom', 'BedPressureBedroom', 'CabinetMagneticBathroom', 'CooktopPIRKitchen', 'CupboardMagneticKitchen', 'FridgeMagneticKitchen', 'MaindoorMagneticEntrance', 'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToasterElectricKitchen', 'ToiletFlushBathroom']
	else:
		oss_sor = ['BasinPIRBathroom', 'BedPressureBedroom', 'CupboardMagneticKitchen', 'DoorPIRBedroom', 'DoorPIRKitchen', 'DoorPIRLiving', 'FridgeMagneticKitchen', 'MaindoorMagneticEntrance', 'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToiletFlushBathroom']

	#Stati ordinati senza duplicati
	if 'labeledA' in csv_file:
		sor = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
	else:
		sor = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']

	#dictionary for indexing Activity in O
	my_dict = {}
	index = 0
	for name in sor:
		my_dict[name] = index
		index+=1

	#dictionary for indexing Actions in O
	my_dict_oss = {}
	index = 0
	for name in oss_sor:
		my_dict_oss[name] = index
		index+=1

	#create the Osservation Matrix
	O = np.zeros([len(sor),len(oss_sor)]) 
	times = np.zeros([1,len(sor)]) 
	
	for i in range(0, len(activity_column)):
		O[my_dict[activity_column[i]], my_dict_oss[oss[i]]] +=1
		times[0, my_dict[activity_column[i]]] += 1 
		
	# print(sor)
	# print(O)

	for row in range(0, len(O)):
		for column in range(0, len(O[row])):
			if O[row][column] == 0:
				O[row][column] = 1
				times[0][row] += 1

	# Normalize the matrix 
	for i in range(0,O.shape[0]):
		O[i,:]=O[i,:]/times[0,i]
	#print(O)
	# print(times)
	return O