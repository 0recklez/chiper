ALPH_EN = 'abcdefghijklmnopqrstuvwxyz'
ALPH_EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPH_RU = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ALPH_RU_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def is_valid():
    while True:
        num = input('введите сдвиг: ')
        if num.isdigit() and int(num) > 0:
            return int(num)
        print('введите целое, положительное число')


def crypt_or_decrypt(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ('crypt', 'decrypt'):
            return choice
        print('команда не найдена')


def check_language(lang):
    while True:
        choice = input(lang).lower()
        if choice in ("ru", "eng"):
            return choice
        print("введите 'ru' или 'eng'")


def cesar_crypt(text, k, lang):
    text_crypt = ''
    if lang == 'eng':
        for i in text:
            if i in alph_en:
                text_crypt += alph_en[(alph_en.index(i) + k) % 26]
            elif i in alph_en_upper:
                text_crypt += alph_en_upper[(alph_en_upper.index(i) + k) % 26]
            else:
                text_crypt += i
    if lang == 'ru':
        for i in text:
            if i in alph_ru:
                text_crypt += alph_ru[(alph_ru.index(i) + k) % 32]
            elif i in alph_ru_upper:
                text_crypt += alph_ru_upper[(alph_ru_upper.index(i) + k) % 32]
            else:
                text_crypt += i
    print(text_crypt)


def cesar_decrypt(text, k, lang):
    text_decrypt = ''
    if lang == "eng":
        for i in text:
            if i in alph_en:
                text_decrypt += alph_en[(alph_en.index(i) - k) % 26]
            elif i in alph_en_upper:
                text_decrypt += alph_en_upper[(alph_en_upper.index(i) - k) % 26]
            else:
                text_decrypt += i
    if lang == 'ru':
        for i in text:
            if i in alph_ru:
                text_decrypt += alph_ru[(alph_ru.index(i) - k) % 32]
            elif i in alph_ru_upper:
                text_decrypt += alph_ru_upper[(alph_ru_upper.index(i) - k) % 32]
            else:
                text_decrypt += i
    print(text_decrypt)


def main():
    print('добро пожаловать в шифратор и дешифратор цезаря')
    text = input('введите текст, который хотите зашифровать или расшифровать: ')
    shift = is_valid()
    lang = check_language('введите язык алфавита ru/eng: ')
    prompt = crypt_or_decrypt('введите "crypt", если хотите зашифровать текст\n'
                              'введите "decrypt", если хотите расшифровать текст\n')
    if prompt == 'crypt':
        cesar_crypt(text, shift, lang)
    if prompt == 'decrypt':
        cesar_decrypt(text, shift, lang)


if __name__ == '__main__':
    main()
