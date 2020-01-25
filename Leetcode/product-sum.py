from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        n = list(str(n))
        for item in n:
            prod = prod*int(item)
        for item in n:
            sums = sums+int(item)
        return prod-sums

objSol = Solution()
print(objSol.subtractProductAndSum(343))
