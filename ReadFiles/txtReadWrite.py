#!/usr/bin/python

userName = raw_input("Enter your user name: ")

fo = open("data.txt", "r+")

myName = fo.readlines()
notInFile = 1

if len(myName) > 0:
    for name in myName:
        print(name)
        if name != userName:
            notInFile = 1
            #break
        else:
            notInFile = 0
            #break
else:
    notInFile = 1

if notInFile == 1:
    fo.write(userName + "\n")
    print(userName + ", Your details have been added successfully")
else:
    print("Sorry, " + userName + " already exists")

fo.close()