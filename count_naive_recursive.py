def count_naive_recursive(T:str, A:str):
    if 0 < len(T) and len(T) <= len(A):
        def naive_recursive(A,T):
            if len(A) < len(T): return 0
            if len(A)==1: 
                if len(T)==1 and T[0]==A[0]: return 2
                return 0
            if len(T)==0 : return 0
            output = naive_recursive(A[0:len(A)-1],T)
            if A[-1]==T[0]: 
                if len(T)==1: output += 2**(len(A)-1)
                else: output += naive_recursive(A[0:len(A)-1],T[1:])
            if len(A)==len(T) and A[-1]==T[-1]: output += naive_recursive(A[0:len(A)-1],T[0:len(T)-1])
            return output
        return naive_recursive(A,T)
    return 0



print(count_naive_recursive('ACAC','ACACBCA'))
print(count_naive_recursive('ACAC','CACA'))
print(count_naive_recursive('ACABD','ACABDBCACA'))
print(count_naive_recursive('DBACA', 'ACABD'))
print(count_naive_recursive('AABBAA','BABAAA'))
print(count_naive_recursive('AABBAA','CHAABBAA'))
print(count_naive_recursive('ACAB','BDACACBA'))