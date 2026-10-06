class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        This seems to be union find question.
        we are going to do union find with rank for this
        we don't need adjacency list either. edges can do union find better
        everything starts as a single disconnected node. so we start with count = n and decrement it as we do union.

        union find by rank uses O(log n) as hieght is strictly capped and shorter trees are added to long trees. 
        Path compression would make it NEARLY O(1) but we are not doing that. rank is enough.

        if we don't even use rank, its going to be O(n).
        '''
        def find(vertex):  #finding parent of node
            if parent[vertex] != vertex:
                return find(parent[vertex])
            else:
                return vertex

        def union(a, b):
            nonlocal count
            parentA = find(a)
            parentB = find(b)
            if parentA == parentB:
                return

            if rank[parentA] > rank[parentB]:
                parent[parentB] = parentA
            elif rank[parentB] > rank[parentA]:
                parent[parentA] = parentB
            else: #both ranks equal
                parent[parentB] = parentA #anything
                rank[parentA] += 1
            count -= 1

        count = n  #starts with n different nodes and then goes down as we connect
        rank = [0]*n
        parent = [i for i in range(n)]
        for v,e in edges:
            parentV = find(v)
            parentE = find(e)
            union(v,e)
        return count

