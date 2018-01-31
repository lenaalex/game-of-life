from spillebrett1 import Spillebrett
# importerer fra fil spillebrett klass spilebrett

def hovedprogram(): # lager funksjon uten parameter
    rad=int(input("Skriv ut rader: ")) # brukeren lager rader
    kolonne=int(input("Skriv ut kolloner: "))# # brukeren lager kolloner
    spillebrett1 = Spillebrett( rad, kolonne) # variabel som henter klasse spillebrett med disse variabller som lagt brukeren
    spillebrett1.tegnBrett() # tegner brett med disse variabler som brukeren legg inn i spillebrett
    print("Trykk enter for å forsette men hvis du vil avslutter spillet trykk q ")
    while True:# while løkke alltid true
        inp=input(" ") # tom linje skal oppdaterer spillebrettet
        spillebrett1.oppdatering()# kaller metode oppdatering fra klasse spillebrett med vedier som brukeren lagg inn
        spillebrett1.tegnBrett() # kaller metode tegnmetode med med vedier som har brukeren lagg inn
        if inp =="q": # hvis trykke q
            break     # skal programmet er avsluttes
        print("Antall levende celler:", spillebrett1.finnAntallLevende()) # skriver ut antall levende celler

    print("Antall levende celler:", spillebrett1.finnAntallLevende()) # skriver ut antall levende celler


hovedprogram() # kaller programmet main
