# Datei:    Sudokusolver.py
# Version:  1.0
# Datum:    13.02.2018
# Autor:    Joules

##4 Überprüfungen:
## 1. Ist Feld=0?
## 2. Gibts die Zahl in der spalte
## 3. Gibts sie in der Zeile?
## 4. Gibts sie im Block

liste =
{
{ 2, 4, 0, 0, 9, 0, 0, 0, 0 },
{ 5, 1, 0, 0, 0, 3, 4, 0, 9 },
{ 0, 0, 0, 0, 6, 4, 2, 8, 1 },
{ 0, 0, 0, 3, 0, 8, 1, 0, 0 },
{ 1, 0, 7, 0, 0, 0, 0, 5, 3 },
{ 0, 3, 5, 6, 0, 0, 0, 0, 4 },
{ 0, 5, 1, 7, 0, 0, 0, 0, 2 },
{ 0, 0, 3, 0, 2, 0, 0, 0, 0 },
{ 0, 2, 4, 0, 1, 9, 3, 0, 0 }
};


def bedroht(akt, zahl):
    if liste==[]:
        return 0
    
    #Kontrolle der Zeile/Spalte
    for  in gesetzteDamen:
        if dieDame[0]==dame[0] or dieDame[1]==dame[1]:
            return 1


    #Kontrolle des Kastens


def loese( aktPos, zeile, liste):
    akt=(zeile,aktPos)
    gesetzt=0
    zahl=1
    while not gesetzt and zahl>9:
        if bedroht(akt, zahl) is 1 :
            zahl +=1
        else:
            liste[akt]=zahl
            gesetzt+=1
        if aktPos is 8 and zeile is 8 :
            print liste
        elif zeile is 8:
            loese(0, zeile+1, liste )
        else:
            loese(aktPos+1, zeile, liste)
