from sys import argv
from os.path import exists

script, from_file, to_file = argv

# replaces variables with the names of entered files
print(f"Copying from {from_file} to {to_file}")

# we could do these on one line, how?
indata = open(from_file).read()

# opens the output file in 'write' mode
open(to_file, 'w').write(indata)

print("Allright, all done")

# closes files
out_file.close()
in_file.close()