from sys import argv
from os.path import exists

script, from_filename, to_filename = argv

print(f"Now I will copy from {from_filename} to {to_filename}")

infile = open(from_filename)
data = infile.read()

print(f"The input file is {len(data)} bytes long")
print(f"Does the output file exist?{exists(to_filename)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()


out_file = open(to_filename, 'w')
out_file.write(data)

print("All right, all done")

out_file.close()
infile.close()
