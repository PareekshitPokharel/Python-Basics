#Printing out the Length of the message

message = 'Hello world!'
print(len(message))

#using idnexing to access the message 
print(message[0])

#lowercasing the string

print(message.lower())

#uppercasing the string

print(message.upper())

#counting the message

print(message.count('Hello')) #count takes at least one positional indexing

#using the find method to locate the string 

print(message.find('o'))

#replacing the string in the variable using.replace method
replace = 'hello world!'
print(replace.replace('hello', 'beautiful'))


#concatenate strings

variable1 = "what's your"
variable2 = 'name?'

message = variable1 + ' ' + variable2
print(message)


#using format techniques to concatenate strings
variable1 = "what's your"
variable2 = 'name?'

message = "Welcome! {} {}".format(variable1, variable2)
print(message)

#using F string for the formatting

variable1 = "what's your"
variable2 = 'name?'

message = f"Welcome! {variable1} {variable2}"
print(message)

#dir function to check other attributes
name = 'Michael'
print(dir(name)) 


#learning more about string
print(help(str))




