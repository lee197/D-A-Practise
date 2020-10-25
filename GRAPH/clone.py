import deque

class Node:
  def __init__(self, val, neighbours):
    self.val = val
    self.neighbours = neighbours

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue=deque([node])
        head=Node(node.val,[])
        visited={ node:head }

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in visited:
                    visited[node].neighbors.append(visited[neighbor])
                else:
                    queue.append(neighbor)
                    copy=Node(neighbor.val,[])
                    visited[neighbor]=copy
                    visited[node].neighbors.append(copy)                    
        return head