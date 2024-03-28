import random


def worpen(aantal):
    #hier komt de functieinhoud
    #lege lijst
    lijstmetworpen=[]
    for index in range(aantal):
        lijstmetworpen.append(random.randint(1,6))
    return lijstmetworpen