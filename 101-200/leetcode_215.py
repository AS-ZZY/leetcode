class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = sorted(nums, reverse = True)
        return a[k - 1] 
