class Solution:
    def evalRPN(self, tokens):
        l = []
        fuhao = ['*','/','+','-']
        for i in tokens:
            if i in fuhao:
                a = l.pop()
                b = l.pop()
                if i != '/':
                    c = eval("(" + str(b)+ ")" + i +'('+ str(a) + ")")
                else:
                    c = eval("(" + str(b)+ ")" + "//" + '(' +str(a)+ ")")
                    d = eval("(" + str(b)+ ")" + "/" + '(' +str(a)+ ")")
                    if c < 0 and d != c:
                        c += 1
                l.append(c)
            else:
                l.append(i)
        return int(l[0])
        
