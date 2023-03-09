
#sets don't care about order print the sets below it gives unique print everytime

subjects = {'history', 'maths', 'English', 'science'}
print(subjects)



#sets also throw away the duplicates
subjects_new = {'history', 'maths', 'English', 'science', 'science'}
print(subjects_new)


#sets can also be used to check the common elements in both

subjects_new = {'history', 'maths', 'English', 'science', 'science'}
subjects_old = {'history', 'maths', 'Nepali', 'social', 'art'}

print(subjects_old.intersection(subjects_new))

#sets can also be used to check the difference among two sets us difference


subjects_new = {'history', 'maths', 'English', 'science', 'science'}
subjects_old = {'history', 'maths', 'Nepali', 'social', 'art'}

print(subjects_old.difference(subjects_new))


#sets can also be used to create a union
subjects_new = {'history', 'maths', 'English', 'science', 'science'}
subjects_old = {'history', 'maths', 'Nepali', 'social', 'art'}

print(subjects_new.union(subjects_old))