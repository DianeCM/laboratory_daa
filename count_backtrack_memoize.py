def count_backtrack_memoize(T:str, S:str):
    if 0 < len(T) and len(T) <= len(S):
        memoize = {}
        def backtrack(T:str, S:str, index:int, A:str):
            if len(S) == index:
                if T == A[0:len(T)]:return 1
                return 0
            char = S[index]
            dict_str = S[index+1:len(S)]
            word_form = char + A
            if dict_str in memoize and word_form in memoize[dict_str]: 
                cant = memoize[dict_str][word_form]
            else: 
                cant = backtrack(T, S, index+1, word_form)
                memoize[dict_str] = {word_form : cant}
            word_form = A + char
            if dict_str in memoize and word_form in memoize[dict_str]: 
                cant += memoize[dict_str][word_form]
            else:
                cant2 = backtrack(T, S, index+1, word_form)
                memoize[dict_str] = {word_form : cant2}
                cant += cant2
            return cant
        return backtrack(T, S, 0, "")
    return 0

print(count_backtrack_memoize('ACAC','ACACBCA'))
print(count_backtrack_memoize('ACAC','CACA'))
print(count_backtrack_memoize('ACABD','ACABDBCACA'))
print(count_backtrack_memoize('DBACA', 'ACABD'))
print(count_backtrack_memoize('AABBAA','BABAAA'))
print(count_backtrack_memoize('AABBAA','CHAABBAA'))
print(count_backtrack_memoize('ACAB','BDACACBA'))