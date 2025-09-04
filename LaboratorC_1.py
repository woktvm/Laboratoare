def encrypt(text, alfabet, key):  # criptarea cu o singura cheie
    result = ""
    for litera in text:
        criptograma = (alfabet.index(litera) + key) % len(alfabet)
        result += alfabet[criptograma]
    return result


def encryptalfa(alfabet, key2):  # crearea noului alfabet pentru criptare
    result = ""
    newalfa = key2 + alfabet
    for litera in newalfa:
        if litera not in result:
            result += litera
    return result


def encrypt2(text, newalfa, key):  # criptarea cu 2 chei
    result = ""
    for litera in text:
        criptograma = (newalfa.index(litera) + key) % len(newalfa)
        result += newalfa[criptograma]
    return result


def decrypt(mesajul1, alfabet, key):  # decriptarea cu o singura cheie
    result = ""
    for litera in mesajul1:
        criptograma = (alfabet.index(litera) - key) % len(alfabet)
        result += alfabet[criptograma]
    return result


def decryptalfa(mesajulalfa, newalfa, key):  # decriptarea cu 2 chei
    result = ""
    for litera in mesajulalfa:
        criptograma = (newalfa.index(litera) - key) % len(newalfa)
        result += newalfa[criptograma]
    return result


alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print("Alegeti 1.Criptare sau 2.Decriptare: ")
choice = input()
while True:
    print("Mesajul: ")
    text = input().upper()
    text = text.replace(" ", "")
    valid = True
    for litera in text:
        if litera not in alfabet:
            print(
                "Textul contine unul sau mai multe caractere ilegale folositi litere A - Z sau a-z"
            )
            valid = False
            break
    if valid == True:
        break


while True:  # repeta intrebarea cheii
    print("Cheia:")
    key = int(input())
    if key >= 26 or key < 0:
        print(
            "Introduce o cheie cu un numar al unei litere alfabet("
            + str(len(alfabet))
            + ")"
        )
        key = int(input())
    else:
        break
while True:  # repeta intrebarea cheii alfabetice
    print("Cheia alfabetica: ")
    key2 = input().upper()
    valid = True
    for litera in key2:
        if litera not in alfabet:
            print(
                "Textul contine unul sau mai multe caractere ilegale folositi litere A - Z sau a-z"
            )
            valid = False
            break
    if valid == True:
        break
    if len(key2) == 0:
        break
    elif len(key2) < 7:
        print("Introduceti o cheie mai lunga")

newalfa = encryptalfa(alfabet, key2)  # creaza alfabetul cu cheia speciala
if choice == "2" and len(key2) != 0:
    mesajdec = decryptalfa(text, newalfa, key)
    print(mesajdec)
elif choice == "2" and len(key2) == 0:
    mesajdec = decrypt(text, alfabet, key)
    print(mesajdec)
else:
    if len(key2) != 0:  # daca are cheie alfabetica
        mesajulalfa = encrypt2(text, newalfa, key)
        print(mesajulalfa)
        mesajulalfadec = decryptalfa(mesajulalfa, newalfa, key)
        print("Doriti decriptarea mesajului:")
        raspuns = input().lower()
        if raspuns == "da":
            print("Mesajul initial este: " + mesajulalfadec)
    else:
        mesajul1 = encrypt(text, alfabet, key)
        print(mesajul1)
        mesajul2 = decrypt(mesajul1, alfabet, key)
        print("Doriti decriptarea mesajului:")
        raspuns = input().lower()
        if raspuns == "da":
            print("Mesajul initial este: " + mesajul2)