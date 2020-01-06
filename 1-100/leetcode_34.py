class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		
		l = [ -1, -1 ]
		front = 0
		end = len(nums) - 1
		
		while front <= end:
			mid = (front + end) // 2
			if nums[mid] == target:
				l1 = self.searchRange(nums[front:mid], target)
				l2 = self.searchRange(nums[mid + 1:end + 1], target)
				
				if l1[0] == -1:
					l[0] = mid
				else:
					l[0] = l1[0] + front
				
				if l2[1] == -1:
					l[1] = mid
				else:
					l[1] = l2[1] + mid + 1
				
				break

			elif nums[mid] < target:
				front = mid + 1
			else:
				end = mid - 1

		return l