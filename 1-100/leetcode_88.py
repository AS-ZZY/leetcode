class Solution:
    def merge(self, nums1, m: int, nums2, n):
        alllen = m + n
        for i in range(alllen, -1, -1):
            if m > 0 and n > 0:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
            elif m > 0:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
