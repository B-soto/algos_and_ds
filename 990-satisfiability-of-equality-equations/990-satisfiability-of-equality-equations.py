from collections import deque
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def bfs_path_exists(graph, root, target):
            q = deque()
            q.append(root)
            visited = {root}
            
            while q:
                curr = q.popleft()
                print(curr)
                if curr == target:
                    return True
                neighbors = graph[curr]
                for n in neighbors:
                    if n not in visited:
                        
                        q.append(n)
                        visited.add(n)
            return False
            
        positive = []
        negative = []
        equality_dict = {}
        
        for pair in equations:
            if '!' == pair[1]:
                negative.append(pair)
            else:
                positive.append(pair)
        
        
        for pair in positive:
            x1, x2 = pair[0], pair[3]
            
            if x1 in equality_dict:
                equality_dict[x1].append(x2)
            else:
                equality_dict[x1] = [x2]
                
            if x2 in equality_dict:
                equality_dict[x2].append(x1)
            else:
                equality_dict[x2] = [x1]
                
        
        for pair in negative:
            x1, x2 = pair[0], pair[3]
            
            if x1 == x2:
                return False
            
            if x1 not in equality_dict or x2 not in equality_dict :
                continue
            
            if bfs_path_exists(equality_dict, x1, x2):
                return False
            
        return True
            
            
        
        
        

        