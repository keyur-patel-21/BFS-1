# Approach:
# The function `canFinish` checks if it's possible to complete all `numCourses` given the `prerequisites`.
# It constructs a prerequisite map `preMap` that maps each course to a list of courses it depends on.
# The `dfs` helper function performs a Depth-First Search to detect cycles in course dependencies.
# - If a course is already in `Visitset`, a cycle is detected, so we return `False`.
# - If a course has no prerequisites, it's marked as complete by setting `preMap[crs] = []`.
# - After visiting each prerequisite for a course, it's removed from `Visitset` to backtrack correctly.
# The function iterates over all courses and runs `dfs` to check each course independently.
# If any course cycle is detected, the function returns `False`; otherwise, it returns `True`.

# Time Complexity (TC): O(V + E), where V is the number of courses and E is the number of prerequisites.
# - This is because each course and its prerequisites are visited once in the DFS.

# Space Complexity (SC): O(V + E), due to the storage in `preMap` and `Visitset`.
# - `preMap` stores the adjacency list, and `Visitset` can hold up to `V` elements during recursion.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        Visitset = set()

        def dfs(crs):
            if crs in Visitset:
                return False
            if preMap[crs] == []:
                return True
            
            Visitset.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            Visitset.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
