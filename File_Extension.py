# Program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")            # Reading the file(input)
f_extns = filename.split(".")                                # Finding the extension of the file
print ("The extension of the file is : " + repr(f_extns[-1]))       # Printing the extension of the file

# This is was already taught in my college so I have done in this way
# I am not able to do this program with the basics..