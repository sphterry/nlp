
# DP approach to minimum edit distance
# Using variable names from algorithm in L2
def minEditDistance(v: str, w: str) -> int:
    # memoization technique
    cache = {}
    m, n = len(v), len(w)

    # where i is the index into word1 and j is the index into word2
    def dist(i, j):
        if (i, j) in cache:
            return cache[(i, j)]

        if i not in range(m):
            return n - j

        if j not in range(n):
            return m - i

        if v[i] == w[j]:
            # no change needed
            cache[(i, j)] = dist(i + 1, j + 1)
            return cache[(i, j)] 

        delete = dist(i + 1, j)
        insert = dist(i, j + 1)
        replace = dist(i + 1, j + 1)
        
        res = min(replace, min(delete, insert)) # pick min of all three

        cache[(i,j)] = 1 + res

        return cache[(i,j)]
    
    return dist(0, 0)

print(minEditDistance("intention", "execution"))
print(minEditDistance("fast", "cats"))