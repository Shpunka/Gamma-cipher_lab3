alphabet = 'abcdefghijklmnopqrstuvwxyz'


def short_slogan(ciphertext: str, key: str):
    if len(ciphertext) != len(key):
        key_new = key * (len(ciphertext) // len(key) + 1)
        key_new = key_new[:len(ciphertext)]
    return key_new


def selfkey(alphabet: str, text: str, char: str):
    key = char + text
    key = key[:len(text)]
    return key


def selfkey_ciphertext(alphabet: str, text: str, char: str):
    ciphertext = text.lower()
    key_text = ''
    encode_array = []
    key_array = []
    key_array.append(alphabet.index(char))
    for i in range(len(ciphertext)):
        for j in range(len(alphabet)):
            if ciphertext[i] not in alphabet:
                encode_array.append(len(alphabet) + 1)
                break
            if ciphertext[i] == alphabet[j]:
                encode_array.append((alphabet.index(ciphertext[i]) + key_array[-1]) % len(alphabet))
                key_array.append(encode_array[-1])
    for j in key_array[:len(key_array) - 1]:
        key_text += alphabet[j]

    return key_text


def encode(alphabet: str, ciphertext: str, key: str):
    ciphertext = ciphertext.lower()
    key = key.lower()
    encode_text = ''
    encode_array = []
    for i in range(len(ciphertext)):
        for j in range(len(alphabet)):
            if ciphertext[i] not in alphabet:
                encode_array.append(len(alphabet) + 1)
                break
            if ciphertext[i] == alphabet[j]:
                encode_array.append(((alphabet.index(ciphertext[i]) +
                                      alphabet.index(key[i % len(key)])) % len(alphabet)))
    for i in encode_array:
        if i == len(alphabet) + 1:
            encode_text += ' '
        else:
            encode_text += alphabet[i]

    return encode_text


def decode(alphabet: str, ciphertext: str, key):
    ciphertext = ciphertext.lower()
    key = key.lower()
    decode_text = ''
    encode_array = []
    for i in range(len(ciphertext) - 1):
        for j in range(len(alphabet) - 1):
            if ciphertext[i] not in alphabet:
                encode_array.append(len(alphabet) + 1)
                decode_text += ciphertext[i]
                break
            if ciphertext[i] == alphabet[j]:
                encode_array.append((alphabet.index(ciphertext[i]) -
                                     alphabet.index(key[i])) % len(alphabet))
    for i in encode_array:
        if i == len(alphabet) + 1:
            decode_text += ' '
        else:
            decode_text += alphabet[i]

    return decode_text


stop = True

while stop:
    method = int(input('Выберите, что желаете сделать? \n1. Зашифровать \n2. Расшифровать\n'))
    if method == 1:
        text = input('Введите текст, который нужно зашифровать: \n')
        key = int(input(
            '1. Шифр Виженера с выработкой гаммы по короткому лозунгу \n2. Шифр Виженера с самоключом по открытому тексту\n'
            '3. Шифр Вижинера с самоключом по шифртексту\n '))
        if key == 1:
            key_input = input('Введите ключ: \n')
            print(f'Ваш ключ: {short_slogan(text, key_input)}')
            print(f'Зашифрованное сообщение: {encode(alphabet, text, short_slogan(text, key_input))}')
        elif key == 2:
            key_input = input('Введите ключ (одна буква): \n')
            print(f'Ваш ключ: {selfkey(alphabet, text, key_input)}')
            print(f'Зашифрованное сообщение: {encode(alphabet, text, selfkey(alphabet, text, key_input))}')
        elif key == 3:
            key_input = input('Введите ключ (одна буква): \n')
            print(f'Ваш ключ: {selfkey_ciphertext(alphabet, text, key_input)}')
            print(f'Зашифрованное сообщение: {encode(alphabet, text, selfkey_ciphertext(alphabet, text, key_input))}')
        else:
            raise ValueError('Выберите в пределах от 1 до 3. Другие значения неуместны')
    elif method == 2:
        text = input('Введите текст, который нужно расшифровать: \n')
        key = input('Введите ключ: \n')
        print(f'Сообщение: {decode(alphabet, text, key)}')
    else:
        raise ValueError("Введено некорректное значение.")
    print('Желаете продолжить или закрыть программу? \n')
    _ = input('Введите да или нет: \n')
    _.lower()
    if _ == 'нет':
        stop = False
