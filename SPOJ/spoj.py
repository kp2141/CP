# from collections import defaultdict
# flag = 0
# def dfs(graph,j,visited):
#     visited[j] = 1
#     count = 0
#     for k in graph[j]:
#         if visited[k]==0:
#             dfs(graph,k,visited)
#         elif(visited[k]):
#             count+=1
#             if count>=2:
#                 global flag
#                 flag = 1
# 
# R = lambda:map(int,input().split())
# n, m = R()
# graph  = defaultdict(list)
# 
# for _ in range(m):
#     u, v = R()
#     graph[u].append(v)
# 
# visited = [0 for _ in range(0,n+1)]
# print(visited)
# for i in graph.keys():
#     print("for i : "+str(i))
#     visited[i] = 1
#     for j in graph[i]:
#         dfs(graph,j,visited)
# for i in range(1,n+1):
#     if visited!=1:
#         flag = 1
# if flag:
#     print("NO")
# else:
#     print("YES")
from collections import defaultdict


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        # Add w to v ist.
        self.graph[v].append(w)
        # Add v to w list.
        self.graph[w].append(v)

        # A recursive function that uses visited[]

    # and parent to detect cycle in subgraph
    # reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):

        # Mark current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent
        # for this vertex
        for i in self.graph[v]:
            # If an adjacent is not visited,
            # then recur for that adjacent
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True

            # If an adjacent is visited and not
            # parent of current vertex, then there
            # is a cycle.
            elif i != parent:
                return True

        return False

    # Returns true if the graph is a tree,
    # else false.
    def isTree(self):
        # Mark all the vertices as not visited
        # and not part of recursion stack
        visited = [False] * self.V

        # The call to isCyclicUtil serves multiple
        # purposes. It returns true if graph reachable
        # from vertex 0 is cyclcic. It also marks
        # all vertices reachable from 0.
        if self.isCyclicUtil(0, visited, -1) == True:
            return False

        # If we find a vertex which is not reachable
        # from 0 (not marked by isCyclicUtil(),
        # then we return false
        for i in range(self.V):
            if visited[i] == False:
                return False

        return True

if __name__ == "__main__":
    n, m = map(int,input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u,v)

    if g.isTree():
        print("Yes")
    else:
        print("No")