# def bfs(graph, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited
#
# '''
# Iterative version:
# '''
# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             stack.extend(graph[vertex] - visited)
#     return visited

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
