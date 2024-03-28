import random

def introduction():
    print("dit is het dobbelspel druk op enter")

def worpen(aantal):
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen

def bereken_score_easy(lijst):
    score=0
    for getal in lijst:
        if getal==1:
            getal=0
        if getal==6:
            getal=12
        score=score+getal
    return score
introduction()
aantalworpen=3
wl=worpen(aantalworpen)

#worplijst2=[1,6,1]
#print("test -->",worplijst2,"===",bereken_score_easy(worplijst2), " moet zijn volgens Easy:  ", 12)

def worpen(aantal):
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen
#wl2 = print(bereken_score_easy(wl))
#print("test -->",wl2,"===",bereken_score_easy(wl2), " moet zijn volgens Easy:  ", 16)