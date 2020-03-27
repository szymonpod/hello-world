dochód = float(input("Wprowadź roczny dochód: "))
if dochód <= 85528:
    podatek = ((0.18*dochód)-556.2)
else:
    podatek = (14839.2+(0.32*85528))
podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)