#IN FUNCTION WE USE DEF KEYWORD WHICH STANDS FOR DEFINITION

#def my_func ():
#def stands for definition
#my_func stands for function name
#() these are used for passing parameters


def hello_func():
    pass
hello_func() #Note that if we call function without () it will equate to the function itself



#WORKING WITH THE FUNCTION

def new_func():
    print('hello world!')
new_func() #Note you will always have to call the function to return it's value


#WE CAN USE FUNCTION FOR MULTIPLE USES AND ITS LESS HECTIC TO EDIT AT THE FUNCTION LEVEL 

def hello_world():
    print("hello_world")

hello_world()
hello_world()
hello_world() #we can call it multiple times for a single function

        ##NOTE functions allow us to make a changes to a single line of code
        ##NOTE functions comply with the keyword DRY which means DO NOT REPEAT YOURSELF!


#WE CAN ALSO CHAIN THE FUNCTION WITH STRING METHODS

def function ():
    return 'chain methods'

print(function().upper()) ##we just uppercased this with the .upper method 


#PASSING PARAMETER ON THE FUNCTION

def greeting_func(Greeting1, Greeting2):
    return ' {} {} '.format(Greeting1, Greeting2)

print(greeting_func('Hello!', 'Are you fine?'))


#PRINTING *ARGS = ARGUMENT AND **KWARGS = KEYWORD ARGUMENT


def arg_func(*args, **kwargs):
    print(args)
    print(kwargs)

arg_func('Maths', 'Science', name='Pareekshit', age=24, location='bhadrapur')

        #*** NOTE SO BASICALLY ARGUMENTS ARE JUST TUPLES AND KEYWORD ARGUMENTS ARE SET OF DICTIONARY PRINT THIS OUTPUT TO SEE IT



#TO UNDERSTAND THIS BETTER LET US USE * AND ** TO PASS IT INTO OUR FUNCTION


def arg_function(*args, **kwargs):
    print(args)
    print(kwargs)

course = ('Maths', 'Nepali') #>>we will use this tuple as the args
info = {'name': 'Pareekshit', 'age': 24, 'location': 'bhadrapur'} #>>we will use this information as the kwargs

arg_function(course, info) #>> if we print this in a way we will get one whole tuple 



#BUT IF WE PRINT THIS WITH STAR * AND DOUBLE ** WE WILL GET WHAT WE ACTUALLY WANTED

def arg_function(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['Maths', 'Nepali'] #>>we will use this tuple or list as the args
info = {'name': 'Pareekshit', 'age': 24, 'location': 'bhadrapur'} #>>we will use this  dictionary information as the kwargs

arg_function(*course, **info) #>> HERE THE PYTHON WILL TAKE THE VALUES AND ARGS AND KWARGS AND UNPACK THEM INTO TUPLES AND DICTIONARY











