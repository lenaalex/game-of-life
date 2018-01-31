"""
I denne delen oppgaven vi skal beskrive et todimensjonalt brett som inneholder
celler. Spillebrettet skal holde styr på hvilken celler som skal endre status og
oppdaterer disse for hver generasjon.
"""
# importerer Celle klasser og metoder fra fil celle.
# og importerer funskjon fra ferdig programmet i puthon random fra fil randint
from celle1 import Celle
from random import randint
# definerer klass Spillebrett og lager konsturktør, metoder
class Spillebrett:
    """ initialiseres variabler som skal brukes i klassen med "self._"
    inne i parameter setter kolonner og rader som skal tegnes spillebrett
    """
    def __init__(self,kolloner,rader): # initialisere rader og kolloner
        self._kolloner = kolloner # kolonner
        self._rader = rader # rader
        self._rutenett=[] # tom lister
        self._generasjonsnummer=0 # lager en fast variabel
        """
        for løkke går gjennom rader og kolonner. Legger inn i tom liste først rader og
        etterpå kolloner i todimensjonalt liste
        """
        for i in range (self._rader): #for løkke går gjennom rader
            liste=[] # definerer variabel tom liste
            for j in range(self._kolloner): # for løkke går gjennom kolloner
                   liste.append(Celle()) # kolloner og rader lik til celle objekt og legges in i tom liste
            self._rutenett.append(liste) #  legger den listen med rader og kolloner inn i rutenett liste

        self.generer() # definerer metoden generer inne i konstruktør
    """ inne i metoden tegnBrett skal vi tegne todimensjonal liste som vi har fylt med
    tom liste ruternett , først skal skrives ut rader og etterpå kolonner
    """
    def tegnBrett(self):

        for y in range (len(self._rutenett)): # for løkke skriver ut rader

            for x in range(len(self._rutenett[y])): # for løkke skriver ut kolloner
                celleObjekt = self._rutenett[y][x] # lager en variabel som lik til en celle objekt i rutenett
                print(celleObjekt.tegnerepresentasjon(),end='')# skriver ut tegnerepresentasjon inne i rutenett liste
            print()
    """ i metoden oppdatering lager to tomme lister en liste heter døde der skal lages alle døde
    celler men den listen som heter levende skal legges inn alle levende celler. En variabel
    generasjonsnummer som skal økes hver gang når spillebrettet er oppdageres
    """
    def oppdatering(self): # denne metoden oppdaterer celler i rutenett
        self._generasjonsnummer=self._generasjonsnummer + 1 #teller hvert generasjon
        #print("Generasjon", self._generasjonsnummer)
        doede=[] # lager en tomme lister for døde celler
        levende=[] # lager en tomme for levende celler

        for i in range (len (self._rutenett)): # for løkke går gjennom rader
            for j in range (len(self._rutenett[i])): # for løkke går gjennom kolloner
                liste = self.finnNabo(i,j) # definerer variabel liste som lik nabolisten
                teller=0 # teller som start verdi lik null
                celle2 = self._rutenett[i][j] # lager en variabel celle som lik til celle inne i rutenett
                for celle in liste: # for celle inne i naboliste
                    if celle.erLevende() == True: # hvis den celle inne i nabolisten er levende
                         teller=teller+1 # teller disse levende celler inne i liste
                if celle2.erLevende(): # hvis det den celle i ruternett er levende
                    if teller < 2: # hvis det er mindre enn 2 levende celler
                        doede.append(celle2) # den levende celle i rutenett skal legges in i døde liste
                    if teller > 3: # hvis det levende celler større enn 3
                        doede.append(celle2)#skal lages den celle inne i døde liste
                else:
                    if teller == 3: # hvis det levedne celle lik 3 eller 2
                        levende.append(celle2) # celle skal legges inn i levende liste

        for celle1 in doede: # for hver celle i døde liste
            celle1.settDoed() # den celle skal endre status
        for celle1 in levende: # for hver celle i levende liste
            celle1.settLevende() # skal den celle endre status
        print("Generasjon", self._generasjonsnummer) # skriv ut generasjon nummer når rutenett endres


    def finnAntallLevende(self): # en metode som teller alle levende celler
        antallLevende=0 # skal lage variabel som har første verdi lik null
        for i in range (len (self._rutenett)):# for løkke går gjennom rader
            for j in range (len(self._rutenett[i])): # for løkke går gjennom kolloner
                if self._rutenett[i][j].erLevende(): # hvis inne i rutenett liste en celle er levende
                    antallLevende= antallLevende + 1 # teller den levende celler
        return antallLevende # returnerer antall levende celler


    def generer(self): # den metode generer tilfeldig levende celler
        for i in range (self._rader): # for løkke går gjennom rader
            for j in range (self._kolloner): # for løkke går gjennom kolloner
                rand = randint(0,3) # variabel som generer tilfeldig tall
                if rand == 1: # hvis det tilveldig tall lik 1
                    self._rutenett[i][j].settLevende() # og skal lage den som levende

    def finnNabo (self, rader, kolloner):# metode som finne nabo celler inne i rutenett
        naboliste = []
        for i in range (-1, 2) :
            for j in range (-1, 2) :
                naboRad = rader+i
                naboKolonne = kolloner+j
                if (naboRad == rader and naboKolonne == kolloner) != True :
                    if (naboRad < 0 or naboKolonne < 0 or naboRad > self._rader-1 or naboKolonne > self._kolloner-1) != True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste
