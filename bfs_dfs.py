def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs2(graph, node):
    visited, queue =  set(), [node]
    visited.add(node) # add initial starting node.
    while queue:
        vertex = queue.pop(0)
        for edge in graph[vertex]:
            if edge not in visited:
                visited.add(edge)
                queue.append(edge)
# '''
# Iterative version:
# '''

# def dfs_iterative(graph, start):
#     stack, path = [start], []
#
#     while stack:
#         vertex = stack.pop()
#         if vertex in path:
#             continue
#         path.append(vertex)
#         for neighbor in graph[vertex]:
#             stack.append(neighbor)
#
#     return path

'''
Recursive version
'''
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def dfs(graph, node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor)

# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python#:~:text=Depth%2Dfirst%20search%20(DFS),structures%20like%20dictionaries%20and%20sets.

# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)
dfs(graph, 'A')
print(visited)
