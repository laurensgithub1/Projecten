def invullen_achternaam():
  while True:
        achternaam = input("Voer hier uw achternaam in: ")
        if achternaam.isalpha():
            return achternaam
#islapha is een string method die ik vond tussen de string methods in w3schools en isalpa kijkt of alle tekens in het alphabed zitten en kijkt of het waar is.
        else:
            print("Ongeldige invoer. Voer alleen letters in.")

ingevulde_achternaam = invullen_achternaam()
print("Ingevoerde achternaam:", ingevulde_achternaam)