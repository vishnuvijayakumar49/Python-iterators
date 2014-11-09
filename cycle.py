import itertools as it

k = it.cycle('ABC')

print k

for i in range(12):
    print k.next()


