
def triple_hop(x):
    #Recursive and no memozation
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)




def Top_Down_List(N,Memo=None):
    #Dynamic programing with memozation using list and for loop
    if N<0:
        return 0
    if Memo is None:
        Memo=[-1]*(N+1)
        if N>=0:
            Memo[0]=1
        if N>=1:
            Memo[1]=1
        if N>=2:
            Memo[2]=2
    for i in range(3,N+1):
        Memo[i] = Memo[i-1] + Memo[i-2] + Memo[i-3]
    return Memo[N]
        


def Top_Down_Dict(N,Memo={0:1,1:1,2:2}):
    #Dynamic programing with memozation using dictionary and recursion
    if N<0:
        return 0
    if N in Memo.keys():
        return Memo[N]
    else:
        Memo[N] = Top_Down_Dict(N-1,Memo)+Top_Down_Dict(N-2,Memo)+Top_Down_Dict(N-3,Memo)
        return Memo[N]
        
        
        
def Bottom_Up(N):
    #Dynamic programing 
    a=1
    b=1
    c=2
    if N<0:
        return 0
    if N==0:
        return a
    if N==1:
        return b
    if N==2:
        return c
    if N>2:
        for i in range(3,N+1):
            d=a+b+c
            a=b
            b=c
            c=d
        return d
    
N=100
Bottom_Up(N)




test_cases = (
    # list, k, expected
    (1,1),
    (2,2),
    (3,4),
    (10,274))


Method_cases=[triple_hop,Top_Down_List,Top_Down_List, Top_Down_Dict,Bottom_Up]

#Method_cases=[kth_to_last_recursive]

def Triple_Steps():
    for Method in Method_cases:
        for N,expected in test_cases:
            print(N, Method(N))
            #assert Method(N) == expected


if __name__ == "__main__":
    Triple_Steps()
