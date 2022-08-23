class Node:
    def __init__(self, node_id, val=None):
        self.id = node_id
        self.val = None
        self.neighbors = []
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        

class Graph:
    def __init__(self,n):
        self.n =n
        self.storage = {}
        
        for i in range(1,n+1):
            node = Node(i)
            self.storage[i] = node
    
    def add_edges (self, edges_list):
        for pair in edges_list:
            n1,n2 = pair[0], pair[1]
            self.storage[n1].add_neighbor(n2)
            self.storage[n2].add_neighbor(n1)
        
    def print_contents(self):
        for k,v in self.storage.items():
            print(k, v.neighbors)
            
    def populate_graph(self):
        # flower_types = {1,2,3,4}
        queue = [i for i in range(1,self.n+1)]
        visited = {1}
        
        while queue:
            flower_types = {1,2,3,4}
            seen_flowers = set()
            curr_node = self.storage[queue.pop()]
            neighbors = curr_node.neighbors
            
            for node in neighbors:
                if node not in visited:
                    visited.add(node)
                    # queue.append(node)
                val = self.storage[node].val
                if val:
                    seen_flowers.add(val)
            if seen_flowers:
                for flower in seen_flowers:
                    flower_types.remove(flower)
                
            curr_node.val = list(flower_types)[0]
            # print(f'curr_node {curr_node.id}, = {curr_node.val}')
                
                
        

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        garden = Graph(n)
        garden.add_edges(paths)
        # garden.print_contents()
        garden.populate_graph()
        
        gardens_type = [garden.storage[node].val for node in garden.storage]
        return gardens_type
        