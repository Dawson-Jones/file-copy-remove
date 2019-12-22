class Solution:
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)


s = Solution()
res = s.climb_stairs(10)
print(res)
