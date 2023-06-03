"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        graph = {}
        
        
        
        stack = [node]
        visited = set()
        visited.add(node.val)
        
        while stack:
            
            curr_node = stack.pop()
            
            
            if curr_node.val not in graph:
                graph[curr_node.val] = Node(curr_node.val)
            
            curr_copy = graph[curr_node.val]
                

            for n in curr_node.neighbors:
                
                if n.val not in graph:
                    graph[n.val] = Node(n.val)
                
                n_copy = graph[n.val]
               
                curr_copy.neighbors.append(n_copy)
                if n.val not in visited:
                    stack.append(n)
                    visited.add(n.val)

        
        return graph[1]