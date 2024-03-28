

def geslacht_invullen():
    geslacht = input("Wat is uw geslacht (man, vrouw of overig)? ").lower()

    # Dit is de ingevulde informatie van de gebruiker.
    while geslacht != [man, vrouw, overig]:
        print("Geslacht fout ingevuld:", geslacht)
        geslacht = input("Wat is uw geslacht (man, vrouw of overig)? ").lower()


# Als het geslacht juist is ingevuld, print het geslacht.
print("Geslacht correct ingevuld:", geslacht)