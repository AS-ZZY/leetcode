class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        frist = -1
        end = False
        for i in range(len(A)):
            if A[i] != B[i]:
                if not end:
                    if frist == -1:
                        frist = i
                    else:
                        if A[frist] == B[i] and A[i] == B[frist]:
                            end = True
                        else:
                            return False
                else:
                    return False
        if end or (frist == -1 and len(A) > len(set(list(A)))):
            return True
        return False
