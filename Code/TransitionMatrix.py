
import pandas as pd
import numpy as np

column_name='Activity'
df = pd.read_csv('ActivityA.csv', sep=';')
saved_column = df['Activity']

mylist = list( dict.fromkeys(saved_column) )
ml = sorted(mylist)
print(ml)

 
#['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
sor = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']

index = 0
listy = np.asarray(ml);

#indexing the activities
for name in sor:
	listy[listy==name]=index
	index+=1

#dictionary for indexing in T
my_dict = {}
index = 0
for name in sor:
	my_dict[name] = index
	index+=1
#create the Transition Matrix
T = np.zeros([9,9]);
times = np.zeros([1,9]);
prev = '';
for activity in saved_column:
	if (prev == ''):
		print('first')
		prev = activity
	else:	
		T[my_dict[prev], my_dict[activity]] +=1
		times[0, my_dict[prev]] += 1;
		prev = activity
print(T)

#Normalize the matrix 
for i in range(0,T.shape[0]):
	T[i,:]=T[i,:]/times[0,i]
print(T)
print(times)




