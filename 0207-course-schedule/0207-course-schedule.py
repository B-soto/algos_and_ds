class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create our graph adjaetncy list
        # graph = { 0:[], 1:[] }
        graph = {i:[] for i in range(numCourses)}
        
        
        for a,b in prerequisites:
            graph[b].append(a)
            
        print(graph)
        seen = set()
        
        def dfs(node):
            #base Cases
            if graph[node] == []:
                return True
            if node in seen:
                print("Here", node)
                return False
            
            
            #iterative cases
            seen.add(node)
            for pre in graph[node]:
                if dfs(pre) == False:
                    return False
            seen.remove(node)
            graph[node] = []
            return True    
            
        for i in range(numCourses):
            
            if dfs(i) == False:
                return False
    
            
        return True
        
        
        
            
        
        
        
        
        
        
        
            
            