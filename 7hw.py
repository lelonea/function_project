def dum(a):
    sm1 = a * 2.54
#    print(sm1)
    return sm1


def sm(a):
    dum1 = a / 2.54
#    print(dum1)
    return dum1


def milya(a):
    km1 = a * 1.609
#    print(km1)
    return km1


def km(a):
    milya1 = a / 1.609
#    print(milya1)
    return milya1


def funt(a):
    kg1 = a / 2.205
#    print(kg1)
    return kg1

def kg(a):
    funt1 = a * 2.205
#    print(funt1)
    return funt1


def unc(a):
    g1 = a * 28.35
#    print(g1)
    return g1


def g(a):
    unc1 = a / 28.35
#    print(unc1)
    return unc1


def gal(a):
    l1 = a / 3.785
#    print(l1)
    return l1


def l(a):
    gal1 = a * 3.785
#    print(gal1)
    return gal1


def pint(a):
    litr1 = a * 2.113
#    print(litr1)
    return litr1


def litr(a):
    pint1 = a / 2.113
#    print(pint1)
    return pint1



while True:
    b = input('choose number:  ')
    b = int(b)
    if b == 0:
        break
    a = input('number:  ')
    a = int(a)
    c = [dum(a), sm(a), milya(a), km(a), funt(a), kg(a), unc(a), g(a), gal(a), l(a), pint(a), litr(a)]
    print(c[b-1])

