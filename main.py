def cesar(text, k):
    alph_en = 'abcdefghijklmnopqrstuvwxyz'
    alph_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    text_crypt = ''
    for i in text:
        text_crypt += alph_en[(alph_en.index(i) + k) % 26]
    print(text_crypt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cesar('a', 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
