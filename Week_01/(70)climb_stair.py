class Solution:
    def climbStairs(self, n: int) -> int:

        f0, f1 = 0, 1

        for _ in range(n):
            fn = f0 + f1
            f0 = f1
            f1 = fn

        return fn
