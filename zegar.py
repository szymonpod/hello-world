h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))
#d = duration = czas trwania
minuty = (m + d) % 60
godziny = int(h + (m + d) / 60) % 24
print(hours,":",minutes)
