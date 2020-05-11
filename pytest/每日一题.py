print('---x的平方根---')
print('牛顿迭代法')
class Solution:
    def mySqrt(self,x:int)->int:
        if x == 0:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5*(x0+C/x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)
mysq = Solution()
print(mysq.mySqrt(8))













