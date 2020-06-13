class Solution:
    def reversePairs(self, nums):
        self.times = 0

        def mergeSort(nums, left, right):
            if left > right or left == right:
                return
            if left == right - 1:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    self.times += 1
                return
            
            mid = left // 2 + right // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)

            l = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    l.append(nums[i])
                    i += 1
                else:
                    l.append(nums[j])
                    j += 1
                    self.times += mid + 1 - i
            if i <= mid:
                l.extend(nums[i : mid + 1])
            if j <= right:
                l.extend(nums[j : right + 1])
            nums[left : right + 1] = l

        mergeSort(nums, 0, len(nums) - 1)
        return self.times