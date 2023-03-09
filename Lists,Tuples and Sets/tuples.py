#We cannot modify tuples so they are immutable while lists are mutable because we can modify them

subjects = ['Maths', 'History', 'Computerscience', 'English']
subjects1 = subjects

print(subjects)
print(subjects1)

#changing the values because lists are mutable

subjects[0] = 'economics'
print(subjects)
print(subjects1)


#the case is different with the tuples

subjects2 = ('Maths', 'History', 'Computerscience', 'English')
subjects3 = subjects2

print(subjects2)
print(subjects3)

subjects2[0] = 'Art' #we will get an error here because tuples cannot be modified