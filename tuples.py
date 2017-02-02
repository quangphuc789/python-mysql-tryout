# A tuple in python works as a list of constants in other languages

tup = 1, 2, 3, 4, 5
print tup

for val in tup:
    print val * 2

print tup[2]

# Trigger error since tuples in python are immutable
# tup[2] = 10

