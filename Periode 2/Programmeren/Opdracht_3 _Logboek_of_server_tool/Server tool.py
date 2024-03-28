import datetime
#Zo word er een dagtijd opgehaalt)
x = datetime.datetime.now()
datum = x.strftime("%d/%m/%Y %H:%M:%S")
#Zo word de datum van nu gepakt, word de dag, maand, jaar en tijd in uren, minuten en seconden gepakt.
f = open("demofile4.txt", "a")
#De f staat voor file en daar mee opend hij de goeden file.
invoergebruiker=""
tekst=""
# Dat is de tekst waar de gebruiker gaat invullen.
while invoergebruiker!= "stop":
    invoergebruiker=input("toets een regel in die u in het bestand wil oplsaan en schrijf stop als u klaar bent met wat u wilt opslaan.").lower()
    if invoergebruiker.lower()!="stop":
        
        tekst=tekst+"\n"+invoergebruiker
    else :
        tekst=tekst+" "+ datum
#Als de invoergebruiker stop zegt, dan is het niet gelijk door != daar door stopt hij met verder type als de invoergebruiker stop typt.
#invoergebruiker=input zo dat de gebruiker kan invullen wat hij/zij wilt opslaan.
#invoergebruiker lower zorg er voor dat de tekst van stop in kleien letter komt zo dat het werkt als dat nodig is.
#anders is de tekst de ingevulden tekst met de datum.
print("dit is de tekst:", tekst)
f.write(tekst)
f.close()
#hij print de tekst zo dat je het ziet.
#f.write tekst zorgt er voor dat je het kan schrijven in het document.
#f.close zogt er voor dat het document dicht gaat.