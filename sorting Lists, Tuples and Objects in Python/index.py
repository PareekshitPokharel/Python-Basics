#Sorting lists in python using sorted method

li = [9,1,7,6,8,4,3,5,2,0]

so_li = sorted(li) #sorted method arranges the values in the ascending order
print('sorted lists:\t', so_li) 

#Reverse function to sort in descending order

li = [9,1,7,6,8,4,3,5,2,0]
rev_li = sorted(li, reverse = True)
print('Reversed sorted lists: \t', rev_li)

#sort won't work with tuples hence you have to do sorted instead of sort
li = (9,1,7,6,8,4,3,5,2,0)
new_list = sorted (li)
print(new_list)

#sorting with the negative values we can assign key = abs which simply stand for absolute values

li = [-6,-5,-4,-3,1,2,3]

sort = sorted(li, key = abs)
print(sort)

