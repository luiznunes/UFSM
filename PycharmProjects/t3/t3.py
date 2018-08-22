import random
import string


def encrypt(msg):
    list_msg = list(msg)
    encrypted = ""
    for i in range(len(list_msg)):
        char = msg[i].lower()
        if char == ' ':
            encrypted += char
        else:
            index = homophon[0].index(char)
            s = 0
            for j in range(len(homophon)):
                if homophon[j][index] != "-":
                    s += len(homophon[j][index])
            encrypted += homophon[random.randint(1, s - 1)][index]

    return encrypted


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def create_transposition():
    matrix = [list(key.upper())]
    size = len(key)
    new_message = ''.join(e for e in message if e.isalnum()).upper()
    for msg in list(chunks(new_message, size)):
        tmp = []
        for l in msg:
            tmp.append(l)

        while len(tmp) < size:
            tmp.append(random.choice(alphabet))

        matrix.append(tmp)

    return matrix


def modify_cipher():
    modified_cipher = []

    for letter in alphabet:
        if letter in transposed[0]:
            tmp = []
            index = transposed[0].index(letter)
            for row in range(1, len(transposed)):
                tmp.append(transposed[row][index])
            modified_cipher.append(tmp)

    return modified_cipher


def convert_to_string(modified_cipher):
    tmp_cipher = []

    for n_cipher in modified_cipher:
        tmp_cipher.append(''.join(n_cipher))

    str_cipher = ' '.join(tmp_cipher)

    return str_cipher


def convert_message(modified_message):
    tmp_msg = []

    modified_message = chunks(modified_message.replace(',', ''), len(key)-1)

    for n_msg in modified_message:
        tmp_msg.append(''.join(n_msg))

    str_cipher = ' '.join(tmp_msg)

    return str_cipher


def create_homophon():
    matrix = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
              ['8', 'F', 'H', 'G', '3', 'l', '1', 'L', 'E', 'I', 'w', 'o', 'M', 'X', '6', 'Q', 'P',
               'b', 'V', '9', 'a', 'Z', 'S', 'D', 'j', 'r'],
              ['z', '-', 'k', 'm', 'x', 'n', 'B', 'u', '0', '-', '-', 'O', 'A', 'v', '5', 'p', '-',
               'R', 'y', 'f', '4', 'g', '-', '-', '-', '-'],
              ['K', '-', 's', 'N', 'q', '-', '-', '-', 'J', '-', '-', 'a', 'c', '-', '2', '-', '-',
               'T', 'e', 'Y', 'h', '-', '-', '-', '-', '-'],
              ['7', '-', '-', '-', 't', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'W', '-', '-',
               'C', '-', '-', '-', '-', '-', '-', '-', '-']]

    return matrix


message = ""
alphabet = string.ascii_uppercase

while True:
    message = input("Type the message: ")
    if len(message) < 200:
        break
    print("Message too long!")

key = input("Type the key: ")

transposed = create_transposition()
res_transposed = modify_cipher()
new_cipher = convert_to_string(res_transposed)
homophon = create_homophon()
encrypted_cipher = encrypt(new_cipher)
encrypted_message = encrypt(convert_message(''.join(e for e in message if e.isalnum()).upper()))

print("Original message: " + message)
print("Key: " + key)
print("\nTransposed message:\n")

for c in convert_to_string(transposed).split(" "):
    print("\t" + "\t" + ' '.join(c))

print("\nCiphered message: " + new_cipher)
print("\nHomophon matrix:\n")

for c in convert_to_string(create_homophon()).split(" "):
    print("\t" + "\t" + ' '.join(c))
print("\n")

print("Encrypted Cipher")
print(encrypted_cipher)
print("Encrypted Message")
print(encrypted_message)
