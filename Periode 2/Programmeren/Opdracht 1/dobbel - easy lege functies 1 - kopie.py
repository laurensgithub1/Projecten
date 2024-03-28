import random
"""
        Programmeur J. Roode
        Datum: laatste revisie: 23-11-2022
        gitRepo:https://github.com/JGPROODE/python-workspace.git
        Import : random noodzakelijk
"""

def introduction():
    """
    input: geen
    output: geen
    wat doet de functie: zet tekst met uitleg van het spel op het scherm.
    """
    print("dit is een dobbelspel....etc etc")


def worpen(aantal):
    """
        Import : random noodzakelijk
        Input: een integer die het aantal worpen aangeeft
        Output: een lijst met worpen
        wat moet er gebeuren in de functie:
          Er wordt een random getal bepaald van (inclusief) 1 tot en met 6 en het resultaat 
          wordt in een lijst gezet.
          Dit wordt aantal keer herhaald
    """
    #hier komt de functieinhoud
    #lege lijst
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen

def bereken_score_easy(lijst):
    """
        Programmeur: J. Roode
        Datum: laatste revisie: 16-11-2022
        Import : geen
        Input: lijst met gehele getallen van 1 t/m 6, onbekende lengte
        Output: de score volgens de regels easy/medium/Yatzee
    """
    #hier komt de functie inhoud
    
    score=0
    return score


#hoofdprogramma
introduction()
#test --> aanroepen functie zodat wl=lijst met aantal worpen
aantalworpen=3
wl=worpen(aantalworpen)
#controle / test
print(wl,"aantal is :", aantalworpen)
print("het aantal worpen is :", len(wl))
  
#Test ==> berekenen van de score, resultaat op het scherm
print(bereken_score_easy(wl))

wl2=[2,6,2]
 
print("test -->",wl2,"===",bereken_score_easy(wl2), " moet zijn volgens Easy:  ", 16)


