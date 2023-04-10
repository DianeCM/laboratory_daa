def count_square_dynamic(T:str, S:str):
    m = len(T)
    n = len(S)
    if m > n: return 0

    dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
    for i in range(n):
        if i >= m or T[i] == S[0]: dp[i][i] = 2
    
    for k in range(1, len(S)):    
        c = S[k]
        i = 0        
        for j in range(k, n):
            if i >= m or c == T[i]:
                dp[i][j] += dp[i+1][j]
            if j >= m or c == T[j]:
                dp[i][j] += dp[i][j-1]            
            i += 1            
    return dp[0][-1]

print(count_square_dynamic('ACAC','ACACBCA'))
print(count_square_dynamic('ACAC','CACA'))
print(count_square_dynamic('ACABD','ACABDBCACA'))
print(count_square_dynamic('DBACA', 'ACABD'))
print(count_square_dynamic('AABBAA','BABAAA'))
print(count_square_dynamic('AABBAA','CHAABBAA'))
print(count_square_dynamic('ACAB','BDACACBA'))