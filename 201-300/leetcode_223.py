class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int):
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        if B > H or D < F or C < E or G < A:
            return s1 + s2
        length = abs(min(G, C) - max(A, E))
        width = abs(min(H, D) - max(B, F))
        return s1 + s2 - width * length