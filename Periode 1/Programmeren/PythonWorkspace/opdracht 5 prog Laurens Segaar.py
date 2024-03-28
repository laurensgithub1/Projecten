#deze functie telt de waarden bij elkaar op vanaf beginwaarde tot en met eindwaarde
#het resultaat wordt geretourneerd(teruggegeven)


def tel_op(bw,ew):
    teller=bw 
    resultaat=0
    while teller<=ew:
        resultaat=resultaat+teller
        teller+=1
    return resultaat

print(tel_op(0,100))