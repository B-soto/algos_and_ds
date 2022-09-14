# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def bfs_to_k(some_graph, k, target):
            this_level = [target]
            visited = set()
            visited.add(target)
            level = 0
            while this_level:
                if level == k:
                    return this_level
                next_level = []

                for node in this_level:
                    neighbors = some_graph[node]
                    for n in neighbors: #[1,7,4]
                        if n not in visited:
                            next_level.append(n)
                            visited.add(n)

                level +=1
                this_level = next_level
            return []
        def my_graph(root):
            graph = {}
            q = [root]

            while q:
                curr = q.pop(0)
                if curr.val not in graph:
                    graph[curr.val] = []
                if curr.left:
                    q.append(curr.left)
                    graph[curr.val].append(curr.left.val)
                    if curr.left.val not in graph:
                        graph[curr.left.val] = [curr.val]

                if curr.right:
                    q.append(curr.right)
                    graph[curr.val].append(curr.right.val)
                    if curr.right.val not in graph:
                        graph[curr.right.val] = [curr.val]
            return graph
        
        g = my_graph(root)
        # print(g)
        # print(k,target.val)
        # print(bfs_to_k(g,k,target.val))
        return bfs_to_k(g,k,target.val)
        
        

        
