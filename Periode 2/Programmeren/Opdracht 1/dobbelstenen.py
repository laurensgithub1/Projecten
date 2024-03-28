import random


def worpen(aantal):
    #hier komt de functieinhoud
    #lege lijst
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen


print(worpen(3000))

def telogen(wl):
    ogenteller=[]
    eenteller=0
    tweeteller=0
    drieteller=0
    vierteller=0
    vijfteller=0
    zesteller=0

    for worp in wl:
        if worp==1:
            eenteller+=1
        if worp==2:
            tweeteller+=1
        if worp==3:
            drieteller+=1
        if worp==4:
            vierteller+=1
        if worp==5:
            vijfteller+=1
        if worp==6:
            zesteller+=1
    ogenteller.append(eenteller)
    ogenteller.append(tweeteller)
    ogenteller.append(drieteller)
    ogenteller.append(vierteller)
    ogenteller.append(vijfteller)
    ogenteller.append(zesteller)
    return ogenteller


print("Dit is het aaantal ogen:",telogen(worpen(10)))