def invullen_geslacht():
    geslachten = ["man", "vrouw", "overig"]
#Dit zijn de geslachten die de gebruiker zou kunnen kiezen.
    while True:
        geslacht = input("Wat is uw geslacht (man, vrouw of overig)? ").lower()
#Door de input kan de gebruiker het geslacht in vullen en door de .lower worden hoofdletter automatisch kleine letters gemaakt.
        if geslacht in geslachten:
            print("Geslacht correct ingevuld:", geslacht)
            return geslacht
#De in kijkt of de informatie van de gebruiker overeenkomt met de correcte geslachten.
        else:
            print("Fout ingevuld. Vul u alstublieft 'man', 'vrouw' of 'overig' in.")
#Als het niet overeenkomt met de correcte geslachten dan is het fout ingevuld.
ingevulde_geslacht = invullen_geslacht()
print("Ingevulde geslacht:", ingevulde_geslacht)
#Als het ingevulde geslacht het ingevulde geslacht, dan print hij het ingevulde geslacht.



def invullen_motivatiezin():
  while True:
        motivatiezin = input("Voer hier uw motivatiezin in: ")
        if motivatiezin.replace(" ", "").isalpha():
            return motivatiezin
#De.relace zorgt voor dat je spaties kan plaatsten. .Islapha is een string method die ik vond tussen de string methods in w3schools en isalpa kijkt of alle tekens in het alphabed zitten en kijkt of het waar is.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties, maar geen cijfers of punten.")
#Als er een verkeerd teken is gebruikt bij het achternaam dan print hij: Ongeldige invoer. Voer alleen letters in.
ingevulde_motivatiezin = invullen_motivatiezin()
print("Ingevoerde motivatiezin:", ingevulde_motivatiezin)
#Hier word de fuctie uitgevoerd.




def invullen_achternaam():
  while True:
        achternaam = input("Voer hier uw achternaam in: ")
        if achternaam.replace(" ", "").isalpha():
            return achternaam
#De.relace zorgt voor dat je spaties kan plaatsten. Islapha is een string method die ik vond tussen de string methods in w3schools en isalpa kijkt of alle tekens in het alphabed zitten en kijkt of het waar is.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties.")
#Als er een verkeerd teken is gebruikt bij het achternaam dan print hij: Ongeldige invoer. Voer alleen letters in.
ingevulde_achternaam = invullen_achternaam()
print("Ingevoerde achternaam:", ingevulde_achternaam)
#Hier word de fuctie uitgevoerd.




def invullen_geboortejaar():
    while True:
        geboortedatum = input("Voer hier uw geboortejaar: ")
        if geboortedatum.isdigit():
            return geboortedatum
#Hier gebruikte ik eerst isalnum dat doet precies het tegenovergestelde van isalpha, want het zorgt er voor dat alleen cijfers waar worden aangegeven. Alleen dit werkte uiteindelijk toch niet dus heb ik het vervangen voor isdigit en dat werkt goed.       
        else:
            print("Ongeldige invoer. Voer u alleen cijfers in en geen letters.")
#De else word uitgevoerd als de if niet waar is. En dan word ongeldige invoer. Voer alleen letters in en indien nodige spaties uitgeprint en dus aan de gebruiker getoont.
ingevulde_geboortedatum = invullen_geboortejaar()
print("Ingevoerde geboortejaar:", ingevulde_geboortedatum)
#Hier word de fuctie uitgevoerd.




def invullen_leeftijd():
  while True:
        leeftijd = input("Voer hier uw leeftijd in die u momenteel bent als u al jarig bent geweest dit jaar, als u dit jaar nog niet jarig bent geweest voer dan de leeftijd in die u nog moet worden: ")
        if leeftijd.isdigit():
            return leeftijd
#Hier gebruik ik .isdigit dat zorgt ervoor dat je alleen getallen kunt invullen.
        else:
            print("Ongeldige invoer. Voer u alleen cijfers in en geen letters.")
#De else word uitgevoerd als de if niet waar is. En dan word ongeldige invoer. Voer alleen letters in en indien nodige spaties uitgeprint en dus aan de gebruiker getoont.
ingevulde_leeftijd = invullen_leeftijd()
print("Ingevoerde leeftijd:", ingevulde_leeftijd)
#Hier word de fuctie uitgevoerd.

mylist = [ingevulde_geslacht, ingevulde_motivatiezin , ingevulde_achternaam , ingevulde_geboortedatum , ingevulde_leeftijd]
print(mylist)
#Hier print hij alle ingevulde infomatie in een lijst.





import datetime
#Hier word de actuelen datum vandaan gehaalt.
def ingevulde_leeftijd_gelijk_geboortejaar(geboortedatum, leeftijd):
    huidige_datum = datetime.datetime.now()
    geboortedatum = datetime.datetime.strptime(geboortedatum, "%Y")
    leeftijd_verjaardag_gepasseerd = (huidige_datum.month, huidige_datum.day) >= (geboortedatum.month, geboortedatum.day)
#De datums van nu is huidige_datum.month, huidige_datum.day >= zegt true als het groter dan is.     
    if huidige_datum.year - geboortedatum.year == int(leeftijd) and leeftijd_verjaardag_gepasseerd:
        print("Leeftijd en geboortejaar zijn geldig.")
        return True
#Huidig jaar min geboorte jaar is gelijk aan de leeftijd en de gepaseerde leeftijd.   
    else:
        print("Leeftijd en geboortejaar zijn niet geldig.")
        return False
    
#Als dat niet zo is print hij Leeftijd en geboortejaar zijn niet geldig.
gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)
print("Leeftijd en geboortejaar is:", gelijke_ongelijke_leeftijd)
#Hier word de functie uitgevoerd.







while not gelijke_ongelijke_leeftijd:
    print("U heeft een ongeldige combinatie van leeftijd en geboortejaar ingevoerd. probeer het opnieuw.")

    ingevulde_geboortedatum, ingevulde_leeftijd = invullen_geboortejaar_leeftijd()

    gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)

mylist = [ingevulde_geslacht, ingevulde_motivatiezin, ingevulde_achternaam, ingevulde_geboortedatum, ingevulde_leeftijd]
print(mylist)
# ... (de rest van de code blijft hetzelfde)