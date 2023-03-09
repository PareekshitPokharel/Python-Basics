# = :sign is used for assinging the variables
# == :is used to test the equality
# != :is used to denot not equal
# >= :Denotes greater than or equal to
# <= :Denotes less than or equal to 
# is :Object identity


#using IF , ELIF and ELSE

language = 'java'

if language == 'java':
	print('the language is java') ###>>> This will check the first condition if the langauage is equals to java if not

elif language == 'python':
	print('the language is java') ##>>> This ELIF will check another condition if the language is equals to python

else:
	print('No match')	### if none of the cases are fulfilled it will print no match



#AND OR NOT BOOLEAN OPERATORS
user = 'Admine'
logged_in = True

if user =='Admin' and logged_in: #while using these operators they check for True Boolean values (in our case above both the condition of user being admin and logged in being true were met)
	print('Admin page')
else:
	print('Bad credentials')

#NOT operater will change true to a false and false to a true
user = 'Admin'
logged_in = True
if user =='Admin'and not logged_in: 
	print('Admin page')
else:
	print('Please log in')


#FALSE VALUES:
	# False
	# None
	# Zero of any numeric type
	# Any empty sequence. for example, '', (), []
	# Any empty maping. For example, {}

condition = False

if condition:
	print('evaluated to true')

else:
	print('evaluated to false')

