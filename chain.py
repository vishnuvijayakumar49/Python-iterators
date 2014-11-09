import itertools as it

k = it.chain('ABC', 'DEF')

print k

for i in range(6):
    print k.next()


