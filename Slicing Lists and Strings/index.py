#SLICING IS BASICALLY THE WAY TO EXTRACT CERTAIN INFORMATION FROM THE LISTS AND STRINGS


my_list = [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]

#		 [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1] ##>we can access the last element using negative indexing as well 

print((my_list)[-1])


#ACCESSING CERTAIN RANGE FROM THE LIST USING INDEXIN

#	**list[start:stop]
my_list = [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
print (my_list [0:4]) #>> last index is exclusive in our case 4


#we can also combine positive and negative indexing

my_list = [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
print (my_list [1:-1]) #this did not print the last element because as we said earlier the last element is non inclusive


#using step to skip the value

#[start:stop:step]
my_list = [0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0:-1:2]) #>> it's skipping every 2nd value


#MOVING BACKARDS IN THE LIST
my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list1[-1:0:-1])

#REVERES THE ENTIRE LIST
my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list1[::-1])

#WE CAN ALSO SLICE THE STRINGS 

url = "http://facebook.com"

print(url[-4:]) #>>print only the .com
print(url[7:]) #>>print only the facebook.com


