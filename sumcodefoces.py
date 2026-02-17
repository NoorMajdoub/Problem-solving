tt = int(input())
for _ in range(tt):  #nafess el faza ta3 el map ta3 el liste
    a,b,c = map(int, input().split())
    print("YES" if a+b ==c or a+c == b or b+c == a else "NO")
