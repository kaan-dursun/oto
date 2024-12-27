import random

# Liste oluşturuluyor
kuralistesi = []
k = "kaan"
u = "umut"
m = "melih"
mu = "murat"
c = "celal"
d="Yildiray"
kuralistesi.append(k)
kuralistesi.append(u)
kuralistesi.append(m)
kuralistesi.append(mu)
kuralistesi.append(c)
kuralistesi.append(d)
takimlar = []
b = "barcelona"
c = "city"
r = "real"
ba = "bayern"
l = "liverpool"
o="fenerbahce"
takimlar.append(b)
takimlar.append(c)
takimlar.append(r)
takimlar.append(ba)
takimlar.append(l)
takimlar.append(o)
a=0
while(a<=6):
# Kura çekimi
    kazanan = random.choice(kuralistesi)
    takim= random.choice(takimlar)
    print( kazanan,takim)
    kuralistesi.remove(kazanan)
    takimlar.remove(takim)
    a+=1