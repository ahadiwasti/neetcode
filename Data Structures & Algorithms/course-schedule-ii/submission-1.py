class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)

        for c,p in prerequisites:
            graph[c].append(p)
        visiting, visited = set(),set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True


            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)

            res.append(course)

            return True

        for cc in range(numCourses):
            if not dfs(cc):
                return []
        return res