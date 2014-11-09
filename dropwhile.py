import itertools as it

a = [1, 6, 2, 8, 14, 12, 71, 5]

k = it.dropwhile(lambda x:x <10, a)

print k

for element in k:
    print element


