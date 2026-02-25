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
        
