dictionary = {}


def add_word(english_word, french_translation):
    dictionary[english_word] = french_translation
    print(f"Слово '{english_word}' и его перевод '{french_translation}' добавлены в словарь.")


def delete_word(english_word):
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово '{english_word}' удалено из словаря.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


def find_translation(english_word):
    if english_word in dictionary:
        translation = dictionary[english_word]
        print(f"Перевод слова '{english_word}' на французский: '{translation}'")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


def replace_translation(english_word, new_french_translation):
    if english_word in dictionary:
        dictionary[english_word] = new_french_translation
        print(f"Перевод слова '{english_word}' обновлен на '{new_french_translation}'.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")


if __name__ == '__main__':
    while True:
        print(
            "\nМеню:\n"
            "1. Добавить слово и перевод\n"
            "2. Удалить слово\n"
            "3. Найти перевод слова\n"
            "4. Заменить перевод слова\n"
            "5. Выйти\n"
        )

        choice = input("Выберите действие: ")

        if choice == "1":
            english_word = input("Введите английское слово: ")
            french_translation = input("Введите перевод на французский: ")
            add_word(english_word, french_translation)
        elif choice == "2":
            english_word = input("Введите английское слово, которое хотите удалить: ")
            delete_word(english_word)
        elif choice == "3":
            english_word = input("Введите английское слово для поиска перевода: ")
            find_translation(english_word)
        elif choice == "4":
            english_word = input("Введите английское слово, перевод которого хотите изменить: ")
            new_french_translation = input("Введите новый перевод на французский: ")
            replace_translation(english_word, new_french_translation)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
