
import os

path ="D:\\Brodie Stuff\\test.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("Thats is a file")
    elif os.path.isdir(path):
        print("that os a directory!")
else:
    print("That location doesn't exist")