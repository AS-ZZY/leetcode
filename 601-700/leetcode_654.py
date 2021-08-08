class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maxIndex]:
                maxIndex = i
        root = TreeNode(nums[maxIndex])
        root.left = self.constructMaximumBinaryTree(nums[0:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        return root
