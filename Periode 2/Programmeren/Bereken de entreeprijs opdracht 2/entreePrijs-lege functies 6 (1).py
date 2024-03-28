"""
    use case : Bereken de entreeprijs
    versie 1,0
    JGP Roode
    22-11-2022
"""
def vraagWeekdag():
    #hier wordt de code geschreven om de weekdag te vragen
    while not(weekdag>=1 and weekdag<=7):
        vraagWeekdag = int(input("Welke dag van de week is het"))
    #print("dit is vraagweekdag")
    return weekdag

def vraagLeeftijd():
    #hier wordt de code geschreven om de leeftijd te vragen
    leeftijd=12
    print("dit is vraagleeftijd")
    return leeftijd

def vraagAbonnement():
    #hier wordt gevraagd of de klant een abonnement heeft.
    print("vraagabo")
    heeftAbo=False
    return heeftAbo

def vraagNogEenKeer():
    #hier komt de code om te vragen of er nog een gebruiker is
    nogeens=True
    antw="Z"
    while antw not in ["N","J"]:
        antw=input("Is er nog een klant?[j/n]").upper()
        if antw=="N" :
            nogeens=False
    return nogeens

def berekenPrijs(dag,leeftijd,heeftAbo):
    #Hier komt de code om de prijs te berekenen
    print("ik reken het bedrag uit")
    prijs=5.00
    return prijs

#initialiseren
nogEenKlant=True
dag=vraagWeekdag()
prijs=0
totaalprijs=0

while nogEenKlant:
    leeftijd=vraagLeeftijd()
    heeftKorting=vraagAbonnement()
    prijs=berekenPrijs(dag,leeftijd, heeftKorting)
    nogEenKlant=vraagNogEenKeer()
    print(prijs)
    totaalprijs+=prijs

    
print(totaalprijs)
    
    
