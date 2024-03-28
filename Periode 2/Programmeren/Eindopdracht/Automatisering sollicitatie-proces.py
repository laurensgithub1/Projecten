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
def invullen_motivatiezin():
    while True:
        motivatiezin = input("Voer hier uw motivatiezin in: ")
        if motivatiezin.replace(" ", "").isalpha():
            return motivatiezin
#Hier word de motivatiezin gevraagt waar de gebruiker het kan type. .isalpa zorgt ervoor dat je alleen maar letters kan type uit het alphabed en . replace (" ", "") zorgt er voor dat je spaties kan plaatsen.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties, maar geen cijfers of punten.")
#Als dat er niet aanvoldoet print hij ongeldige invoer.
def invullen_achternaam():
    while True:
        achternaam = input("Voer hier uw achternaam in: ")
        if achternaam.replace(" ", "").isalpha():
            return achternaam
#Hier word weer .replace(" ", "") en .isalpa gebruikt. De return aachternaam zorgt er voor dat de achternaam weer terug geroepen wordt.
        else:
            print("Ongeldige invoer. Voer alleen letters in en indien nodige spaties.")
#Als het er niet aanvoldoet ziet de gebruiker ongeldig invoer.
def invullen_geboortejaar_leeftijd():
    while True:
        ingevulde_geboortedatum = input("Voer hier uw geboortejaar: ")
        ingevulde_leeftijd = input("Voer hier uw leeftijd in die u momenteel bent als u al jarig bent geweest dit jaar, als u dit jaar nog niet jarig bent geweest voer dan de leeftijd in die u nog moet worden: ")
#Hier vult de gebruiker geboortejaar en leeftijd in.
        if ingevulde_leeftijd.isdigit() and ingevulde_geboortedatum.isdigit():
            return ingevulde_geboortedatum, ingevulde_leeftijd
#Hier heb ik de .isdigit sting gebruikt die waar is als je getallen gebruikt en niet waar als je letters gebruikt of anderen tekens. Ik heb ook and gebruikt die waar is als ze beiden waar zijn.
        else:
            print("Ongeldige invoer. Voer alleen cijfers in.")
#Als het niet goed is ingevuld door de gebruiker, dan krijgt de gebruiker te zien dat het ongeldig is ingevoerd.
def ingevulde_leeftijd_gelijk_geboortejaar(geboortedatum, leeftijd):
    huidige_datum = datetime.datetime.now()
    geboortedatum = datetime.datetime.strptime(geboortedatum, "%Y")
    leeftijd_verjaardag_gepasseerd = (huidige_datum.month, huidige_datum.day) >= (geboortedatum.month, geboortedatum.day)
#Hier word de tijden aangegeven en gebruik ik >= en die zegd dat het waar is als het groter dan is.
    if huidige_datum.year - geboortedatum.year == int(leeftijd) and leeftijd_verjaardag_gepasseerd:
        print("Leeftijd en geboortejaar zijn geldig.")
        return True
#Als het gelijk aan elkaar is het goed.
    else:
        print("Leeftijd en geboortejaar zijn niet geldig.")
        return False
#Anders als het niet gelijk is het fout.

with open("Automatisering sollicitatie-proces tekst.txt", "w") as file:
    ingevulde_geslacht = invullen_geslacht()
    file.write("Ingevulde geslacht: " + ingevulde_geslacht + "\n")
# Open the file in write mode ('W'). \n staat voor enter. as file zorgt voor de aangeven file.
    ingevulde_motivatiezin = invullen_motivatiezin()
    file.write("Ingevoerde motivatiezin: " + ingevulde_motivatiezin + "\n")
#file.write zorgt hier voor "Ingevoerde motivatiezin: " + ingevulde_motivatiezin + "\n" zo dat het in de file komt.
    ingevulde_achternaam = invullen_achternaam()
    file.write("Ingevoerde achternaam: " + ingevulde_achternaam + "\n")
#Zo komt er in de file de geschreven achternaam.
    ingevulde_geboortedatum, ingevulde_leeftijd = invullen_geboortejaar_leeftijd()
    file.write("Ingevoerde geboortejaar: " + ingevulde_geboortedatum + "\n")
    file.write("Ingevoerde leeftijd: " + ingevulde_leeftijd + "\n")
#Zo komt er in de file ingevule geboortedatum en leeftijd.
    gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)
    while not gelijke_ongelijke_leeftijd:
        print("U heeft een ongeldige combinatie van leeftijd en geboortejaar ingevoerd. Probeer eerst geboortejaar opnieuw en daarna leeftijd.")
#Als de leeftijd ongelijk is aan geboortejaar, dan word er bij de gebruiker aangegeven dat er een ongeldige combinatie is.
        ingevulde_geboortedatum, ingevulde_leeftijd = invullen_geboortejaar_leeftijd()
        gelijke_ongelijke_leeftijd = ingevulde_leeftijd_gelijk_geboortejaar(ingevulde_geboortedatum, ingevulde_leeftijd)
#Hier word gezegd dat ingevulde geboortejaat en ingevulde leeftijd, dat is invullen_geboortejaar_leeftijd.
    mylist = [ingevulde_geslacht, ingevulde_motivatiezin, ingevulde_achternaam, ingevulde_geboortedatum, ingevulde_leeftijd]
    file.write("Ingevulde gegevens: " + str(mylist) + "\n")
#Hier word alle ingevulde informatie van de functies in een lijst gezet in de file. 
print("Gegevens zijn succesvol opgeslagen in Automatisering sollicitatie-proces tekst.txt")
#Dit ziet de gebruiker als het goed is uitgevoerd.