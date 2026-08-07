class Solution:
    def integerBreak(self,n):
        seen = {1:1}
        def dfs(num):
            if num in seen:
                return seen[num]

            seen[num] = 0 if num == n else num
            for i in range(1,num):
                val = dfs(i)*dfs(num-i)
                seen[num] = max(val,seen[num])
            
            return seen[n]

        
        return dfs(n)