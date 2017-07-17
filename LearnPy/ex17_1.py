print(f"input the file you want to copy")
filename = input("filename>")
infile = open(filename)
data = infile.read()

print(f"The input file is {len(data)} bytes long")

print("Ready, hit RETURN to continue, CTRL-C to abort")
output = input("input the new file name>")


out_file = open(output, 'w')
out_file.write(data)

print("All right, all done")

out_file.close()
infile.close()
