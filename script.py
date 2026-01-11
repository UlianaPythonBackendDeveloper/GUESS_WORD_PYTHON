import random

word_dict = [
    "кот", "дом", "лес", "сон", "чай", "нос", "рот", "год", "день",
    "стол", "стул", "книга", "рука", "нога", "снег", "окно", "дверь", "мечта",
    "солнце", "цветок", "машина", "город", "улица", "школа", "работа", "семья",
    "программа", "компьютер", "библиотека", "праздник", "учитель"
]

def guess_word_game():
    print("="*50)
    print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ УГАДАЙ СЛОВО!")
    print("="*50)
    
    secret_word = random.choice(word_dict).lower()
    print(f"Я загадал слово из {len(secret_word)} букв")
    print(f"У вас будет 5 попыток чтобы отгадать его")
    print('-'*50)
    
    for attempts in range(1,6):
        print(f"\nПопытка {attempts} из 5")
        user_guess = input("Введите слово: ").strip().lower()
        
        if user_guess not in [w.lower() for w in word_dict]:
            print("Этого слова нет в моем словаре. Попробуйте другое")
            continue
        if user_guess == secret_word:
            print("="*50)
            print(f"Поздравляю вы угадали слово!")
            print(f"Загаданное слово: '{secret_word}'")
            print(f"Вам потребовалось {attempts} попыток")
            print("="*50)
            return
        if user_guess < secret_word:
            print(f"Загаданное слово идет ПОСЛЕ '{user_guess}' в алфавитном порядке")
        else:
            print(f"Загаданное слово идет ДО '{user_guess}'в алфавитном порядке")
            
            if user_guess[0] != secret_word[0]:
                print(f"Подсказка: Загаданное слово начинается на '{secret_word[0]}'")
                
            if len(user_guess) != len(secret_word):
                print(f"Ваше слово имеет {len(user_guess)} букв, а загаданное {len(secret_word)}")
                
            if attempts == 4:
                print("Осталась одна попытка!")
        print("\n" + "=" *50)
        print("Попытки закончились")
        print(f"Загаданное число было: '{secret_word}'")
        
        print("Ближайшие слова в алфавитном порядке: ")
        sorted_word = sorted(word_dict, key=str.lower)
        word_index = -1
        for i, word in enumerate(sorted_word):
             if word.lower() == secret_word:
                 word_index = i
                 break
            
        if word_index >= 0:
            if word_index > 0:
                print(f"Слово до загаданного: '{sorted_word[word_index - 1]}'")
                
        print(f"Загаданное слово: '{secret_word}'")
        
        if word_index < len(sorted_word) - 1:
            print(f"Слово после загаданного: '{sorted_word[word_index + 1]}'")

    print("="*50)

print("\n Начинаем игру!")
print("Я загадал слово из словаря. Попробуйте отгадать его!")
print("Я буду говорить, идет ли мое слово ДО или ПОСЛЕ вашего по алфавиту.")
print()

guess_word_game()

print("Спасибо за игру! Всего хорошего!")