from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        arr = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr += nums1[i:]
        arr += nums2[j:]

        if len(arr)%2 == 0:
            return ( arr[ (len(arr)//2) - 1 ] + arr[len(arr)//2] ) / 2
        else:
            return float(arr[len(arr)//2])

s = Solution()
 
n1 = [1,3]
n2 = [2,7]
n3 = [1,2]
n4 = [3,4]
n5 = [1,3]
n6 = [2]

s.findMedianSortedArrays(n1, n2)
s.findMedianSortedArrays(n3, n4)
# s.findMedianSortedArrays(n5, n6)
