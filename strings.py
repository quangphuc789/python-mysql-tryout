str1 =  "String 1"
print "Whole string " + str1
print "**********"
print "First character " + str1[1]
print "**********"

# Note that in python users cannot combine String and Integer. There is a need to convert
print "String length " + str(len(str1))
print "**********"

print "Print each letter out of string"
for letter in str1:
    print letter
print "**********"

# Result in error
# str1[7] = '2';
# print str1
str1 = "String 2"
print str1

