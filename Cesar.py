alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift):
    cipher = ""

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher, shift):
    decrypted = ""

    for letter in cipher:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
    message = 'Khairul'
    shift = 10
    cipher = encrypt(message, shift)
    decrypted = decrypt(cipher, shift)

    print('Original message: ' + message)
    print('Encrypted message: ' + cipher)
    print('Decrypted message: ' + decrypted)

main()