#Creating dictionaries and accessing the values

student = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}
print(student['name'])


#we can use the get method to return the value of a key without an error
student = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}
print(student.get('location'))


#we can update the keys using [''] method just like adding columns in pandas

student1 = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}
student1['location'] = 'ontario'
print(student1)

#we can also update the keys and values using update method
student1 = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}
student1.update({'name': 'grishma'})
print(student1)

#del key word can be used to delete specific key and values

del student1['name']
print(student1)


#Looping through all the keys and values

student1 = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}
print(len(student1)) ##Gives all the length of keys in the dictionary
print(student1.keys()) ## Shows all the keys in the variable
print(student1.items()) ##Gives pairs of the keys and values in the dictionary


#loooping through the key and values in dicitonary

student1 = {'name':'pareekshit', 'Age':25, 'courses':['Maths', 'english']}

for x,y in student1.items():
	print(x,y)



