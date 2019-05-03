class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        ll = []
        for i in l:
            if i == "" or i == "." or (i == ".." and len(ll) == 0):
                pass
            elif i== '..':
                ll.pop()
            else:
                ll.append(i)
        s = ""
        for i in ll:
            s = s + '/' + i
        if s == "":
            return "/"
        return s
