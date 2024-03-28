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