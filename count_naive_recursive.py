def count_naive_recursive(C,G):
    G=[s for s in G]
    C=[s for s in C]
    return naive_recursive(G,C)

def naive_recursive(G,C):
    if len(G) < len(C): return 0
    if len(G)==1: 
        if len(C)==1 and C[0]==G[0]: 
            return 2
        return 0
    if len(C)==0 : return 0
    output=naive_recursive(G[0:len(G)-1],C)
    if G[-1]==C[0]: 
        if len(C)==1: output+= 2**(len(G)-1)
        else: output+=naive_recursive(G[0:len(G)-1],C[1:])
    if len(G)==len(C) and G[-1]==C[-1]: output+=naive_recursive(G[0:len(G)-1],C[0:len(C)-1])
    return output

print(count_naive_recursive('ACAC','ACACBCA'))
print(count_naive_recursive('ACAC','CACA'))
print(count_naive_recursive('ACABD','ACABDBCACA'))
print(count_naive_recursive('DBACA', 'ACABD'))
print(count_naive_recursive('AABBAA','BABAAA'))
print(count_naive_recursive('AABBAA','CHAABBAA'))