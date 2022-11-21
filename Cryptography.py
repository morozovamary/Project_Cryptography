from random import randint

def Caesar_crypt(message):
    print('Введите шаг шифрования')
    shift = int(input())
    crypt_message = ''
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in message:
        letter = alphabet.find(i)
        new_letter = (letter + shift) % 33
        if i in alphabet:
            crypt_message += alphabet[new_letter]
        else:
            crypt_message += i
    file_out = (way_2, 'w')
    file_out.write(crypt_message)


def Caesar_decrypt(message):
    print('Введите шаг шифрования')
    shift = int(input())
    decrypt_message = ''
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in message:
        letter = alphabet.find(i)
        new_letter = (letter - shift + 33) % 33
        if i in alphabet:
            decrypt_message += alphabet[new_letter]
        else:
            decrypt_message += i
    file_out = (way_2, 'w')
    file_out.write(decrypt_message)


def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return (key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def Vigener_crypt(message):
    print('Введите ключ шифрования')
    key = str(input())
    key = generate_key(message, key)
    crypt_message = ''
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 33
        x += ord('А')
        crypt_message += chr(x)
    file_out = (way_2, 'w')
    file_out.write(crypt_message)


def Vigener_decrypt(message):
    print('Введите ключ шифрования')
    key = str(input())
    key = generate_key(message, key)
    decrypt_message = ''
    for i in range(len(message)):
        x = (ord(message[i]) - ord(key[i]) + 33) % 33
        x += ord('А')
        decrypt_message += chr(x)
    file_out = (way_2, 'w')
    file_out.write(crypt_message)



def Vernam_crypt(message):
    keys = ''
    crypt_message = ''
    for symbol in message:
        key = randint(0, 32)
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        keys += alphabet[key]
        crypt_message += chr((ord(symbol) + key - 17) % 33 + ord('А'))
    file_out = (way_2, 'w')
    file_out.write(crypt_message, '\n')
    file_out.write('Ключ шифрования: ', keys)


def Vernam_decrypt(message):
    print('Введите ключ шифрования: ')
    keys_in = str(input())
    keys = []
    for i in range(len(keys_in)):
        keys.append(alphabet.find(keys_in[i]))
    decrypt_message = ''
    for i, symbol in enumerate(message):
        if keys[i] != '':
            decrypt_message += chr((ord(symbol) - int(keys[i]) - 17) % 33 + ord('А'))
    file_out = (way_2, 'w')
    file_out.write(decrypt_message)


def frequency_analisys(message):
    letters = 0
    counter = 0
    shift = 0
    min_difference = 100
    difference = 0
    crypt_message = ''
    regular_frequency = [8.01, 1.59, 4.54, 1.70, 2.98, 8.45, 0.04, 0.97, 1.65, 7.35, 1.21, 3.49, 4.40,
                         3.21, 6.70, 10.97, 2.81, 4.73, 5.47, 6.26, 2.62, 0.26, 0.97, 0.48, 1.44, 0.73,
                         0.36, 0.04, 1.90, 1.74, 0.32, 0.64, 2.01]
    my_frequency = []
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in message:
        if i in alphabet:
            letters += 1
    for i in range(32):
        for j in range(len(message)):
            if alphabet[i] == message[j]:
                counter += 1
        my_frequency[i] = (counter / letters) * 100
    for i in range(32):
        difference += abs(my_frequency[i] ** 2 - regular_frequency[i] ** 2)
        if difference < min_difference:
            shift = i
            min_difference = difference
        difference = 0
    for i in message:
        letter = alphabet.find(i)
        new_letter = (letter + shift) % 33
        if i in alphabet:
            crypt_message += alphabet[new_letter]
        else:
            crypt_message += i
    file_out = (way_2, 'w')
    file_out.write(crypt_message)



def communication_with_user():
    print('Введите адрес сообщения для обработки')
    way_in = str(input())
    file_in = open(way_in,'r')
    text = file_in.read().splitelines()
    message = ''
    for i in range(len(text)):
        message = message + text[i].upper() + ' '
    print('Введите адрес для обработанного сообщения')
    way_out = str(input())
    print('Вы хотите зашифровать или дешифровать сообщение?')
    if str(input()) == 'зашифровать':
        crypt = True
    else:
        crypt = False

    print('Выберете предпочтительный способ шифрования: шифр Цезаря, шифр Виженера или шифр Вернама')
    type_of_crypt = str(input())
    if type_of_crypt == 'шифр Цезаря':
        if crypt:
            Caesar_crypt(message)
        else:
            print('Выберете предпочтительный способ взлома: классический или частотный анализ')
            type_of_hacking = str(input())
            if type_of_hacking == 'классический':
                Caesar_decrypt(message)
            else:
                requency_analisys(message)
    elif type_of_crypt == 'шифр Виженера':
        if crypt:
            Vigener_crypt(message)
        else:
            Vigener_decrypt(message)
    elif type_of_crypt == 'шифр Вернама':
        if crypt:
            Vernam_crypt(message)
        else:
            Vernam_decrypt(message)

communication_with_user()









