def count_first_memoize(T,S):
    dp=[[[-1 for i in range(len(S))] for i in range(len(T))]for i in range(len(T))]
    return count_memoize(0,len(T)-1,len(S)-1,T,S,dp)

def count_memoize(p:int, q:int, k:int,T:str,S:str,dp):
    if dp[p][q][k]>=0: return dp[p][q][k]
    count = 0
    m=q-p+1
    for i, elem in enumerate(S[0:k+1]):
        if elem == T[p]:
            if m == 1:
                if i == 0: count+=2
                else: count += 2**i
            elif i > 0 and i >= m-1: count += count_memoize(p+1,q,i-1,T,S,dp)
            elif i > 0 and i < m-1 and T[p+i+1:q+1] == S[i+1:m]: count += count_memoize(p+1,p+i,i-1,T,S,dp)
            elif i == 0 and T[p+1:q+1] == S[1:m]: count += 2
    dp[p][q][k]=count
    return count

print(count_first_memoize('ACAC','ACACBCA'))
print(count_first_memoize('ACAC','CACA'))
print(count_first_memoize('ACABD','ACABDBCACA'))
print(count_first_memoize('DBACA', 'ACABD'))
print(count_first_memoize('AABBAA','BABAAA'))
print(count_first_memoize('AABBAA','CHAABBAA'))
print(count_first_memoize('ACAB','BDACACBA'))