'''
Script was written to compute strongly computed components in
enterprise knowledge graph. We use the Kosaraju's two pass algorithm
for this purpose.
'''

from collections import defaultdict
import sys
import threading


adj_list = defaultdict(list)
rev_list = defaultdict(list)
scc_list = defaultdict(list)

a_file = open('SCC.txt')
lines = a_file.read().splitlines()
for l in lines:
    tokens = l.split() # defaulted to be whitespace
    adj_list[int(tokens[0])].append(int(tokens[1]))
    rev_list[int(tokens[1])].append(int(tokens[0]))
a_file.close()

explored = set() # cheap membership
finish_time = 0 # finishing times
source = None # current source node
finish_d = {}
visited = set()

'''
First pass
'''

def DFS1(graph, node):
    global explored, finish_time, finish_d
    explored.add(node)
    for arc in graph[node]:
        if arc not in explored:
            DFS1(graph, arc)
    # reach here, done recursing
    finish_time = finish_time +  1
    finish_d[finish_time] = node

def DFS1_loop(graph):
    global explored
    sorted_keys = sorted(graph.keys(), reverse = True)
    for i in sorted_keys:
        if i not in explored:
            DFS1(graph, i)

'''
Second pass
'''
def DFS2(graph, node):
    global visited, scc_list, source
    visited.add(node)
    scc_list[source].append(node)
    for arc in graph[node]:
        if arc not in visited:
            DFS2(graph, arc)

def DFS2_loop(graph):
    global finish_d, visited, source
    sorted_keys = sorted(finish_d.keys(), reverse = True)
    for j in sorted_keys:
        curr_node = finish_d[j]
        if curr_node not in visited:
            source = curr_node
            DFS2(graph, curr_node)

def main():
    DFS1_loop(rev_list)
    print(len(explored))
    explored.clear()
    print(len(explored))
    DFS2_loop(adj_list)
    print(sorted([[k, len(v)] for k, v in list(scc_list.items())], key = lambda x: x[1], reverse=True)[:5])

'''
Use multithreading to overcome RAM limitations.
'''

if __name__ == '__main__':
    # https://stackoverflow.com/questions/2917210/what-is-the-hard-recursion-limit-for-linux-mac-and-windows
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
