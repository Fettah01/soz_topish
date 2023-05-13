import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in words or " " in words:
        word = random.choice(words)
    return word.upper()


def display(user_latters, word):
    display_latter = ""
    for latter in word:
        if latter in user_latters:
            display_latter += latter
        else:
            display_latter += "-"
    return display_latter


def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Men {len(word)} honali soz oyladim. Тopa olasizmi?")
    # print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f":Shu vaqtgacha kritilgan harflaringiz {user_letters}")

        letter = input("Harf kriting:: ").upper()
        if letter in user_letters:
            print("Bu harf avval kritilgan booshqa harf kriting.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi togri.")
        else:
            print("Bunday harf yoq.")
        user_letters += letter
    print(f"Tabriklayman! {word} sozni {len(user_letters)} ta urinishda topdingiz.")