class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        x=y=1
        for _ in range(n-2):
            x,y = y,x+y
        return y