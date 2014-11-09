import itertools as it

a = [1, 8, 6, 2, 14, 12, 71]

k = it.takewhile(lambda x:x <10, a)

print k

for element in k:
    print element


