def CitireLista():
    lst = []
    listaString = input("Dati numerele intregi:")
    numarString = listaString.split(",")
    for x in numarString:
        lst.append(int(x))
    return lst

def AfisareaNumerelorNegative(lst):
    '''
    Afiseaza numerele negative din lista nenule
    :param lst: lista initiala
    :return: noua lista cu proprietatea ceruta
    '''

    new_lst = []
    for x in lst:
        if x < 0:
            new_lst.append(x)
    return new_lst

def test_AfisareaNumerelorNegative():
    assert AfisareaNumerelorNegative([-1,3,6,-2]) == [-1,-2]
    assert AfisareaNumerelorNegative([0,1,3,-3,-9,8,-15]) == [-3,-9,-15]


def CeaMaiMicaCifra(n,lst):
    '''
    :param n: cifra data
    :param lst: lista in care lucram
    :return: numarul cerut
    '''

    new_lst = []
    for x in lst:
        if x % 10 == n:
            new_lst.append(x)
    new_lst.sort()
    return new_lst[:1]


def test_CeaMaiMicaCifra():
    assert CeaMaiMicaCifra(6,[13,29,16,56,76]) == 16
    assert CeaMaiMicaCifra(9,[13,17,39,45,69,89]) == 39


def isPrime(x):
    '''
    determina daca un nr este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau Flase in caz contrar
    '''

    if x < 2:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True


def is_SuperPrime(x):
    '''
    determina daca un nr e superprim
    :param x: un numar intreg
    :return: True daca numarul e superprim sau False in caz contrar
    '''
    if x < 0:
        return False
    k=1
    while x > 0:
        if isPrime(x):
            k = 1
            x = x//10
        else:
            k = 0
    if k == 1:
        return True
    elif k == 0:
        return False


def AfisareListaSuperprime(lst):
    '''
    Afiseaza o noua lista care contine toate numerele superprime din lista initiala
    :param lst: lista initiala
    :return: noua lista cu numere superprime
    '''

    new_lst = []
    for x in lst:
        if is_SuperPrime(x):
            new_lst.append(x)
    return new_lst


def test_AfisareListaSuperprime():
    AfisareListaSuperprime([8,16,32,239]) == [239]
    AfisareListaSuperprime ([23,64,68,71]) == [23,71]


def main():
    test_AfisareListaSuperprime()
    test_CeaMaiMicaCifra()
    test_AfisareaNumerelorNegative()
    lst = []
    while True:
        print ("1. Citirea unei liste de numere întregi.")
        print ("2. Afișarea tuturor numerelor negative nenule din listă (de ex. -1, -56).")
        print ("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
        print ("4. Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este strict pozitiv și toate prefixele sale sunt prime.")
        print ("5. Exit")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst=CitireLista()
        elif optiune == "2":
            print (AfisareListaSuperprime(lst))
        elif optiune == "3":
            n = int(input("Dati cifra: "))
            print (CeaMaiMicaCifra(n,lst))
        elif optiune == "4":
            print (AfisareListaSuperprime(lst))
        elif optiune == "5":
            break
        else:
            print ("Optiune gresita. Reincercati")

main()