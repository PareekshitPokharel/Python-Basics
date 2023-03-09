#TRY AND EXCEPT IS USED IN CASES WHERE THE ERRORS ARE PREDICTABLE AND WE WOULD NOT WANT THE CUSTOMER TO SEE THAT ERROR


try:
	file = open('test.txt')

except Exception:
	print('File not found!')


#example 2

try:
	file = open('test123.txt')
	var = bad_var
except FileNotFoundError: ###>> this file not found error is the default error when the opened filed does not exist first error that we are handling here
	print('File not found!')
except NameError: ##>>>NameError occurs is another error that we are handling here with except block
	print('correct that variable')


#example 3

try:
	file = open('test123.txt')
except FileNotFoundError: ###>> this file not found error is the default error when the opened filed does not exist first error that we are handling here
	print('File not found!')
except NameError: ##>>>NameError occurs is another error that we are handling here with except block
	print('correct that variable')
else:					###>> this else clause only runs if we do not throw an exception
	print(file.read()) 
	file.close()
finally: ##>>this code is executed no matter what the condition is fulfilled or not
	print('executing finally')



#example 4 raise exceptions manually

try:
	file = open('test123.txt')
	if file.name == 'test123.txt':
		raise Exception
except Exception:
	print('wrong file name')

