class Solution:
	def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
		i = 0
		l = []

		while True:
			try:
				a = x ** i
			except:
				a = 0
			if a > bound:
				break
			j = 0
			while True:
				try:
					b = a + y ** j
				except:
					b = a + 0
				if b > bound:
					break
				else:
					l.append(b)
				j += 1
				if y == 1 or y == 0:
					break
			i += 1
			if x == 1 or x == 0:
				break

		return list(set(l))