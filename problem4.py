#This is the program which gives all the directories available in your laptop
#I didn't write it by my own.....The code is given by chatgpt
import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
