class Solution:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		i = 0
		j = len(A) - 1
		while i < j:
			if A[i] % 2 == 0:
				i += 1
			else:
				a = A[i]
				A[i] = A[j]
				A[j] = a
				j -= 1
		return A