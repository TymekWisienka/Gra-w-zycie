from random import randint
import os, time, pygame



n = 100
ksztalt = ["010","001","111"]

plansza = []

#PLANSZA LOSOWA
'''
for i in range(0, n):
    plansza.append([])
    for j in range(0, n):
        plansza[i].append(randint(0, 1))
'''

#PLANSZA PUSTA
for i in range(0, n):
    plansza.append([])
    for j in range(0, n):
        plansza[i].append(0)

#print(*plansza, sep="\n")

def dodaj_ksztalt(ksztalt,x,y):
    global plansza
    for i, wiersz in enumerate(ksztalt):
        for j, komorka in enumerate(wiersz):
            plansza[x+i][y+j] = int(komorka)

    #print(plansza)
dodaj_ksztalt(ksztalt, 2, 2)

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

'''

def gra():
    global plansza
    run = True
    while run:

        clock.tick(60)
        fps = clock.get_fps()

        nowa_generacja()


        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                run = False
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if evt.button == 3:
                    mysz = pygame.mouse.get_pos()
                    #print(mysz)
                    dodaj_ksztalt(ksztalt, mysz[1]//rozmiar_komorki - 1, mysz[0]//rozmiar_komorki - 1)
                if evt.button == 1:
                    mysz = pygame.mouse.get_pos()
                    #print(mysz)
                    dodaj_ksztalt([i[::-1] for i in ksztalt[::-1]], mysz[1] // rozmiar_komorki - 1, mysz[0] // rozmiar_komorki - 1)

        rysowanie()



def gra_reczna():
    global plansza
    run = True
    clock.tick(60)
    fps = clock.get_fps()


    while run:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                run = False
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if evt.button == 4:
                    nowa_generacja()
                    rysowanie()
                if evt.button == 3:
                    mysz = pygame.mouse.get_pos()
                    # print(mysz)
                    dodaj_ksztalt(ksztalt, mysz[1] // rozmiar_komorki - 1, mysz[0] // rozmiar_komorki - 1)
                if evt.button == 1:
                    mysz = pygame.mouse.get_pos()
                    # print(mysz)
                    dodaj_ksztalt([i[::-1] for i in ksztalt[::-1]], mysz[1] // rozmiar_komorki - 1,
                                  mysz[0] // rozmiar_komorki - 1)

    rysowanie()

run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        gra()
    else:
        gra_reczna()


'''

run = True
auto = False  # czy automatyczna gra

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Dodawanie kształtów myszką
        if event.type == pygame.MOUSEBUTTONDOWN:
            mysz = pygame.mouse.get_pos()
            x = mysz[1] // rozmiar_komorki - 1
            y = mysz[0] // rozmiar_komorki - 1
            if event.button == 3:
                dodaj_ksztalt(ksztalt, x, y)
            if event.button == 1:
                dodaj_ksztalt([i[::-1] for i in ksztalt[::-1]], x, y)

            #DODAĆ WIĘCEJ KRZTAŁTÓW POD RÓŻNYMI KLAWISZAMI

            # Scroll w trybie ręcznym
            if event.button == 4 and not auto:
                nowa_generacja()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                auto = not auto

    clock.tick(60)

    if auto:
        nowa_generacja()

    rysowanie()
