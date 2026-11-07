class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #difference between a tree and a graph is that all nodes of tree are connected and there is no cycle. so we just check the cycle detection in a undirected graph. 
#cycle detection in undirected graph is: if we find parent, we don't call dfs for parent. else anything in visited comes again, we return false
        adj_list = defaultdict(list)
        for v, e in edges:
            adj_list[v].append(e)
            adj_list[e].append(v)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj_list[node]:
                if nei != parent: #only for non parent
                   if dfs(nei, node) == False:
                    return False
            return True

        if dfs(0,-1) == False:
            return False #we assume 0 is the main root but it won't matter since this is undirected 1-0 or 0-1 is the same. 
        return len(visited) == n
            