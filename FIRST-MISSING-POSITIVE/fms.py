from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hs = set(nums)
        sm = 1
        while sm in hs:
            sm += 1
        return sm

s = Solution()

print(f"Input: [1,2,0], Output: {s.firstMissingPositive([1,2,0])}")
# Expected: 2
print(f"Input: [3,4,-1,1], Output: {s.firstMissingPositive([3,4,-1,1])}")
# Expected: 1
print(f"Input: [7,8,9,11,12], Output: {s.firstMissingPositive([7,8,9,11,12])}")