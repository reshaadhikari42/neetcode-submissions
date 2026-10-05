class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        On a first glance, this seems to be a cycle detection problem. Because a difference between a graph and a tree is that tree doesn't have cycle.
        what else is the diff between them?
        so no, to be a tree, all nodes must be connected
        KEY IDEA: diff betwn graph and tree is that trees have no loops and all nodes are connected

        so we use the cycle detection and count total of visited nodes. if n == len(visited) all nodes are connected
        for cycle detection, we need to do dfs but also keep count of parent node for UNDIRECTED graphs.
        we call dfs on all neighbours EXCEPT the parent node
        '''
        adj_list = defaultdict(list)
        visited = set()
        for v,e in edges:
            adj_list[v].append(e)
            adj_list[e].append(v) #its undirected so goes both ways

        def dfs(vertex, parent):
            if vertex in visited:
                return False
            visited.add(vertex)
            for nei in adj_list[vertex]:
                if nei != parent: #don't call the parent
                    if dfs(nei, vertex) == False:
                        return False
            return True

        res = dfs(0, -1)
        if res == False:
            return res
        return len(visited) == n  #to see if all are connected

        #Time is O(V+E) and space is O(V+E)