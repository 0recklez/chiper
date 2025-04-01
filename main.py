ALPH_EN = 'abcdefghijklmnopqrstuvwxyz'
ALPH_EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPH_RU = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ALPH_RU_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_valid_shift():
    while True:
        shift = input('введите сдвиг: ')
        if shift.isdigit() and int(shift) > 0:
            return int(shift)
        print('ошибка: введите целое положительное число')


def get_crypt_mode():
    while True:
        mode = input('введите "crypt" для шифрования или "decrypt" для дешифрования: ').lower()
        if mode in ('crypt', 'decrypt'):
            return mode
        print('ошибка: команда не распознана')


def get_language():
    while True:
        lang = input('выберите язык (ru/eng): ').lower()
        if lang in ("ru", "eng"):
            return lang
        print("ошибка: введите 'ru' или 'eng'")


def process_text(text, shift, lang, mode):
    shift = shift if mode == 'crypt' else -shift
    new_char = ''
    if lang == 'eng':
        alph, alph_upper = ALPH_EN, ALPH_EN_UPPER
    else:
        alph, alph_upper = ALPH_RU, ALPH_RU_UPPER
    for char in text:
        if char in alph:
            new_char += alph[(alph.index(char) + shift) % len(alph)]
        elif char in alph_upper:
            new_char += alph_upper[(alph_upper.index(char) + shift) % len(alph_upper)]
        else:
            new_char += char
    return new_char


def main():
    print('добро пожаловать в шифратор/дешифратор цезаря')
    text = input('введите текст для обработки: ')
    shift = get_valid_shift()
    lang = get_language()
    mode = get_crypt_mode()

    result = process_text(text, shift, lang, mode)
    print(f'результат: {result}')


if __name__ == '__main__':
    main()
