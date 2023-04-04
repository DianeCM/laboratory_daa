def count_naive_recursive(T:str, S:str):
    if 0 < len(T) and len(T) <= len(S):
        def naive_recursive(S,T):
            if len(S) < len(T): return 0
            if len(S)==1: 
                if len(T)==1 and T[0]==S[0]: return 2
                return 0
            if len(T)==0 : return 0
            output = naive_recursive(S[0:len(S)-1],T)
            if S[-1]==T[0]: 
                if len(T)==1: output += 2**(len(S)-1)
                else: output += naive_recursive(S[0:len(S)-1],T[1:])
            if len(S)==len(T) and S[-1]==T[-1]: output += naive_recursive(S[0:len(S)-1],T[0:len(T)-1])
            return output
        return naive_recursive(S,T)
    return 0



print(count_naive_recursive('ACAC','ACACBCA'))
print(count_naive_recursive('ACAC','CACA'))
print(count_naive_recursive('ACABD','ACABDBCACA'))
print(count_naive_recursive('DBACA', 'ACABD'))
print(count_naive_recursive('AABBAA','BABAAA'))
print(count_naive_recursive('AABBAA','CHAABBAA'))
print(count_naive_recursive('ACAB','BDACACBA'))