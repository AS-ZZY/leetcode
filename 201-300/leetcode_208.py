class Nodelist:
    def __init__(self, x):
        self.letter = x
        self.next = ["", []]


class Trie:
    def __init__(self):
        self.start = Nodelist(' ')

    def insert(self, word: str):
        p = self.start
        for i in word:
            index = p.next[0].find(i)
            if index >= 0:
                p = p.next[1][index]
            else:
                p.next[0] += i
                q = Nodelist(i)
                p.next[1].append(q)
                p = q
        index = p.next[0].find("%")
        if index == -1:
            p.next[0] += "%"
            q = Nodelist("%")
            p.next[1].append(q)
                

        

    def search(self, word: str):
        p = self.start
        for i in word:
            index = p.next[0].find(i)
            if index == -1:
                return False
            else:
                p = p.next[1][index]
        if p.next[0].find("%") == -1:
            return False
        return True
        

    def startsWith(self, prefix: str):
        p = self.start
        for i in prefix:
            index = p.next[0].find(i)
            if index == -1:
                return False
            else:
                p = p.next[1][index]
        return True
