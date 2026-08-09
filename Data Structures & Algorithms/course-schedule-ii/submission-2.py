class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        coursegraph = defaultdict(list)

        for c,p in prerequisites:
            coursegraph[c].append(p)

        visited,visiting = set(),set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for pre in coursegraph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)

            res.append(course)
            return True

        for cour in range(numCourses):
            if not dfs(cour):
                return []
        return res