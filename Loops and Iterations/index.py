#Basic loop of each values

nums = [1,2,3,4,5]
for num in nums:
    print(num)

#using Break  in loops
nums = [1,2,3,4,5]
for x in nums:
    if x == 3:
        print("That's the number")#break will halt the loops in between
        break
    print(x)

#using continue in loops

nums = [1,2,3,4,5]

for x in nums:
    if x == 3:
        print('theres the number') #continue will hit the condition and still move on with the other number
        continue
    print(x)


#Using loops within the loops

nums = [1,2,3,4,5]
for number in nums:
    for values in 'abc':
        print(number, values)


#limiting the number of times a loop can happen using range
for i in range(10):
    print(i)

#specifying the start value and the end value in range
for i in range(1,11): ### this will specify the starting number and end number for loop
    print(i)


#WHILE LOOPS WILL KEEP GOING UNTIL CERTAIN CONDITION IS MET OR UNTIL WE HIT BREAK
x = 0
while x <10:
    print(x)
    x += 1

#USING BREAK TO GET OUT OF THE LOOP
y = 0 

while True:
    if y == 9000:
        break
    y = y+1
    print(y)






