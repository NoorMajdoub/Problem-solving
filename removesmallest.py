
from collections import Counter
def arrit(arr):
    arr=sorted(arr)
    tracker=True
    i=1
    while i<len(arr) and tracker:
        if abs(arr[i]-arr[i-1])>1:
            tracker=False
            return "NO"
        i+=1
    return"YES"
    
n=int(input())
for _ in range(n):
    t=int(input())
    m=list(map(int, input().split()))
    print(arrit(m))
