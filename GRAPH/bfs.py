import defaultdict

class Graph:
   def __init__(self):
       self.graph = defaultdict[list]

   def addEdge(self,u,v):
       self.graph[u].append(v)

   def bfs(self,s):
       visited = [False]*(len(self.graph))
       queue=[]
       queue.append(s)
       visited[s] = True
       while queue:
             s = queue.pop(0)
             print(s)
             for i in self.graph[s]:
                 if visited[i] == False:
                    queue.push(i)
                    visited[i] = True