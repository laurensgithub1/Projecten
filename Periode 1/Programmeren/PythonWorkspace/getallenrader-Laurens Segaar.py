import random
#Dat zorgt er voor dat er een willekeurige getal komt.
max_getal = int (input("Wat is het maxgetal?"))
#Zo kan de speler het maximalen getal aangeven waar hij tussen de 0 en het maximale getal moet schatten.
Aantal_keer_schatten = int (input("Hoeveel keer schatten?"))
#Zo geeft de speler aan hoe vaak hij moet schatten.
random_getal = random.randint(1, max_getal)
#Zo word er een random getal gegereneerd.
print(input("ben je klaar om te beginnen?"))
#Zo ziet de speler de vraag of je klaar bent om te beginnen.
for x in range(0,40):
    print("")
#Dit zorgt voor de loop (dus dat het elke keer opnieuw loopt).
player2_denkt=-99
while player2_denkt!=random_getal and Aantal_keer_schatten>0:
    player2_denkt = int (input("Welk getal denk je?"))
    #Zo kan de speler het getal invullen dat hij denkt en word de loop op een goeden manier gestopt.
    Aantal_keer_schatten -= 1
    #Zo gaat er elke keer een beurt af als een speler geschat heeft.
    if player2_denkt < random_getal:
        print ("Te laag geschat probeer het nog een keer.")
    #Zo ziet de speler dat hij te laag heeft geschat.
    print("je hebt {} beurten over".format(Aantal_keer_schatten))
    if player2_denkt > random_getal:
        print ("Te hoog geschat probeer het nog een keer.")
    #Zo ziet de speler dat hij te hoog heeft geschat. En zo ziet hij hoeveel beurten hij over heeft.
    if player2_denkt == random_getal:
        print ("Goed gedaan je hebt het getal goed geschat.")
        #break FOOOOOEI!!!!!
    #Zo ziet de speler of hij het goed heeft gedaan.
    if Aantal_keer_schatten == 0:
        print ("Helaas zijn je beurten op.")
        print ("het getal was {}" .format(random_getal))
        #break
    #Zo ziet de speler of zijn beurten op zijn zo ziet de speler ook wat het getal was. En is er een einden aan de loop met break.