import copy


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
    x = int(x)
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


def jedanKarakterProvera(x, y):
    if x.isnumeric() == False:
        print("Niste uneli numericki podatak za vrstu!")
        ch1 = -1
    else:
        if y.isnumeric() == True:
            ch1 = -1
            print("Unesite slovo za kolonu!")
        else:
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
    pr1 = jedanKarakterProvera(x, y)
    if pr1 == -1:
        return -1
    else:
        y = ord(pr1)-65
        x = m-int(x)
        ispravan = valjanPotez(mat, iksOks, str(x), y, m, n)
        if ispravan == False:
            return mat
        else:
            new_matrix = pocetnoStanje(m, n)
            for i in range(m):
                j = 0
                while (j < n):
                    if x == i and y == j:
                        if iksOks == False:
                            new_matrix[i][j] = "X"
                            new_matrix[i-1][j] = "X"
                            j += 1
                        else:
                            new_matrix[i][j] = "O"
                            new_matrix[i][j+1] = "O"
                            j += 2
                    else:
                        new_matrix[i][j] = mat[i][j]
                        j += 1
            return new_matrix


def proveraNijeKraj(mat, iksOks: bool, m, n):
    nijeKraj = False
    listPotezi = []
    if iksOks == False:
        for a in range(m-1):
            for b in range(n):
                if mat[a][b] == None and mat[a+1][b] == None:
                    nijeKraj = True
                    listPotezi.append([a, b])
    else:
        for a in range(m):
            for b in range(n-1):
                if mat[a][b] == None and mat[a][b+1] == None:
                    nijeKraj = True
                    listPotezi.append([a, b])
    return (nijeKraj, listPotezi)


def formatirajTekst(lista, m, iksOks):
    string1 = "Moguci potezi su: "
    for el in lista:
        el[0] = m - el[0] - 1
        char1 = 65 + el[1]
        if iksOks == True:
            el[0] = el[0]+1
        string1 = string1 + "[{}, {}], ".format(el[0], chr(char1))
    string1 = string1[:len(string1)-2]
    print(string1)
    return string1


def zapocniIgru():
    tuple1 = inputDim()
    m = tuple1[0]
    n = tuple1[1]
    print(m, n)
    mat = pocetnoStanje(m, n)
    grafickiPrikaz(mat, m, n)

    #Može i ovako da radi, da biramo na početku kao koji igrač će da igra računar
    #kompjuter= input("Ćao, ja sam kompjuter! Kao koji igrač hoćeš da te pobedim?  ")
    #if (kompjuter == "X" or kompjuter == "x"):
        #komp = False
    #else:
        #if (kompjuter == "O" or kompjuter == "o"):
            #komp = True

    pom = input("Uneti igrača(X ili O): ")
    while (pom != "X" and pom != "x" and pom != "O" and pom != "o"):
        print("Unesite igraca kao x ili oks!")
        pom = input("Uneti igrača(X ili O): ")
    if (pom == "X" or pom == "x"):
        igrac = False
    else:
        if (pom == "O" or pom == "o"):
            igrac = True

    #igrac=False #prvo uvek igra x
    moguciPotezi = list()
    while proveraNijeKraj(mat, igrac, m, n)[0] == True:
        koIgra = "X" if igrac == False else "O"
        print("Trenutno je na potezu {}".format(koIgra))
        moguciPotezi = proveraNijeKraj(mat, igrac, m, n)[1]
        potezi = formatirajTekst(moguciPotezi, m, igrac)
        #if igrac==komp:
        if igrac == False:
            optimalniPotez = minimax_alpha_beta(
                mat, m, n, 3, igrac, alpha=(None, -10), beta=(None, 10))[0]
            if type(optimalniPotez) is list:
                xPotez = str(m - optimalniPotez[0]-1)
                yPotez = chr(65 + optimalniPotez[1])
            else:
                moguciPotezi = proveraNijeKraj(mat, igrac, m, n)[1]
                xPotez = str(m-moguciPotezi[0][0]-1)
                yPotez = chr(65+moguciPotezi[0][1])
            #print("Optimalni potez je ", [xPotez, yPotez])
        else:
            xPotez = input("Izaberite red: ")
            yPotez = input("Izaberite kolonu: ")
        prov = potez(mat, igrac, xPotez, yPotez, m, n)
        if type(prov) == list:
            mat = prov
            igrac = not igrac
        grafickiPrikaz(mat, m, n)
    if (proveraNijeKraj(mat, igrac, m, n)[0] == False):
        print("Igra je gotova, pobedio je:  {}".format(
            "X" if igrac == True else "O"))
    else:
        print("Igra je gotova, pobedio je:  {}".format(
            "X" if igrac == False else "O"))


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


def realniPotezi(mat, iksOks, m, n):
    brRealPotez = 0
    if (iksOks):
        for i in range(0, m):
            j = 0
            while (j < n-1):
                if (mat[i][j] == None and mat[i][j+1] == None):
                    brRealPotez += 1
                    j += 2
                else:
                    j += 1
    else:
        for i in range(0, n):
            j = m-1
            while (j > 0):
                if (mat[j][i] == None and mat[j-1][i] == None):
                    brRealPotez += 1
                    j -= 2
                else:
                    j -= 1

    return brRealPotez


def sigurniPotezi(mat, iksOks, m, n):
    brSigPotez = 0
    listaPoteza1 = proveraNijeKraj(mat, True, m, n)[1]  # Oks
    listaPoteza2 = proveraNijeKraj(mat, False, m, n)[1]  # Iks
    if (iksOks):  # false X,true O
        for x in listaPoteza1:
            x1 = x.copy()
            if (x not in listaPoteza2):
                x1[1] += 1
                if (x1 not in listaPoteza2):
                    x1[0] += 1
                    if (x1 not in listaPoteza2):
                        x1[1] -= 1
                        if (x1 not in listaPoteza2):
                            brSigPotez += 1
    else:
        for x in listaPoteza2:
            x1 = x.copy()
            if (x not in listaPoteza1):
                x1[0] -= 1
                if (x1 not in listaPoteza1):
                    x1[1] -= 1
                    if (x1 not in listaPoteza1):
                        x1[0] += 1
                        if (x1 not in listaPoteza1):
                            brSigPotez += 1

    return brSigPotez


def heuristika(mat, potezKoor, iksOks, m, n):
    mat2 = copy.deepcopy(mat)
    mat2[potezKoor[0]][potezKoor[1]] = ("X" if iksOks == False else "O")
    if (iksOks):
        mat2[potezKoor[0]][potezKoor[1]+1] = "O"
    else:
        mat2[potezKoor[0]-1][potezKoor[1]] = "X"

    # izracunati realne poteze
    brRealPotezJa = realniPotezi(mat2, iksOks, m, n)
    brRealPotezProt = realniPotezi(mat2, not iksOks, m, n)
    # izracunati sigurne poteze
    brSigPotezJa = sigurniPotezi(mat, iksOks, m, n)
    brSigPotezProt = sigurniPotezi(mat, not iksOks, m, n)
    #print(brRealPotezProt - brRealPotezJa + brSigPotezProt - brSigPotezJa)
    return (brRealPotezJa - brRealPotezProt + brSigPotezJa - brSigPotezProt )


def Puna(mat, m, n):
    puna = True
    for a in range(m-1):
        for b in range(n-1):
            if (mat[a][b] == None and mat[a-1][b] == None):
                puna = False
            else:
                if (mat[a][b] == None and mat[a][b+1] == None):
                    puna = False
    return puna


def max_value(iksOks, mat, m, n, dubina, alpha, beta, potez1=None):
    # ako je kraj igre
    if proveraNijeKraj(mat, iksOks, m, n)[0] == False or Puna(mat, m, n) == True:
        return (potez1, int(proveraNijeKraj(mat, iksOks, m, n)[0]))
    lista_poteza = (proveraNijeKraj(mat, iksOks, m, n)[1])
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez1, heuristika(mat, potez1, iksOks, m, n))
    else:
        for s in lista_poteza:
            i = str(m - s[0]-1)
            j = chr(65 + s[1])
            alpha = max(alpha, min_value(iksOks, potez(mat, iksOks, i, j, m, n), m, n, dubina - 1,
                        alpha, beta, s if potez1 is None else potez1), key=lambda x: x[1])
        if alpha[1] >= beta[1]:
            return beta
        return alpha


def min_value(iksOks, mat, m, n, dubina, alpha, beta, potez1=None):
    if proveraNijeKraj(mat, iksOks, m, n)[0] == False or Puna(mat, m, n) == True:
        return (potez1, int(proveraNijeKraj(mat, iksOks, m, n)[0]))
    lista_poteza = list((proveraNijeKraj(mat, iksOks, m, n)[1]))
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez1, heuristika(mat, potez1, iksOks, m, n))
    else:
        for s in lista_poteza:
            i = str(m - s[0]-1)
            j = chr(65 + s[1])
            beta = min(beta, max_value(iksOks, potez(mat, iksOks, i, j, m, n), m, n, dubina - 1,
                       alpha, beta, s if potez1 is None else potez1), key=lambda x: x[1])
        if beta[1] <= alpha[1]:
            return alpha
        return beta


def minimax_alpha_beta(mat, m, n, dubina, iksOks, alpha, beta):
    if iksOks:
        return min_value(iksOks, mat, m, n, dubina, alpha, beta)
    else:
        return max_value(iksOks, mat, m, n, dubina, alpha, beta)


zapocniIgru()
