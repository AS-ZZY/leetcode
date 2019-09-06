class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while True:
            middle = (end + start) // 2
            if start == end:
                return nums[end]
            if start == end -1:
                return min(nums[start], nums[end])
            if nums[middle] < nums[end]:
                end = middle
            elif nums[middle] > nums[end]:
                start = middle
            else:
                if nums[start] < nums[middle]:
                    end = middle
                elif nums[start] > nums[middle]:
                    start = middle
                else:
                    return min(self.findMin(nums[:middle]), self.findMin(nums[middle:]))
