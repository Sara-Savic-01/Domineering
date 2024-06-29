import string
listaSlova=list(string.ascii_uppercase)
vrste=input("Unesite broj vrsta: ")
kolone=input("Unesite broj kolona: ")
while not vrste.isnumeric() or not kolone.isnumeric():
    print("Niste uneli odgovarajuce dimenzije table.")
    vrste=input("Unesite broj vrsta: ")
    kolone=input("Unesite broj kolona: ")

vrste=int(vrste)
kolone=int(vrste)

while vrste<2 or vrste>16 or kolone<2 or kolone>16:
    print("Niste uneli validne dimenzije table.")
    vrste=input("Unesite broj vrsta: ")
    kolone=input("Unesite broj kolona: ")
    vrste=int(vrste)
    kolone=int(vrste)


polje=[]
poljeCopy=[]

# odabir igraca za prvu fazu:

#print("Izaberite prvog igraca: ")
#print("Za opciju Covek-unesite broj 1")
#print("Za opciju Racunar-unesite broj 2")
#igrac=int(input("Unesite vasu opciju: "))
#if igrac==1:
#    print("Unesite pozicije da biste odigrali vertikalno:")
#    poz1=int(input("Pozicija: "))
#    poz2=input("Pozicija: ")
#elif igrac==2:
#    print("Racunar je na potezu")
#else:
#    print("Izaberite opciju 1 ili 2.")
#    igrac=int(input("Unesite vasu opciju: "))
    

for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append('   ')
    polje.append(a)

for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append('   ')
    poljeCopy.append(a)

vertikalniZid=[]
for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append('|')
    vertikalniZid.append(a)

horizontalniZid=[]
for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append(' - ')
    horizontalniZid.append(a)

statusi=[]
for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append(None)
    statusi.append(a)

statusiCopy=[]
for i in range(1,vrste+2):
    a=[]
    for j in range(1,kolone+2):
        a.append(None)
    statusiCopy.append(a)

#liste zidova
hor_zid1=[]
for i in range(1,10):
    hor_zid1.append("=")
hor_zid2=[]
for i in range(1,10):
    hor_zid1.append("=")
ver_zid1=[]
for i in range(1,10):
    ver_zid1.append("ǁ")
ver_zid2=[]
for i in range(1,10):
    ver_zid2.append("ǁ")

#pozicije igraca:
listaBrojeva=[]
listaCrtica=[]
def printTable(polje,vertikalniZid,horizontalniZid):
        for a in range(1,kolone+1):
            print("   "+listaSlova[a-1],end="")

        print()
        listaCrtica.append("")
        for a in range(1,kolone+1):
            if a==1:
                listaCrtica.append("    =")
            else:
                listaCrtica.append(" = ")

        for a in range(1,kolone+1):
            print(listaCrtica[a], end= " ")
        print()
        for i in reversed(range(1,vrste+1)):
            if(i<10):
                print(f"{i } ǁ",end="" )
            else:
                print(f"{i } ǁ",end="" )
            for j in range(1,kolone+1):
                print(polje[i][j],end="")
                if j<kolone:
                    print(vertikalniZid[i][j],end="")
            print(f"ǁ {i }")
            if i<vrste+1 and i>1:
                print("    ", end="")
                for k in range(1,kolone+1):
                    
                    print(horizontalniZid[i][k]+" ",end="")
                print()
        for a in range(1,kolone+1):
            print(listaCrtica[a],end=" ")
        print()
        for a in range(1,kolone+1):           
            print("   "+listaSlova[a-1],end="")
        print()
        print("\n")

printTable(polje,vertikalniZid,horizontalniZid)

X = " X "
O = " O "

def validMove(i, j, statusi, ig):        
        if i >= 1 and i <= vrste and j >= 1 and j <= kolone and statusi[i][j]==None and ((ig ==' X ' and statusi[i+1][j]==None and i+1<=vrste) or (ig==' O ' and statusi[i][j+1]==None and j+1<=kolone)):
            return True
        return False
        
    
    
def ciljnoStanje(ig):
    br=0
    if ig==' X ':
        for j in range(1,kolone+1):
            for i in range(1,vrste):

                if statusi[i][j]!=None or statusi[i+1][j]!=None:
                    br+=1
                    
        if br>=(kolone-1)*vrste:
            return True
        else:
            return False
    if ig==' O ':
        for i in range(1,vrste+1):
            for j in range(1,kolone):
                if statusi[i][j]!=None or statusi[i][j+1]!=None:
                    br+=1
        if br>=(vrste-1)*kolone:
            return True
        else:
            return False


def postaviPozicijuX (pozX):
    slovo=ord(pozX[1])-ord('@')
    if validMove(pozX[0],slovo,statusi,X):

        polje[pozX[0]][slovo] = X
        polje[pozX[0]+1][slovo] = X 

        statusi[pozX[0]][slovo] = 1
        statusi[pozX[0]+1][slovo] = 1
    
    printTable(polje,vertikalniZid,horizontalniZid)


def postaviPozicijuXCopy (pozX):
    slovo=ord(pozX[1])-ord('@')
    
    if validMove(pozX[0],slovo,statusiCopy,X):
        poljeCopy[pozX[0]][slovo] = X
        poljeCopy[pozX[0]+1][slovo] = X 

        statusiCopy[pozX[0]][slovo] = 1
        statusiCopy[pozX[0]+1][slovo] = 1
    

def postaviPozicijuO(pozO):
    slovo=ord(pozO[1])-ord('@')
    if validMove(pozO[0],slovo,statusi,O):

        polje[pozO[0]][slovo] = O
        polje[pozO[0]][slovo+1] = O

        statusi[pozO[0]][slovo] = 1
        statusi[pozO[0]][slovo+1] = 1
        
    printTable(polje,vertikalniZid,horizontalniZid)

def postaviPozicijuOCopy (pozO):
    slovo=ord(pozO[1])-ord('@')
    if validMove(pozO[0],slovo,statusiCopy,O):

        poljeCopy[pozO[0]][slovo] = O
        poljeCopy[pozO[0]][slovo+1] = O 

        statusiCopy[pozO[0]][slovo] = 1
        statusiCopy[pozO[0]][slovo+1] = 1

# provera za prvu fazu:
#if igrac==1:
    #postaviPozicijuX((poz1,poz2))
    #drugi igrac je racunar on bi trebao da igra O
#if igrac==2:
    #odigrava racunar  kao X ako je on prvi igrac
    #zatim covek igra kao drugi igrac,tacnije kao O

#postaviPozicijuX((6,'B'))
#postaviPozicijuX((4,'E'))
#postaviPozicijuO((7,'E'))
#postaviPozicijuO((2,'B'))

# provera pozicija
# dobri x
#postaviPozicijuX((1,'A'))
#postaviPozicijuX((2,'E')) 
#postaviPozicijuX((5,'G')) 
#postaviPozicijuX((7,'D')) 

# losi x
#postaviPozicijuX((9,'F'))
#postaviPozicijuX((3,'H')) 
#postaviPozicijuX((8,'B')) 
#postaviPozicijuX((8,'G'))
#postaviPozicijuX((5,'E')) 
#postaviPozicijuX((6,'F')) 

def moguciPotezi(ig):
    pom=[]
    if ig==' X ':
        for j in range(1,kolone+1):
            for i in range(1,vrste):
                if statusi[i][j]==None and statusi[i+1][j]==None:
                    pom.append((i,listaSlova[j-1]))
    if ig==' O ':
        for i in range(1,vrste+1):
            for j in range(1,kolone):
                if statusi[i][j]==None and statusi[i][j+1]==None:
                    pom.append((i,listaSlova[j-1]))
                    
    return pom
                    

#print("Moguci potezi za X:")
#print(moguciPotezi(' X ')) 

#print("Moguci potezi za O:")
#print(moguciPotezi(' O '))    

# covek-covek (igraci za drugu fazu):

def igracX():
    if ciljnoStanje(' X ')==False:
        print("Moguci potezi za X:")
        print(moguciPotezi(' X '))  
        print("Igrac X unosi poziciju.")
        poz1=input("Pozicija: ")
        while not poz1.isnumeric():
            print("Niste uneli ispravnu poziciju.")
            poz1=input("Pozicija: ")
        poz1=int(poz1)
        poz2=input("Pozicija: ")
        poz2=poz2.upper()
        #slovo=ord(poz2)-ord('@')
        #if validMove(poz1, slovo, statusi, ' X '):
        if (poz1,poz2) in moguciPotezi(' X '):
            postaviPozicijuX((poz1,poz2))
           
            print("Igrac O je na potezu!")
            igracO()
        else:
            print("Niste uneli validne pozicije!")
            igracX()
    else:
        print("Igra je gotova! Pobednik je igrac O!")

def igracO():
    if ciljnoStanje(' O ')==False:
        print("Moguci potezi za O:")
        print(moguciPotezi(' O '))
        print("Igrac O unosi poziciju.")
        poz1=input("Pozicija: ")
        while not poz1.isnumeric():
            print("Niste uneli ispravnu poziciju.")
            poz1=input("Pozicija: ")
        poz1=int(poz1)
        poz2=input("Pozicija: ")
        poz2=poz2.upper()
        #slovo=ord(poz2)-ord('@')
        #if validMove(poz1, slovo, statusi, ' O '):
        if (poz1,poz2) in moguciPotezi(' O '):
            postaviPozicijuO((poz1,poz2))
            
            print("Igrac X je na potezu!")
            igracX()
        else:
            print("Niste uneli validne pozicije!")
            igracO()
    else:
        print("Igra je gotova! Pobednik je igrac X!")


# covek-racunar (treca faza):

def heuristika1():
    igrac_X=0
    igrac_O=0
    for i in range(vrste):
        for j in range(kolone):
            if statusi[i][j]==' X ':
                duzinaLanca=1
                k=j+1
                while k<kolone and statusi[i][k]==' X ':
                    duzinaLanca+=1
                    k+=1
                    igrac_X=max(igrac_X,duzinaLanca)
            elif statusi[i][j]==' O ':
                duzinaLanca=1
                k=i+1
                while k<vrste and statusi[k][j]==' O ':
                    duzinaLanca+=1
                    k+=1
                    igrac_O=max(igrac_O,duzinaLanca)
    return igrac_X-igrac_O




def minimax(dubina,alfa,beta,maxIgrac):
    najboljiPotez=None
    najboljaVrednost=-1000 if maxIgrac else 1000
    alfa=-1000
    beta=1000

    def min_value(potez,dubina,alfa,beta):
        if dubina==0 or ciljnoStanje(' O ')==True:
            return heuristika1()
        vrednost=1000
        for potez in moguciPotezi(' O '):
            vrednost=min(vrednost,max_value(postaviPozicijuOCopy((potez[0],potez[1])),dubina-1,alfa,beta))
            if vrednost<=alfa:
                return vrednost
            beta=min(beta,vrednost)
        return vrednost

    def max_value(potez,dubina,alfa,beta):
        if dubina==0 or ciljnoStanje(' X ')==True:
            return heuristika1()
        vrednost=-1000
        for potez in moguciPotezi(' X '):
            vrednost=max(vrednost,min_value(postaviPozicijuXCopy((potez[0],potez[1])),dubina-1,alfa,beta))
            if vrednost>=beta:
                return vrednost
            alfa=max(alfa,vrednost)
        return vrednost

    if maxIgrac:
        for potez in moguciPotezi(' X '):
            vr=min_value(postaviPozicijuXCopy((potez[0],potez[1])),dubina,alfa,beta)
            if vr>najboljaVrednost:
                najboljaVrednost=vr
                najboljiPotez=potez
    else:
        for potez in moguciPotezi(' O '):
            vr=max_value(postaviPozicijuOCopy((potez[0],potez[1])),dubina,alfa,beta)
            if vr<najboljaVrednost:
                najboljaVrednost=vr
                najboljiPotez=potez
    return najboljiPotez
        

def igracCovekX():
    if ciljnoStanje(' X ')==False:
        print("Moguci potezi za X:")
        print(moguciPotezi(' X '))  
        print("Igrac X unosi poziciju.")
        poz1=input("Pozicija: ")
        while not poz1.isnumeric():
            print("Niste uneli ispravnu poziciju.")
            poz1=input("Pozicija: ")
        poz1=int(poz1)
        poz2=input("Pozicija: ")
        poz2=poz2.upper()
        # slovo=ord(poz2)-ord('@')
        # if validMove(poz1, slovo, statusi, ' X '):
        if (poz1,poz2) in moguciPotezi(' X '):
            postaviPozicijuX((poz1,poz2))
            
            igracRacO()            
        else:
            print("Niste uneli validne pozicije!")
            igracCovekX()
    else:
        print("Igra je gotova! Pobednik je igrac O!")

def igracCovekO():
    if ciljnoStanje(' O ')==False:
        print("Moguci potezi za O:")
        print(moguciPotezi(' O '))
        print("Igrac O unosi poziciju.")
        poz1=input("Pozicija: ")
        while not poz1.isnumeric():
            print("Niste uneli ispravnu poziciju.")
            poz1=input("Pozicija: ")
        poz1=int(poz1)
        poz2=input("Pozicija: ")
        poz2=poz2.upper()
        #slovo=ord(poz2)-ord('@')
        #if validMove(poz1, slovo, statusi, ' O '):
        if (poz1,poz2) in moguciPotezi(' O '):
            postaviPozicijuO((poz1,poz2))  
                 
            igracRacX()            
        else:
            print("Niste uneli validne pozicije!")
            igracCovekO()
    else:
        print("Igra je gotova! Pobednik je igrac X!")


def igracRacX():
    if ciljnoStanje(' X ')==False:
        print("Igrac X je na potezu!")
        potez=minimax(3,-1000,1000,True) 
        postaviPozicijuX((potez[0],potez[1]))
        igracCovekO()
    else:
        print("Igra je gotova! Pobednik je igrac O!")


def igracRacO():
    if ciljnoStanje(' O ')==False:
        print("Igrac O je na potezu!")
        potez=minimax(3,-1000,1000,False)
        postaviPozicijuO((potez[0],potez[1]))
        igracCovekX() 
    else:
        print("Igra je gotova! Pobednik je igrac X!")

def igraCovekRacunar():
    print("Izaberite prvog igraca: \nZa opciju Covek-unesite broj 1 \nZa opciju Racunar-unesite broj 2")
    igrac=int(input("Unesite vasu opciju: "))
    if igrac==1:
        igracCovekX()
        
    elif igrac==2:
        print("Racunar je na potezu")
        igracRacX()
        
    else:
        print("Izaberite opciju 1 ili 2.")
        #igrac=int(input("Unesite vasu opciju: "))
        igraCovekRacunar()


def glavnaIgra():
    igracX()
    
# covek-covek:    
#glavnaIgra()

# covek-racunar:

igraCovekRacunar()
