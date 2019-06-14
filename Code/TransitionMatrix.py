
import pandas as pd
import numpy as np

def calculateT(csv_file):
	column_name='ACTIVITY'
	df = pd.read_csv(csv_file, sep=';')
	saved_column = df[column_name]

	mylist = list( dict.fromkeys(saved_column) )
	ml = sorted(mylist)
	print(ml)

	 
	#['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
	if(csv_file == 'labeledA.csv'):
		sor = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
	else:
		sor = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']


	#dictionary for indexing in T
	my_dict = {}
	index = 0
	for name in sor:
		my_dict[name] = index
		index+=1
	#create the Transition Matrix
	T = np.zeros([len(sor),len(sor)]);
	times = np.zeros([1,len(sor)]);
	prev = '';
	for activity in saved_column:
		if (prev == ''):
			print('first')
			prev = activity
		else:	
			T[my_dict[prev], my_dict[activity]] +=1
			times[0, my_dict[prev]] += 1;
			prev = activity
	print(sor)
	print(T)

	#Normalize the matrix 
	for i in range(0,T.shape[0]):
		T[i,:]=T[i,:]/times[0,i]
	print(T)
	print(times)

def main():
	A = 'labeledA.csv'
	B = 'labeledB.csv'
	calculateT(A)

if __name__== "__main__":
  main()
