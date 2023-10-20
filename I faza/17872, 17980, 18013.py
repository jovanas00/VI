
def inputDim():
    m = int()
    n = int()
    ispravno = False
    while ispravno == False:
        m = int(input("Unesite broj vrsta table: "))
        n = int(input("Unesite broj kolona table: "))
        if m > 2 and n > 2 and m <= 26 and n <= 26:
            ispravno = True
        else:
            print("Nevalidne dimenzije!")
    return (m, n)

def pocetnoStanje(m, n):
    mat = list()
    for i in range(m):
        mat1 = list()
        for k in range(n):
            mat1.append(None)
        mat.append(mat1)
    return mat

# iksOks -> X = False, O = True
def valjanPotez(mat, iksOks: bool, x, y, m, n):
    if x < 0 or x >= 26:
        return False
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    else:
        provera = list()
        if iksOks == False:
            if x == 0:
                return False
            else:
                provera.append([x, y])
                provera.append([x-1, y])
        else:
            if y == n-1:
                return False
            else:
                provera.append([x, y])
                provera.append([x, y+1])
        if mat[provera[0][0]][provera[0][1]] != None or mat[provera[1][0]][provera[1][1]] != None:
            return False
        else:
            return True

def jedanKarakterProvera(y):
    if len(y) == 0 or len(y) > 1:
        print("Niste uneli jedan karakter!")
        ch1 = -1
    else:
        if ord(y) < 65 or ord(y) > 122:
            print("Niste uneli ispravan karakter!")
            ch1 = -1
        else:
            ch1 = str.upper(y)
    return ch1


def potez(mat, iksOks: bool, x, y, m, n):
     
    pr1 = jedanKarakterProvera(y)
    if pr1 == -1:
        return -1
    else:
        y = ord(pr1)-65
        x = m-x
        ispravan = valjanPotez(mat, iksOks, x, y, m, n)
        if ispravan == False:
            print("Nevalidan indeks, izaberite druge indekse!")
            return -1
        else:
            if iksOks == False:
                mat[x][y] = "X"
                mat[x-1][y] = "X"
            else:
                mat[x][y] = "O"
                mat[x][y+1] = "O"
            return mat


def proveraNijeKraj(mat, iksOks: bool, m, n):
    nijeKraj = False
    if iksOks == False:
        for a in range(m-1):
            for b in range(n):
                if mat[a][b] == None and mat[a+1][b] == None:
                    nijeKraj = True
    else:
        for a in range(m):
            for b in range(n-1):
                if mat[a][b] == None and mat[a][b+1] == None:
                    nijeKraj = True
    return nijeKraj

def zapocniIgru():
    tuple1 = inputDim()
    m = tuple1[0]
    n = tuple1[1]
    print(m, n)
    mat = pocetnoStanje(m, n)

    pom =input("Uneti igrača(X ili O): ")
    while(pom != "X" and pom != "x" and pom != "O" and pom != "o"):
        print("Unesite igraca kao x ili oks!")
        pom =input("Uneti igrača(X ili O): ")
    if (pom == "X" or pom =="x"):
        igrac = False
    else: 
        if (pom == "O" or pom =="o"):
            igrac= True

    while proveraNijeKraj(mat, igrac, m, n) == True:
        koIgra = "X" if igrac == False else "O"
        print("Trenutno je na potezu {}".format(koIgra))
        xPotez = int(input("Izaberite red: "))
        yPotez = input("Izaberite kolonu: ")
        prov = potez(mat, igrac, xPotez, yPotez, m, n)
        if type(prov) == list:
            mat = prov
            igrac = not igrac
        grafickiPrikaz(mat, m, n)
    if (proveraNijeKraj(mat, igrac, m, n) == False):
        print("Igra je gotova, pobedio je:  {}".format("X" if igrac == True else "O"))
    else: 
        print("Igra je gotova, pobedio je:  {}".format("X" if igrac == False else "O"))



def grafickiPrikaz(mat, m, n):
    chr123 = "A"
    strPrvaLinija = ("   " if m >= 10 else "  ")
    for a in range(n):
        strPrvaLinija = strPrvaLinija + chr123 + " "
        chr123 = chr(ord(chr123)+1)
 
    linijice = ("   " if m >= 10 else "  ")
    for x1 in range(n):
        linijice = linijice + "= "
 
    print(strPrvaLinija)
    print(linijice)
    for a1 in range(m):
        string1 = (" " if m >= 10 and (m-a1) < 10 else "") + "{}ǁ".format(m-a1)
        for a2 in range(n):
            if a2 == n-1:
                string1 = string1 + \
                    str(" " if mat[a1][a2] == None else mat[a1]
                        [a2]) + "ǁ{}".format(m-a1)
            else:
                string1 = string1 + \
                    str(" " if mat[a1][a2] == None else mat[a1][a2]) + "|"
        print(string1)
    print(linijice)
    print(strPrvaLinija)


zapocniIgru()
