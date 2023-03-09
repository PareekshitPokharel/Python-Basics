
#ADVANCED STRING FORMATTING IN PYTHON

tag = 'H1'
text = 'This is a headline'
sentence = '<{0}> {1} </{0}>'.format(tag, text) #>>the 0 will take the first value from the formatting and 1 will take the second value
print(sentence)

#ACCESSING DICTIONARY 

person = {'name': 'Pareekshit' , 'Age': 24}

comb = "I am {0[name]} and I am {0[Age]} year's old".format(person)
print(comb)

sentence = "I am {name} and I am {age} year's old".format(name = 'pareekshit', age = '24')

#Method 2 using kwargs technique
person = {'name': 'Pareekshit' , 'Age': 24}
sentence = "I am {name} and I am {Age} year's old".format(**person)
print(sentence)


#ACCESSING LISTS

person = {'name': 'Pareekshit' , 'Age': 24}
L = ['JABEEN', 24]

comb = "I am {0[0]} and I am {0[1]} year's old".format(L) #The first 0 stands for L and the second stands for indexing inside the list
print(comb)


#Decimal formatting

value = 3.12415678

formatted = 'The value is {:.2f}'.format(value) #This will simply format the decimal values to 2 after the numeric value
print(formatted)

#Comma seperators

value = 100000000
comma = 'The value is {:,.2f}'.format(value)
print(comma)


#DATE TIME FORMATTING
import datetime

date = datetime.datetime(2022, 11, 5 , 10 ,30,00)
print(date)

#%B =month
# %d = date
# %Y = year
formating_date = 'The formatted date is {:%B %d, %Y}'.format(date)
print(formating_date)


#Example 1
formating_date = 'The formatted date is {0:%B %d, %Y} and was the {0:%j} day of the year'.format(date) #HERE IF WE USE WITHOUT 0 IT WILL GIVE AN ERROR BECAUSE NOW WE HAVE MULTIPLE PLACEHOLDERS
print(formating_date)



