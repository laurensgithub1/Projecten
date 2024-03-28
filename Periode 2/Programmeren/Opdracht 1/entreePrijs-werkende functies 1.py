def vraagWeekdag():
    #hier wordt de code geschreven om de weekdag te vragen
    #een waarde toekennen zodat de while actief wordt
    invoer=99
    while invoer not in [1,2,3,4,5,6,7]:
        invoer=int(input("Welke dag is het vandaag ? [1-ma, 7-zo]"))
        if invoer > 7 or invoer<1 :
            print("Voer een getal in van 1 t/m 7! [1-ma, 7-zo]")
    
    return invoer

def vraagLeeftijd():
    #hier wordt de code geschreven om de leeftijd te vragen
    leeftijd=250
    while leeftijd<1 or leeftijd >100 :
        leeftijd=int(input("Wat is je leeftijd?"))
    
    return leeftijd

def vraagAbonnement():
    #hier wordt gevraagd of de klant een abonnement heeft.
    antw="Z"
    while antw not in ["J","N"]:
        antw=input("Heeft u een abonnement? [j/n]").upper()
    if antw=="J":
        heeftAbo=True
    else:
        heeftAbo=False
    return heeftAbo

def vraagNogEenKeer():
    #hier komt de code om te vragen of er nog een gebruiker is
    nogeens=False
    antw="z"
    while antw not in ["J","N"]:
        antw=input("Is er nog een klant ? [j/n]").upper()
        if antw=="J":
            nogeens=True
    return nogeens

def berekenPrijs(dag,leeftijd,heeftAbo):
    #Hier komt de code om de prijs te berekenen
    prijs=5.00
    #werkdagen waarde is 1 t.m 5, weekend 6 en 7
    prijs=0.0
    if dag <=5:
        if heeftAbo:
            prijs=2.5
        else :
            prijs=5.0
    else :
        if leeftijd >=18:
            if heeftAbo:
                prijs=5.0
            else:
                prijs=7.5
        else:
            if heeftAbo:
                if leeftijd >= 7 and leeftijd <=12 :
                    prijs=2.5
                else:
                    prijs=5.0
            else:
                prijs=7.5
    return prijs

def berekenPrijs2(dag,leeftijd,heeftAbo):
    #Hier komt de code om de prijs te berekenen
    prijs=5.00
    #werkdagen waarde is 1 t.m 5, weekend 6 en 7
    prijs = 0.0
    prijs = 0.0

    if dag <= 5:
        prijs = 2.5 if heeftAbo else 5.0
    else:
        if leeftijd >= 18:
            prijs = 5.0 if heeftAbo else 7.5
        elif 7 <= leeftijd <= 12 and heeftAbo:
            prijs = 2.5
        else:
            prijs = 7.5

    return prijs

dag=vraagWeekdag()
prijs=0.0
totaalprijs=0.0
nogEenKlant=True
while nogEenKlant:
    leeftijd=vraagLeeftijd()
    heeftKorting=vraagAbonnement()
    prijs=berekenPrijs2(dag,leeftijd, heeftKorting)
    print("De toegangsprijs is : ",prijs, " met de gegevens: ")#,dag,leeftijd, heeftKorting      
    totaalprijs+=prijs
    nogEenKlant=vraagNogEenKeer()
print("Het totaalbedrag is : ",totaalprijs)       
    
    
