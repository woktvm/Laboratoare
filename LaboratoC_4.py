from secrets import token_bytes

def left_shift(bits, n):
    return bits[n:] + bits[:n]

PC1 = [ #lipsesc bitii de paritate 8, 16, 24, 32, 40, 48, 56, 64
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
key = token_bytes(8)
key = ''.join(f'{byte:08b}' for byte in key)
print(key)
i = int(input("Cate runde de permutare pentru cheie?"))
K_plus = ''.join(key[i-1] for i in PC1)
print(K_plus)
C0 = K_plus[:28]
D0 = K_plus[28:]
C,D = C0, D0
d=1
for round in range(i):
    C = left_shift(C, shifts[round])
    D = left_shift(D, shifts[round])
    print(f"C{d} =", C)
    print(f"D{d} =", D)
    d+=1;
