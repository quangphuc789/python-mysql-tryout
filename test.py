#!/usr/bin/python
def checkName(name):
    checkName = input("Is your name " + name + "? ")

    if checkName.lower() == "yes":
        print("Hello,", name);
    else:
        print("We are sorry about that.")

checkName("Timothy")