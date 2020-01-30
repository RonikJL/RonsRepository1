import math
from _ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        middle = len(nums) / 2
        median = 0
        if (len(nums) % 2 == 0):
            med1 = nums[math.floor(middle) - 1]
            med2 = nums[math.floor(middle)]
            median = (med1 + med2) / 2
        else:
            median = nums[math.floor(middle)]

        return float(median)
