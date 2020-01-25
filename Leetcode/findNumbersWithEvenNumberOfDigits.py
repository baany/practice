from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for item in nums:
            if len(list(str(item)))%2 == 0:
                count = count+1
        return count

objSol = Solution()
print(objSol.findNumbers([12,123,12345,1234,1234546,7162537612]))
