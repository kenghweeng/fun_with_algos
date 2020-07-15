import heapq

with open('Median.txt') as f:
    a = [int(x) for x in f]

median = []

heaped = heapq.heapify(a) # note that no attributes for size of heap
# need to maintain separate pointers for size.

for i in range(1,len(a)+1):
    sorted_a = heapq.nsmallest(i,a[:i])
    if i % 2 == 0:
        median.append(sorted_a[int(i/2) - 1])
    else:
        median.append(sorted_a[int((i+1)/2) -1])

mode = sum(median) % len(median)
# print(mode)
