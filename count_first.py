def count_first(T:str, S:str):
    count = 0
    for i, elem in enumerate(S):
        if elem == T[0]:
            if len(T) == 1:
                if i == 0: count+=2
                else: count += 2**i
            elif i > 0 and i >= len(T)-1: count += count_first(T[1:], S[0:i])
            elif i > 0 and i < len(T)-1 and T[i+1:] == S[i+1:len(T)]: count += count_first(T[1:i+1], S[0:i])
            elif i == 0 and T[1:] == S[1:len(T)]: count += 2
    return count

print(count_first('ACAC','ACACBCA'))
print(count_first('ACAC','CACA'))
print(count_first('ACABD','ACABDBCACA'))
print(count_first('DBACA', 'ACABD'))
print(count_first('AABBAA','BABAAA'))
print(count_first('AABBAA','CHAABBAA'))
print(count_first('ACAB','BDACACBA'))