# Reading the filw using the context manager

with open ("hello.txt", 'r') as f:
	f_contents = f.read()
	print(f_contents)
	f_contents = f.read(100) #will read 100 character of a file
	print(f_contents)


with open ('new.txt', 'w') as w: #writing on the file using w option
	w.write("Hello world !")



	