def count_backtrack(T:str, S:str):
    if 0 < len(T) and len(T) <= len(S):
        def backtrack(T:str, S:str, index:int, A:str):
            if len(S) == index:
                if T == A[0:len(T)]:return 1
                return 0
            char = S[index]
            cant = backtrack(T, S, index+1, char+A)
            cant += backtrack(T, S, index+1, A+char)
            return cant
        return backtrack(T, S, 0, "")
    return 0

print(count_backtrack('ACAC','ACACBCA'))
print(count_backtrack('ACAC','CACA'))
print(count_backtrack('ACABD','ACABDBCACA'))
print(count_backtrack('DBACA', 'ACABD'))
print(count_backtrack('AABBAA','BABAAA'))
print(count_backtrack('AABBAA','CHAABBAA'))
print(count_backtrack('ACAB','BDACACBA'))