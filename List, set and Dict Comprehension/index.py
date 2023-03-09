#Basic list comprehension

nums = [1,2,3,4,5,6,7,8,9]
my_list = []
for x in nums:
	my_list.append(x)
print(my_list)


#we can shorten the above method by just
#EXAMPLE 1
my_list2 = [x for x in nums] #>>x is what we want, for is the loop, x is what we are iterating over and nums is the variable that holds the value
print(my_list2)

#EXAMPLE2
my_list3 = [x*x for x in nums]
print(my_list3)

#EXAMPLE3
#we want the even number from nums in a new list

my_list4 = [x for x in nums if x%2 == 0]
print(my_list4)

#EXAMPLE 4
my_list5 = []
for x in 'abcd':
	for y in range(4):
		my_list5.append((x, y))
print(my_list5)


my_list5 = [(x,y) for x in 'abcd' for y in range(4)]
print(my_list5)


#WE CAN DO THE SAME WITH THE DICTIONARY COMPREHENSIONS AS WELL

names = ['Bruce', 'Clark', 'peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'spiderman', 'wolverine', 'Deadpool']
x= zip(names, heros)
print (list(x)) #>>this will match out with the names and the heroes with it


#EXAMPLE5 5
my_dict = {}
for name,hero in zip(names,heros):
	my_dict[name] = hero
print(my_dict)

#using it as a list comprehension

my_dict10 = {name:hero for name, hero in zip(names,heros)}
print(my_dict10)

#if we don't want peter in the list we can use if function

my_dict10 = {name:hero for name, hero in zip(names,heros) if name != 'peter'}
print(my_dict10)


#SET COMPREHENSION

# **Note we can use the set comprehension to reduce the repeating values and keep only those that are unique

nums = [1,2,2,2,2,3,3,3,3,3,4,4,5,6,7,8,8,8,8,9,9,9,9] #** Notice how we have repeating values here
my_set = set()
for n in nums:
	my_set.add(n) #*notice we did not use append because set attribute or dictionary do not have append method
print(my_set)

#EASY WAY TO SOLVE THE ABOVE PROBLEM USING SET COMPREHENSION

easy_set = {n for n in nums}
print(easy_set)







