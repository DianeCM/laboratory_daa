def count_backtrack_memoize(T:str, A:str):
    if 0 < len(T) and len(T) <= len(A):
        memoize = {}
        
        def backtrack(T:str, A:str, index:int, S:str):
            if len(A) == index:
                if T == S[0:len(T)]:return 1
                return 0

            char = A[index]
            dict_str = A[index+1:len(A)]
            word_form = char + S
            if dict_str in memoize and word_form in memoize[dict_str]: 
                cant = memoize[dict_str][word_form]
            else: 
                cant = backtrack(T, A, index+1, word_form)
                memoize[dict_str] = {word_form : cant}
            
            word_form = S + char
            if dict_str in memoize and word_form in memoize[dict_str]: 
                cant += memoize[dict_str][word_form]
            else:
                cant2 = backtrack(T, A, index+1, word_form)
                memoize[dict_str] = {word_form : cant2}
                cant += cant2

            return cant
        return backtrack(T, A, 0, "")
    return 0

print(count_backtrack_memoize('ACAC','ACACBCA'))
print(count_backtrack_memoize('ACAC','CACA'))
print(count_backtrack_memoize('ACABD','ACABDBCACA'))
print(count_backtrack_memoize('DBACA', 'ACABD'))
print(count_backtrack_memoize('AABBAA','BABAAA'))
print(count_backtrack_memoize('AABBAA','CHAABBAA'))
print(count_backtrack_memoize('ACAB','BDACACBA'))