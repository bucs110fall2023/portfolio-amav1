print("Please spell your name:")
name = ""
ch = input("What is the first letter(leave empty when done)?")
while ch:
	name = name + ch
	ch = input("What is the next letter(leave empty when done)?")
print(name)

