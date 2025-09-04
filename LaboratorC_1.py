def encrypt(text, alfabet, key): #encriptarea cu o singura cheie
    result = ""
    for litera in text:
        if litera.lower() in alfabet:
            criptograma = (alfabet.index(litera.lower()) + key) % len(alfabet)
            if litera.isupper(): #daca caracterul e mare va ramane mare
                result += alfabet[criptograma].upper()
            else: #daca e simbol ramane la fel
                result += alfabet[criptograma]
        else:
            result += litera
    return result

def encryptalfa(alfabet, key2): #crearea noului alfabet pentru criptare
    result = ""
    newalfa = key2+alfabet
    for litera in newalfa:
        if litera not in result:
            result += litera
    return result

def encrypt2(text, newalfa, key): #encriptarea cu 2 chei
    result = ""
    for litera in text:
        if litera.lower() in newalfa:
            criptograma = (newalfa.index(litera.lower()) + key) % len(newalfa)
            if litera.isupper():
                result += newalfa[criptograma].upper()
            else:
                result += newalfa[criptograma]
        else:
            result += litera
    return result



def decrypt(mesajul1, alfabet, key): #decriptarea cu o singura cheie
    result = ""
    for litera in mesajul1:
        if litera.lower() in alfabet:
            criptograma = (alfabet.index(litera.lower()) - key) % len(alfabet)
            if litera.isupper():
                result += alfabet[criptograma].upper()
            else:
                result += alfabet[criptograma]
        else:
            result += litera
    return result

def decryptalfa(mesajulalfa, newalfa, key): #decriptarea cu 2 chei
    result = ""
    for litera in mesajulalfa:
        if litera.lower() in newalfa:
            criptograma = (newalfa.index(litera.lower()) - key) % len(newalfa)
            if litera.isupper():
                result += newalfa[criptograma].upper()
            else:
                result += newalfa[criptograma]
        else:
            result += litera
    return result
 
 
alfabet = 'abcdefghijklmnopqrstuvwxyz'
print("Mesajul: ")
text = input()
while True: #repeta intrabarea cheii
        print("Cheia:")
        key = int(input())
        if key >= 26 or key <0:
            print("Introduce o cheie cu un numar al unei litere alfabet(" + str(len(alfabet)) + ")")
            key = int(input())
        else:
            break
while True: #repeta intrabarea cheii alfabetice
    print("Cheia alfabetica: ")
    key2 = input()
    if int(str(len(key2))) == 0:
        break
    if int(str(len(key2))) <7:
        print("Introduceti o cheie mai lunga")
    else:
        break

if str(len(key2)) != 0: #daca are cheie alfabetica
    newalfa = encryptalfa(alfabet,key2)
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

