from random import randint
import os, time, pygame

n = 200

plansza = []

for i in range(0, n):
    plansza.append([])
    for j in range(0, n):
        plansza[i].append(randint(0, 1))

#print(*plansza, sep="\n")

def sprawdzanie(x, y):
    zywe = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < n and 0 <= j < n:
                zywe += plansza[i][j]
    zywe -= plansza[x][y]
    if zywe == 3 or (zywe == 2 and plansza[x][y] == 1):
        return 1
    return 0

print(sprawdzanie(9, 9))

def nowa_generacja():
    global plansza
    nowa_plansza = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nowa_plansza[i][j] = sprawdzanie(i, j)
    plansza = nowa_plansza
'''
def symulacja(l_generacji):
    global plansza
    for gen in range(l_generacji):
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Generacja ", gen)
        for i in plansza:
            wiersz = ["#" if j == 1 else "." for j in i]
            print(' '.join(wiersz))

        nowa_generacja()

symulacja(50)
'''

# ------------- PYGAME -------------

#wymiary
komorki = n
wymiar = 800
rozmiar_komorki = wymiar // komorki

#kolory
kolor_zywy = (0, 150, 0)
kolor_martwy = (10, 10, 30)

pygame.init()

screen = pygame.display.set_mode((wymiar, wymiar))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

def rysowanie():
    global plansza
    screen.fill(kolor_martwy)


    for i in range(n):
        for j in range(n):
            if plansza[i][j] == 1:
                color = kolor_zywy
            else:
                color = kolor_martwy

            #kwadrat
            rect = pygame.Rect(j * rozmiar_komorki, i * rozmiar_komorki, rozmiar_komorki, rozmiar_komorki)
            pygame.draw.rect(screen, color, rect)


    pygame.display.flip()

def gra():
    while True:
        clock.tick(60)
        fps = clock.get_fps()
        print(fps)
        nowa_generacja()
        rysowanie()

gra()
