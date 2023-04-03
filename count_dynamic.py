def count_dynamic(C,G):
    dp=[ [ [0 for i in range(len(G))] for i in range(len(C))] for i in range(len(C)) ]
    i=len(C)-1
    while i>=0:
        for j in range(i,len(C)):
            for k in range(len(G)):
                m=j-i
                if m > k:
                    dp[i][j][k]=0
                    continue
                if k==0:
                    if G[0] == C[i]: dp[i][j][k]=2
                    else: dp[i][j][k]=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                    continue
                if k >0 : dp[i][j][k]=dp[i][j][k-1]
                if G[k] == C[i]:
                    if m==0: dp[i][j][k]+=2**k
                    elif i<len(C)-1 and k>0: dp[i][j][k]+=dp[i+1][j][k-1]
                if k==m and G[k] == C[j] and j>0 and k>0: dp[i][j][k]+=dp[i][j-1][k-1]
        i-=1
    return dp[0][len(C)-1][len(G)-1]


print(count_dynamic('ACAC','ACACBCA'))
print(count_dynamic('ACAC','CACA'))
print(count_dynamic('ACABD','ACABDBCACA'))
print(count_dynamic('DBACA', 'ACABD'))
print(count_dynamic('AABBAA','BABAAA'))
print(count_dynamic('AABBAA','CHAABBAA'))