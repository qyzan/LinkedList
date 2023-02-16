alphabet = "abcdefghijklmnopqrstuvwxyz"

pesan_ke_index = dict(zip(alphabet, range(len(alphabet))))
index_ke_pesan = dict(zip(range(len(alphabet)), alphabet))


def encrypt(pesan, key):
    cipher = ""

    for x in pesan :
        index = (pesan_ke_index[x] + key) % len(pesan_ke_index)
        huruf = index_ke_pesan[index]
        cipher += huruf

    return cipher


def decrypt(cipher, key):
    decrypted = ""

    for x in cipher :
        index = (pesan_ke_index[x] - key) % len(pesan_ke_index)
        huruf = index_ke_pesan[index]
        decrypted += huruf

    return decrypted


def kirim():
    Pesan = 'qyzan'.lower()
    Key = 10
    Kirim = encrypt(Pesan, Key)
    Kirim2 = decrypt(Kirim, Key).title()
    
    print('Hasil enkripsi : ', Kirim)
    print('Hasil dekripsi : ', Kirim2)
kirim()