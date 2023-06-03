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
            # print(curr_node.val)
            
            if curr_node.val not in graph:
                curr_copy = Node(curr_node.val)
                graph[curr_node.val] = curr_copy
            else:
                curr_copy = graph[curr_node.val]
                
            # visited.add(curr_node.val)
            
            # print(node.val, node.neighbors)
            for n in curr_node.neighbors:
                # print(n.val)
                
                if n.val not in graph:
                    n_copy = Node(n.val)
                    graph[n.val] = n_copy
                else:
                    n_copy = graph[n.val]
               
                curr_copy.neighbors.append(n_copy)
                if n.val not in visited:
                    stack.append(n)
                    visited.add(n.val)
                
        
#         print(visited)
#         for k,v in graph.items():
#             print(v.val,v.neighbors)
        
        return graph[1]