
k,n,w=list(map(int, input().split()))
val=n-(sum([i*k for i in range(1,w+1)]))
if val<0:
    print( abs(n-(sum([i*k for i in range(1,w+1)]))))
else:
    print(0)
