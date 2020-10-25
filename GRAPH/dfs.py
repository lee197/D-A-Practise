import defaultdict 

class Graph:
   def __int__(self):
      self.graph = defaultdict(list) 

   def addEdge(self,u,v):
      self.graph[u].append[v]

   def dfs(self):
      V = len(self.graph)         
      visited = [False]*(V)       
      for i in range(V):
        if visited[i] == False:    
           self.dfsUtil(i,visited)
           
   def __dfsUtil(self,v,visited):
       visited[v] = True
       print(v)
       for i in self.graph[v]:        
          if visited[i] == False: 
             self.dfsUtil(i,visited) 