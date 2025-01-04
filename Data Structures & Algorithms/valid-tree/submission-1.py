class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # solution 1 dfs
        if len(edges) != n-1:
            return False
        nodeMap = {i : [] for i in range(n)}
        for node1,node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)
        visited = set()
        # def dfs(node, parent):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for i in nodeMap[node]:
        #         if i == parent:
        #             continue
        #         if dfs(i,node) == False:
        #             return False
        #     visited.remove(node)
        #     return True
        # return dfs(0,-1)
        # solution 2 bfs
        q = deque()
        q.append((0,-1))
        while q:
            cur =  q.popleft()
            node,parent = cur[0], cur[1]
            if node in visited:
                return False
            visited.add(node)
            for i in nodeMap[node]:
                if i == parent:
                    continue
                q.append((i,node))
        if len(visited) == n:
            return True
        return False        
        # solution 3 disjoint set union

        