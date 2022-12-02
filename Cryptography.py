from random import randint


class Const:
    alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    len_of_alphabet = 32
    regular_frequency = [8.01, 1.59, 4.54, 1.70, 2.98, 8.45, 0.04, 0.97, 1.65, 7.35, 1.21, 3.49, 4.40,
                         3.21, 6.70, 10.97, 2.81, 4.73, 5.47, 6.26, 2.62, 0.26, 0.97, 0.48, 1.44, 0.73,
                         0.36, 0.04, 1.90, 1.74, 0.32, 0.64, 2.01]
    order_first_russian_letter = 1040
    order_last_russian_letter = 1105
    vernam_shift = 16


def get_message(way_in):
    with open(way_in, 'r', encoding="utf-8") as f:
        text = f.readlines()
    message = ''
    for i in text:
        string = i
        if string[-1] == '\n':
            string = string[:-1]
        message = message + string + ' '
    return message


def caesar_crypt(way_in, key):
    message = get_message(way_in)
    crypt_message = ''
    for i in message:
        if i.islower():
            letter = Const.alphabet_lower.find(i)
        else:
            letter = Const.alphabet_upper.find(i)
        new_letter = (letter + int(key)) % Const.len_of_alphabet
        if i in Const.alphabet_upper:
            crypt_message += Const.alphabet_upper[new_letter]
        elif i in Const.alphabet_lower:
            crypt_message += Const.alphabet_lower[new_letter]
        else:
            crypt_message += i
    with open(way_in, 'a', encoding="utf-8") as f:
        f.write('\n' + "Зашифрованное сообщение: " + crypt_message)


def caesar_decrypt(way_in, key):
    message = get_message(way_in)
    decrypt_message = ''
    for i in message:
        if i.islower():
            letter = Const.alphabet_lower.find(i)
        else:
            letter = Const.alphabet_upper.find(i)
        new_letter = (letter - int(key) + Const.len_of_alphabet) % Const.len_of_alphabet
        if i in Const.alphabet_upper:
            decrypt_message += Const.alphabet_upper[new_letter]
        elif i in Const.alphabet_lower:
            decrypt_message += Const.alphabet_lower[new_letter]
        else:
            decrypt_message += i
    print(decrypt_message)
    with open(way_in, 'a', encoding="utf-8") as f:
        f.write('\n' + "Расшифрованное сообщение: " + decrypt_message)


def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return (key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def vigener_crypt(way_in, key):
    message = get_message(way_in)
    key = generate_key(message, key)
    key_upper = key.upper()
    key_lower = key.lower()
    crypt_message = ''
    for i in range(len(message)):
        if ord(message[i]) < Const.order_first_russian_letter or ord(message[i]) > Const.order_last_russian_letter:
            crypt_message += message[i]
        else:
            if message[i].islower():
                x = (ord(message[i]) + ord(key_lower[i]) - 1) % Const.len_of_alphabet + ord('а')
            else:
                x = (ord(message[i]) + ord(key_upper[i]) + 1) % Const.len_of_alphabet + ord('А')
            crypt_message += chr(x)
    with open(way_in, 'a', encoding="utf-8") as f:
        f.write('\n' + "Зашифрованное сообщение: " + crypt_message)


def vigener_decrypt(way_in, key):
    message = get_message(way_in)
    key = generate_key(message, key)
    key_upper = key.upper()
    key_lower = key.lower()
    decrypt_message = ''
    for i in range(len(message)):
        if ord(message[i]) < Const.order_first_russian_letter or ord(message[i]) > Const.order_last_russian_letter:
            decrypt_message += message[i]
        else:
            if message[i].islower():
                x = (ord(message[i]) - ord(key_lower[i]) + 1) % Const.len_of_alphabet + ord('а')
            else:
                x = (ord(message[i]) - ord(key_upper[i]) - 1) % Const.len_of_alphabet + ord('А')
            decrypt_message += chr(x)
    with open(way_in, 'a', encoding="utf-8") as f:
        f.write('\n' + "Расшифрованное сообщение: " + decrypt_message)


def vernam_crypt(way_in):
    message = get_message(way_in)
    crypt_message = ''
    keys_upper = ''
    keys_lower = ''
    for i in range(len(message) - 1):
        symbol = message[i]
        key = randint(0, Const.len_of_alphabet - 1)
        keys_upper += Const.alphabet_upper[key]
        keys_lower += Const.alphabet_lower[key]
        if ord(message[i]) < Const.order_first_russian_letter or ord(message[i]) > Const.order_last_russian_letter:
            crypt_message += message[i]
        else:
            if message[i].islower():
                crypt_message += chr((ord(symbol) + key - Const.vernam_shift) % Const.len_of_alphabet + ord('а'))
            else:
                crypt_message += chr((ord(symbol) + key - Const.vernam_shift) % Const.len_of_alphabet + ord('А'))
    with open(way_in, 'w', encoding="utf-8") as f:
        f.write('\n' + 'Зашифрованное сообщение: ' + crypt_message + '\n')
        f.write('Ключ шифрования: ' + keys_upper)


def decryption(message, keys_lower, keys_upper):
    decrypt_message = ''
    for i, symbol in enumerate(message):
        if ord(message[i]) < Const.order_first_russian_letter or ord(message[i]) > Const.order_last_russian_letter:
            decrypt_message += message[i]
        else:
            if message[i].islower():
                if i < len(keys_lower):
                    if keys_lower[i] != '':
                        decrypt_message += chr((ord(symbol) - int(keys_lower[i]) - Const.vernam_shift) %
                                               Const.len_of_alphabet + ord('а'))
            else:
                if i < len(keys_upper):
                    if keys_upper[i] != '':
                        decrypt_message += chr((ord(symbol) - int(keys_upper[i]) - Const.vernam_shift) %
                                               Const.len_of_alphabet + ord('А'))
    return decrypt_message


def vernam_decrypt(way_in, key):
    message = get_message(way_in)
    keys_in_lower = key.lower()
    keys_in_upper = key.upper()
    keys_upper = []
    keys_lower = []
    for i in range(len(keys_in_lower)):
        keys_upper.append(Const.alphabet_upper.find(keys_in_upper[i]))
        keys_lower.append(Const.alphabet_lower.find(keys_in_lower[i]))
    decrypt_message = decryption(message, keys_lower, keys_upper)
    with open(way_in, 'a', encoding="utf-8") as f:
        f.write('\n' + 'Расшифрованное сообщение: ' + decrypt_message)


def my_frequency_fill(message, min_difference):
    shift = 0
    letters = 0
    my_frequency = []
    for i in message:
        if i in Const.alphabet_upper:
            letters += 1
    for i in range(Const.len_of_alphabet):
        counter = 0
        for j in range(len(message)):
            if Const.alphabet_upper[i] == message[j]:
                counter += 1
        my_frequency.append((counter / letters) * 100)
    for i in range(Const.len_of_alphabet):
        difference = 0
        for j in range(Const.len_of_alphabet):
            difference += (my_frequency[j] - Const.regular_frequency[(i + j) % Const.len_of_alphabet]) ** 2
        if difference < min_difference:
            shift = i
            min_difference = difference
    return shift


def decrypt_frequency_analysis(message, original, shift):
    crypt_message = ''
    counter = 0
    for i in message:
        letter = Const.alphabet_upper.find(i)
        new_letter = (letter + shift - 1) % Const.len_of_alphabet
        if i in Const.alphabet_upper:
            if original[counter].islower():
                crypt_message += Const.alphabet_lower[new_letter]
            else:
                crypt_message += Const.alphabet_upper[new_letter]
        else:
            crypt_message += i
        counter += 1
    return crypt_message


def frequency_analisys(file_in):
    with open(file_in, 'r', encoding="utf-8") as f:
        text = f.readlines()
    original = ''
    message = ''
    for i in range(len(text)):
        original = original + text[i]
        message = message + text[i].upper()
    min_difference = 100000000
    shift = my_frequency_fill(message, min_difference)
    crypt_message = decrypt_frequency_analysis(message, original, shift)
    with open(file_in, 'a', encoding="utf-8") as f:
        f.write('\n' + 'Расшифрованное сообщение: ' + crypt_message)
