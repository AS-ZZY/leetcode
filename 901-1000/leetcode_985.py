class Solution:
    def sumEvenAfterQueries(self, A, queries):
        l = [sum([ i for i in A if i % 2 == 0 ])]
        for i in queries:
            sums = l[-1]
            if A[i[1]] % 2 == 0:
                sums -= A[i[1]]
            A[i[1]] += i[0]
            if A[i[1]] % 2 == 0:
                sums += A[i[1]]
            l.append(sums)
        return l[1:]