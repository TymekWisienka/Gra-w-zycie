from random import randint

plansza = []
n = 10
for i in range(0, n):
    plansza.append([])
    for j in range(0, n):
        plansza[i].append(randint(0, 1))

print(*plansza, sep="\n")

def sprawdzanie(x, y):
    zywe = 0
    for i in range(x-1, x+1):
        for j in range(y-1, y+1):
            zywe += plansza[i][j]
    if zywe == 3 or (zywe == 2 and plansza[x][y] == 1):
        return 1
    return 0

print(sprawdzanie(1, 1))