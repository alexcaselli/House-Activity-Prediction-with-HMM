
import pandas as pd
import numpy as np

def calculateT(csv_file):
	activity='ACTIVITY'
	df = pd.read_csv(csv_file, sep=';')
	activity_column = df[activity]
	mylist = list( dict.fromkeys(activity_column) )
	ml = sorted(mylist)
	print(ml)

	location='LOCATION'
	location_column = df[location]
	act_type='TYPE'
	type_column = df[act_type]
	place ='PLACE'
	place_column = df[place]

	oss = location_column + type_column + place_column
	print(len(activity_column))
	print(len(oss))


	mylist = list( dict.fromkeys(oss) )
	ml = sorted(mylist)
	print('oservations: ')
	print(ml)

	#Osservazioni ordinate senza duplicati
	if(csv_file == 'labeledA.csv'):
		oss_sor = ['BasinPIRBathroom', 'BedPressureBedroom', 'CabinetMagneticBathroom', 'CooktopPIRKitchen', 'CupboardMagneticKitchen', 'FridgeMagneticKitchen', 'MaindoorMagneticEntrance', 'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToasterElectricKitchen', 'ToiletFlushBathroom']
	else:
		oss_sor = ['BasinPIRBathroom', 'BedPressureBedroom', 'CupboardMagneticKitchen', 'DoorPIRBedroom', 'DoorPIRKitchen', 'DoorPIRLiving', 'FridgeMagneticKitchen', 'MaindoorMagneticEntrance', 'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToiletFlushBathroom']


	 
	#Stati ordinati senza duplicati
	if(csv_file == 'labeledA.csv'):
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
	O = np.zeros([len(sor),len(oss_sor)]);
	times = np.zeros([1,len(sor)]);
	
	for i in range(0, len(activity_column)):
		O[my_dict[activity_column[i]], my_dict_oss[oss[i]]] +=1
		times[0, my_dict[activity_column[i]]] += 1;
			
	print(sor)
	print(O)

	#Normalize the matrix 
	for i in range(0,O.shape[0]):
		O[i,:]=O[i,:]/times[0,i]
	print(O)
	print(times)

def main():
	A = 'labeledA.csv'
	B = 'labeledB.csv'
	calculateT(B)

if __name__== "__main__":
  main()

