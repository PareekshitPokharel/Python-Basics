#instead of using .format we can directly use f string to do this example

first_name = 'pareekshit'
last_name = 'Pokharel'
sentence = f'My name is {first_name} {last_name}'
print(sentence)

#USING DICTIONARY METHOD

person = {'name':'pareekshit', 'age':24}
dict_sentence = f"My name is {person['name']} {person['age']}" #>>MAKE SURE YOU CHECK OUT FOR DOUBLE QUOTES AND SINGLE QUOTES 
print(dict_sentence)

#working on calculations
calc = f'4 times 11 is equals to : {4 * 11}'
print(calc)

#using loop on f string method

for n in range (1, 11):
	value = f'the value of n is {n:02}'
	print(value)

