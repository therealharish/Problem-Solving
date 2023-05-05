class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        if not edges:
            return 0

        subtreeHasApple = [False for i in range(len(hasApple))]

        def populateSubTreeHasApple(v, parent, d, subtreeHasApple):
            subtreeHasApple[v] = hasApple[v]
            for neigh in d[v]:
                if neigh == parent:
                    continue
                populateSubTreeHasApple(neigh, v, d, subtreeHasApple)
                subtreeHasApple[v] = subtreeHasApple[v] or subtreeHasApple[neigh]

        def solve(v, parent, d, subTreeHasApple):
            cost = 0
            for neigh in d[v]:
                print(neigh, parent)
                if neigh == parent:
                    continue
                if subTreeHasApple[neigh]:
                    cost += 2 + solve(neigh, v, d, subTreeHasApple)
            return cost
                
        d = {}
        for edge in edges:
            if edge[0] not in d:
                d[edge[0]] = []
            if edge[1] not in d:
                d[edge[1]] = []
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        populateSubTreeHasApple(0, -1, d, subtreeHasApple)
        print(subtreeHasApple)
        return solve(0, -1, d, subtreeHasApple)

            