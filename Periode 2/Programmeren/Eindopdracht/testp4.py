import datetime
#Zo word de actuelen tijd opgehaalt.
def invullen_geslacht():
    geslachten = ["man", "vrouw", "overig"]
#hier worden alle mogelijke antwoorden aangeven voor geslacht.
    while True:
        geslacht = input("Wat is uw geslacht (man, vrouw of overig)? ").lower()
#Hier word er aan de gebruiker gevraagt naar zijn geslacht. De .lower zorgt er voor dat de antwoorden met hoofdletters kleinen letters worden.
        if geslacht in geslachten:
            print("Geslacht correct ingevuld:", geslacht)
            return geslacht
#Als het geslacht in geslacht staat is het waar.
        else:
            print("Fout ingevuld. Vul u alstublieft 'man', 'vrouw' of 'overig' in.")
#Als het geslacht er niet in staat word er getypt: Fout ingevuld. Vul u alstublieft 'man', 'vrouw' of 'overig' in.
ingevulde_geslacht = invullen_geslacht()
print("Ingevulde geslacht:", ingevulde_geslacht)
#Hier word de functie aangeroepen.

def invullen_motivatiezin():
    while True:
        motivatiezin = input("Voer hier uw motivatiezin in: ")
        if motivatiezin.replace(" ", "").isalpha():
            return motivatiezin
#Hier word de motivatiezin gevraagt waar de gebruiker het kan type. .isalpa zorgt ervoor dat je alleen maar letters kan type uit het alphabed en . replace (" ", "") zorgt er voor dat je spaties kan plaatsen.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties, maar geen cijfers of punten.")
#Dit word geprint als je het fout hebt ingevoerd.
ingevulde_motivatiezin = invullen_motivatiezin()
print("Ingevoerde motivatiezin:", ingevulde_motivatiezin)
#Hier word de functie weer aangeroepen.

def invullen_achternaam():
    while True:
        achternaam = input("Voer hier uw achternaam in: ")
        if achternaam.replace(" ", "").isalpha():
            return achternaam
#Hier word weer .replace(" ", "") en .isalpa gebruikt. De return aachternaam zorgt er voor dat de achternaam weer terug geroepen wordt.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties.")
#Als er een ongeldige invoer is word dit geprint.
ingevulde_achternaam = invullen_achternaam()
print("Ingevoerde achternaam:", ingevulde_achternaam)
#Hier word de functie aangeroepen.

def invullen_geboortejaar_leeftijd():
    while True:
        ingevulde_geboortedatum = input("Voer hier uw geboortejaar: ")
        ingevulde_leeftijd = input("Voer hier uw leeftijd in die u momenteel bent als u al jarig bent geweest dit jaar, als u dit jaar nog niet jarig bent geweest voer dan de leeftijd in die u nog moet worden: ")
#Hier word gevraagt om je geboortejaar en leeftijd intevullen.
        if ingevulde_leeftijd.isdigit() and ingevulde_geboortedatum.isdigit():
            return ingevulde_geboortedatum, ingevulde_leeftijd
#Hier heb ik de .isdigit sting gebruikt die waar is als je getallen gebruikt en niet waar als je letters gebruikt of anderen tekens. Ik heb ook and gebruikt die waar is als ze beiden waar zijn.
        else:
            print("Ongeldige invoer. Voer alleen cijfers in.")
#Dit word geprint als geboorte en leeftijd niet gelijk zijn.
ingevulde_geboortedatum, ingevulde_leeftijd = invullen_geboortejaar_leeftijd()
print("Ingevoerde geboortejaar:", ingevulde_geboortedatum)
print("Ingevoerde leeftijd:", ingevulde_leeftijd)
#Hier worden de functies uitgevoerd (dus ook getoond door het uitteprinten).

def ingevulde_leeftijd_gelijk_geboortejaar(geboortedatum, leeftijd):
    huidige_datum = datetime.datetime.now()
    geboortedatum = datetime.datetime.strptime(geboortedatum, "%Y")
    leeftijd_verjaardag_gepasseerd = (huidige_datum.month, huidige_datum.day) >= (geboortedatum.month, geboortedatum.day)
#Hier word de tijden aangegeven en gebruik ik >= en die zegd dat het waar is als het groter dan is.
    if huidige_datum.year - geboortedatum.year == int(leeftijd) and leeftijd_verjaardag_gepasseerd:
        print("Leeftijd en geboortejaar zijn geldig.")
        return True
#Hier word de huidigen datum(die gelijk is aan leeftijd) min geboortedatum en dat is gelijk aan leeftijd en dat is waar met de and aan leeftijd_verjaardag_gepasseerd.
    else:
        print("Leeftijd en geboortejaar zijn niet geldig.")
        return False
#Als het niet waar is is de leeftijd en geboortejaar niet gelijk dus niet geldig.
gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)
#gelijke_ongelijke_leeftij dat is ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd).
while not gelijke_ongelijke_leeftijd:
    print("U heeft een ongeldige combinatie van leeftijd en geboortejaar ingevoerd. Probeer eerst geboortejaar opnieuw en daarna leeftijd.")
#Als de gebruiker de verkeerde gelijke leeftijd en geboortejaar heeft ingevult word dit uitgeprint.
    ingevulde_geboortedatum, ingevulde_leeftijd = invullen_geboortejaar_leeftijd()
#De ingevulde geboortedatum en ingevulde leeftijd is ingevulde geeboortejaar leeftijd.
    gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)
#De gelijke ongelijke leeftijd is de ingevulde leeftijd, die gelijk is aan geboortejaar met de ingevulde geboortedtum en ingevulde leeftijd.
mylist = [ingevulde_geslacht, ingevulde_motivatiezin, ingevulde_achternaam, ingevulde_geboortedatum, ingevulde_leeftijd]
print("Ingevulde gegevens:", mylist)
#Hier word de lijst geprint met alle informatie.