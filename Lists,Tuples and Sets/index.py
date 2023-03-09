
#Lists are denoted by [] square brackets
#it allows us to work with the lists of values

#counting the lenghts of our lists
subjects = ['Maths', 'History', 'Computerscience', 'English']
print(len(subjects))

#accessing the values inside the lists
print(subjects[0])

#we can also access the values in the list with negative items 
print(subjects[-1]) #gives the last item in the lists

#accessing the list of values in the list
print(subjects[0:3])

#Append method to add the values in the lists
subjects = ['Maths', 'History', 'Computerscience', 'English']
subjects.append('Music')
print(subjects)


#To append the value in a specific position we can use the insert method 
new_subjects = ['Maths', 'History', 'Computerscience', 'English']
new_subjects.insert(3, 'Music') #>> insert takes position in the first place sperated by comma and value in the second place
print(new_subjects)

#since append will append one list one the other for example look at the case below:

subjects1 = ['Maths', 'History', 'Computerscience', 'English']
subjects2 = ['History', 'Social study']

subjects1.append(subjects2)
print(subjects1)

# we will use the extend method to solve this case
subjects1 = ['Maths', 'History', 'Computerscience', 'English']
subjects2 = ['History', 'Social study']
subjects1.extend(subjects2)
print(subjects2)



#remove the values from the list using remove
subjects = ['Maths', 'History', 'Computerscience', 'English']
subjects.remove('Maths')

#pop will remove the last value and it will also return the value it removed

subjects = ['Maths', 'History', 'Computerscience', 'English']
popped = subjects.pop()
print(popped)


#WE CAN ALSO REVERSE THE ITEMS IN THE LIST USING REVERSE METHOD
subjects = ['Maths', 'History', 'Computerscience', 'English']
subjects.reverse()
print(subjects)

#Sorted method can be used to bring the sorted list

subjects = ['Maths', 'History', 'Computerscience', 'English']

sorted_course = sorted(subjects)
print(sorted_course)

#we can also get the min max and sum of the list

list1 = [1,2,3,4,5,6,7,8]
print(sum(list1))
print(min(list1))
print(max(list1))


#WE CAN ALSO GET THE INDEX OF THE VALUE IN THE LIST

subjects = ['Maths', 'History', 'Computerscience', 'English']

print(subjects.index('History'))


# use in function to return boolean values from the list
subjects = ['Maths', 'History', 'Computerscience', 'English']

print('Maths' in subjects)


#WE CAN ALSO GRAB THE INDEX AND VALUES USING ENUMERATE FUNCTION IN PYTHON WITH THE FOR LOOP:

subjects = ['Maths', 'History', 'Computerscience', 'English']

for index,x in enumerate(subjects):
	print(index, x)

#we can also start the indexing at 1 instead of 0 with the start method

subjects = ['Maths', 'History', 'Computerscience', 'English']

for index,x in enumerate(subjects, start = 2):
	print(index, x)


#we can also seperate these values in the string using the join method

subjects = ['Maths', 'History', 'Computerscience', 'English']

sperated = " - ".join(subjects) 

print(sperated)
