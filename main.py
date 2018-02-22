# Datei:    Sudokusolver.py
# Version:  1.1
# Datum:    22.02.2018
# Autor:    Joules

##4 Überprüfungen:
## 1. Ist Feld=0?
## 2. Gibts die Zahl in der spalte
## 3. Gibts sie in der Zeile?
## 4. Gibts sie im Block

'''liste =[[ 2, 4, 0, 0, 9, 0, 0, 0, 0 ],
        [ 5, 1, 0, 0, 0, 3, 4, 0, 9 ],
        [ 0, 0, 0, 0, 6, 4, 2, 8, 1 ],
        [ 0, 0, 0, 3, 0, 8, 1, 0, 0 ],
        [ 1, 0, 7, 0, 0, 0, 0, 5, 3 ],
        [ 0, 3, 5, 6, 0, 0, 0, 0, 4 ],
        [ 0, 5, 1, 7, 0, 0, 0, 0, 2 ],
        [ 0, 0, 3, 0, 2, 0, 0, 0, 0 ],
        [ 0, 2, 4, 0, 1, 9, 3, 0, 0 ]];'''
liste = [[0,0,3],
         [2,0,0],
         [0,0,0]];


def bedroht(liste, zahl, aktPos, zeile):
    #print "bedroht"
    if liste==[]:
        return 0
    
    #Kontrolle der Zeile/Spalte
    for  k in liste[zeile]:
        if k == zahl:
            return 1
    for m in range(0,8):
        if liste[m][aktPos] == zahl:
            return 1

    #Kontrolle des Kastens
    bPos=aktPos/3
    bZeile=zeile/3
    for i in range(0,8):
        if i/3 == bZeile:
            for j in range(0,8):
                if j/3 == bPos:
                    if liste[i][j]==zahl:
                        return 1

def loese(aktPos, zeile, liste):
    gesetzt=0
    zahl=1
    while zahl<=9 and not gesetzt:
        if aktPos is not 8 and liste[zeile][aktPos]==0:
            while zahl<=9 and not gesetzt:
                if bedroht(liste, zahl, aktPos, zeile) is 1:
                    zahl=zahl+1
                else:
                    print zeile, aktPos, liste[zeile][aktPos], zahl
                    liste[zeile][aktPos]=zahl
                    gesetzt+=1
                    print gesetzt

        else:
            if aktPos is 8:
                loese(0, zeile+1, liste)
            else:
                loese(aktPos+1, zeile, liste)
            
        if aktPos is 8 and zeile is 8 and gesetzt==1:
            print liste
        elif aktPos is 8 and zeile is not 8 and gesetzt==1:
            loese(0, zeile+1, liste)
        elif aktPos is not 8 and zeile is not 8 and gesetzt==1:
            loese(aktPos+1, zeile, liste)
        else:
            return 0
    
                   
def sudokusolver():
    loese(0,0, liste)

sudokusolver()
    
    
