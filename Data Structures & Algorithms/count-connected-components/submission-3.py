class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union find with rank and path compression
        rank = [0] * n
        parent = [i for i in range(n)]
        count = n

        def findParent(a):
            if parent[a] != a:
                parent[a] = findParent(parent[a])
            return parent[a]

        def union(a, b):
            nonlocal count
            parentA = findParent(a)
            parentB = findParent(b)
            if parentA == parentB:
                return
            
            if rank[parentA] > rank[parentB]:
                parent[parentB] = parentA
            elif rank[parentB] > rank[parentA]:
                parent[parentA] = parentB
            else: #equal
                parent[parentB] = parentA
                rank[parentA] += 1
            count -=1


        for v,e in edges:
            union(v, e)

        return count