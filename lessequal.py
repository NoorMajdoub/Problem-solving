n, k = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()

if k == 0:
    if elements[0] > 1:
        print(elements[0] - 1)
    else:
        print(-1)
elif k == n:
    print(elements[-1])
else:
    if elements[k-1] < elements[k]:
        print(elements[k-1])
    else:
        print(-1)
