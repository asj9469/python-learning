# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#       Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#       Return k.
#
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#
# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.

####################################################
# My Approach
# Runtime 34 ms
# Beats 87.55% of users with Python3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[l] != val:
                l+=1
                continue
            if nums[r] != val:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l+=1

        return l

####################################################
# NeetCode Optimized Approach
# Using partition method to bring all the non vals to the front
# 34 ms | beats 87% of users with Python 3
# 17.30 MB | beats 18% of users with Pyhton 3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k
