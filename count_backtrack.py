def count_backtrack(T:str, A:str):
    if 0 < len(T) and len(T) <= len(A):
        def backtrack(T:str, A:str, index:int, S:str):
            if len(A) == index:
                if T == S[0:len(T)]:return 1
                return 0
    
            char = A[index]
            cant = backtrack(T, A, index+1, char+S)
            cant += backtrack(T, A, index+1, S+char)
            return cant
        return backtrack(T, A, 0, "")
    return 0

print(count_backtrack('ACAC','ACACBCA'))
print(count_backtrack('ACAC','CACA'))
print(count_backtrack('ACABD','ACABDBCACA'))
print(count_backtrack('DBACA', 'ACABD'))
print(count_backtrack('AABBAA','BABAAA'))
print(count_backtrack('AABBAA','CHAABBAA'))
print(count_backtrack('ACAB','BDACACBA'))