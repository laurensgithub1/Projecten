def vraagWeekdag():
    #hier wordt de code geschreven om de weekdag te vragen
    weekdag=-99
    while not(weekdag>=1 and weekdag<=7):
        weekdag = int(input("Welke dag van de week is het"))
    #print("dit is vraagweekdag")
    return weekdag


dag=vraagWeekdag()
print(dag)