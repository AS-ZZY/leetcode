class Solution:
    def rotate(self, nums, k: int) -> None:
        nums[:] = nums[-k % len(nums): ] + nums[: -k % len(nums)] 
