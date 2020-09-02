class Solution:
    def invalidTransactions(self, transactions):
        for i in range(len(transactions)):
            transactions[i] = transactions[i].split(",")
        transactions.sort(key = lambda x:int(x[1]))
        out = []
        for i in range(len(transactions)):
            for j in range(i + 1,len(transactions)):
                if int(transactions[j][1]) - int(transactions[i][1]) > 60:
                    break
                if transactions[i][0] == transactions[j][0] and transactions[i][3] != transactions[j][3]:
                    out.extend([i, j])
            if int(transactions[i][2]) > 1000:
                out.append(i)
        out = list(set(out))
        for i in range(len(out)):
            s = ""
            for j in transactions[out[i]]:
                s += j + ","
            out[i] = s[:-1]
        return out