nb = 5
for r in range(nb):
    row = list(map(int, input().split()))
    for m in range(n):
        if row[m] == 1:
            moves = abs(r-2) +abs(m-2)
            print(moves)
            break  #you quit cause found it already enti
