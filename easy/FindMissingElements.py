'''You are given an integer array nums consisting of unique integers.

Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

The smallest and largest integers of the original range are still present in nums.

Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.
'''

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_nums = []
        nums.sort()

        start = nums[0]
        end = nums[-1]
        i = 0
        
        for num in range(start,end+1):
            if num == nums[i]:
                i += 1
                continue
            else:
                missing_nums.append(num)

        return missing_nums 
        
