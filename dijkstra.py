import sys
import threading


with open('dijkstraData.txt') as f:
    #dijkstraData
    #a = [[int(x) for x in ln.split()] for ln in f]
    data = []
    list_data = []
    node_list = []
    u = []
    v = []
    data_u = []
    data_v = []
    dict_nested = {}
    list_nested = []
    for ln in f:
        #print ln
        #print type(ln)
        #print len(ln)
        if len(ln) >1:
            data = ln.split()
            #print data
            list_data.append(data)
            #print list_data

    for i in range(len(list_data)):
        node_list.append(i+1)
        del list_data[i][0]

        for j in range(len(list_data[i])):
            u,v = list_data[i][j].split(',')
            #print u,v
            #print type(u)
            data_u.append(int(u))
            data_v.append(int(v))
        #print data_u,data_v
        list_nested.append(dict(zip(data_u,data_v)))
        #print list_nested
        data_u,data_v = [],[]
    #print node_list
    #print list_nested
    dict_nested = dict(zip(node_list,list_nested))

# print(dict_nested)
def dijkstra():
    scores = []
    V = node_list
    X = [1]
    A = {}
    A[1] = 0
    data_w = []

    while X != V:
        for v in X:
            for w in dict_nested[v].keys():
                if w not in A:
                    data_w.append(w)
                    scores.append(A[v] + dict_nested[v][w])

        find_w = 0
        find_w = data_w[scores.index(min(scores))]
        X.append(find_w)
        A[find_w] = min(scores)
        X.sort()
        scores.clear()
        data_w.clear()

    #print A
    print([A[key] for key in [7,37,59,82,99,115,133,165,188,197]])

if __name__ == '__main__':
    dijkstra()
