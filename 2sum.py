'''
We are interested to compute the number of target values, t, in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y
that satisfy x+y=t.
'''

with open('2sum.txt') as f:
    arr = [int(line) for line in f]

hashset = set()
hashset.update(arr)

counter = 0

for target in range(-10000, 100001):
    if target % 500 == 0:
        print(target)
    for val in arr:
        val_c = target - val
        if val_c in hashset and (val != val_c):
            counter += 1
            break

print('Counter is ', counter)
