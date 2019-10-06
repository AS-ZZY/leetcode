class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        minL = chr(ord("z") + 1)
        biggerL = chr(ord("z") + 1) 
        for i in letters:
            if ord(biggerL) > ord(i) and ord(i) > ord(target):
                biggerL = i
            elif ord(minL) > ord(i):
                minL = i
        if ord(biggerL) == ord("z") + 1:
            return minL
        return biggerL
