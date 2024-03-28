import random
#Zo komt er een willekeurig getal.
def introduction():
    print("dit is het dobbelspel dit zijn de resultaten")
#Dit zorgt ervoor dat mensen bij het begin dit is het dobbelspel druk op enter te zien krijgen.
def worpen(aantal):
#Hiermee maak je een fuctie die je later kan gebruiken voor het aantal worpen.
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen
#Hiermee word een randomgetal van 1 tot 6 voor in de lijst gemaakt en for index in range herhaalt het aantal getallen.
def bereken_score_easy(lijst):
    score=0
    for getal in lijst:
        if getal==1:
            getal=0
        if getal==6:
            getal=12
        score=score+getal
    return score
#Hier word een functie aangamaakt waarmee de score van de lijstmetworpen goed berekend word.
introduction()
aantalworpen=3
wl=worpen(aantalworpen)
#Hier word de functie gebruikt dat het aantalwopren 3 is.
worpenlijst=worpen(3)
#Er zijn drie worpen in de worpenlijst.
for teller in range(1):
    worpenlijst=worpen(3)
    print("worp ",teller,"is : ",worpenlijst,"resultaat is: ",bereken_score_easy(worpenlijst))
#Dat for teller in range 1 dat zorgt dat het 1 keer word uitgevoerd en dat je een regel hebt met het antwoord en dat de resultaten worden uitgeprint.