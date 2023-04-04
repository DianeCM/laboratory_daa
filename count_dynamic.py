def count_dynamic(T:str, A:str):
    if len(T) > len(A): return 0
    dp=[ [ [0 for i in range(len(A))] for i in range(len(T))] for i in range(len(T)) ]
    i=len(T)-1
    while i>=0:
        for j in range(i,len(T)):
            for k in range(len(A)):
                m=j-i
                if m > k:
                    dp[i][j][k]=0
                    continue
                if k==0:
                    if A[0] == T[i]: dp[i][j][k]=2
                    else: dp[i][j][k]=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                    continue
                if k >0 : dp[i][j][k]=dp[i][j][k-1]
                if A[k] == T[i]:
                    if m==0: dp[i][j][k]+=2**k
                    elif i<len(T)-1 and k>0: dp[i][j][k]+=dp[i+1][j][k-1]
                if k==m and A[k] == T[j] and j>0 and k>0: dp[i][j][k]+=dp[i][j-1][k-1]
        i-=1
    return dp[0][len(T)-1][len(A)-1]


print(count_dynamic('ACAC','ACACBCA'))
print(count_dynamic('ACAC','CACA'))
print(count_dynamic('ACABD','ACABDBCACA'))
print(count_dynamic('DBACA', 'ACABD'))
print(count_dynamic('AABBAA','BABAAA'))
print(count_dynamic('AABBAA','CHAABBAA'))
print(count_dynamic('ACAB','BDACACBA'))