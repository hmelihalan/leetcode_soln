'''You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(val, i) for i, val in enumerate(nums)]
        
        arr.sort(key=lambda x: x[0], reverse=True)
        topk = arr[:k]
        
        topk.sort(key=lambda x: x[1])
        return [val for val, _ in topk]
