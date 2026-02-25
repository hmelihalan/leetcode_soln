'''Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1. '''

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky_numbers =[]
        
        for num, count in freq.items():
            if num == count:
                lucky_numbers.append(num)
                
        if lucky_numbers == []:
            return -1
        return max(lucky_numbers)
