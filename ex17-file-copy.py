from sys import argv
from os.path import exists

"""
A Python script to copy one file to another.
It’ll be very short but will give you some ideas about other things you can do with files.
"""


"""
You should immediately notice that we import another handy command named exists. This returns True if a
file exists, based on its name in a string as an argument. It returns False if not. We’ll be using this function in the
second half of this book to do lots of things, but right now you should see how you can import it.
"""

script, from_file, to_file = argv

print("Copying from {} to {}" .format(from_file, to_file))

#we can do these 2 on one line - how?
input = open(from_file)
indata = input.read()

print("The input file is {} bytes long" .format(len(indata)))

print("Does the output file exist? {}" .format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input() not sure what this was supposed to do but it broke the script
output = open(to_file, 'w')
output.write(indata) 
print(indata)

print("Alright, all done.")

output.close()
input.close()