from sys import argv
script, filename = argv
print(f"We are going to erase {filename}")
print("If you don't want that, hit Ctrl + C")
print("If you do want that, hit ENTER")
input("?")


print("Opening the file")
target = open(filename,'w')


print("Truncating the file, GoodBye")
target.truncate()

print("Now I am going to ask you for three lines.")
line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")


print("I am going to write these to the file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)


print("Finally close it")
target.close()
