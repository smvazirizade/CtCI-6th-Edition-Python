def Top_Down(N,Memo={1:1,2:2,3:4}):
    if N in Memo.keys():
        return Memo[N]
    else:
        Memo[N] = Top_Down(N-1,Memo)+Top_Down(N-2,Memo)+Top_Down(N-3,Memo)+6
        return Memo[N]
        
        
        
def Bottom_Up(N):
    a=1
    b=2
    c=4
    
    if N==1:
        return a
    if N==2:
        return b
    if N==3:
        return c
    if N>3:
        for i in range(4,N+1):
            d=(a+1)+(b+2)+(c+3)
            a=b
            b=c
            c=d
        return d
    
N=100
Bottom_Up(N)
Top_Down(N)



test_cases = (
    # list, k, expected
    (1,1),
    (2,2),
    (3,4),
    (10,586),
    (100,387658708225608851984856077))


Method_cases=[Top_Down,Bottom_Up]

#Method_cases=[kth_to_last_recursive]

def Triple_Steps():
    for Method in Method_cases:
        for N,expected in test_cases:
            assert Method(N) == expected


if __name__ == "__main__":
    Triple_Steps()
