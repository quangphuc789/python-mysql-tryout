#!/usr/bin/python
myList = [1, 2, 3, 4, 5]

for i in myList:
    val = i * 2
    print val

print "********"

for i in range(1, len(myList) + 1):
    val = 2 * myList[i - 1]
    print val
