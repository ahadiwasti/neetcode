class Solution:
    def integerBreak(self,n):
        seen={0:1}
        def dfs(num):
            if num in seen:
                return seen[num]

            seen[num] = 0 if num == n else num
            for i in range(num):
                val = dfs(i)*dfs(num-i)
                seen[num] = max(seen[num],val)

            return seen[num]

            


        return dfs(n)