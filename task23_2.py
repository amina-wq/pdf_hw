import json


country_capital_dict = {}


def add_country_and_capital(country, capital):
    country_capital_dict[country] = capital
    print(f"Данные о стране '{country}' и столице '{capital}' добавлены в словарь.")


def delete_country(country):
    if country in country_capital_dict:
        del country_capital_dict[country]
        print(f"Данные о стране '{country}' удалены из словаря.")
    else:
        print(f"Данные о стране '{country}' не найдены в словаре.")


def find_capital(country):
    if country in country_capital_dict:
        capital = country_capital_dict[country]
        print(f"Столица страны '{country}' - '{capital}'")
    else:
        print(f"Данные о стране '{country}' не найдены в словаре.")


def edit_country_and_capital(country, new_capital):
    if country in country_capital_dict:
        country_capital_dict[country] = new_capital
        print(f"Данные о стране '{country}' обновлены. Новая столица - '{new_capital}'")
    else:
        print(f"Данные о стране '{country}' не найдены в словаре.")


def save_data_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(country_capital_dict, file)
    print(f"Данные сохранены в файл '{filename}'.")


def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            country_capital_dict.update(data)
        print(f"Данные загружены из файла '{filename}'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")


if __name__ == '__main__':
    while True:
        print(
            "\nМеню:\n"
            "1. Добавить данные о стране и столице\n"
            "2. Удалить данные о стране\n"
            "3. Найти столицу страны\n"
            "4. Редактировать данные о стране и столице\n"
            "5. Сохранить данные в файл\n"
            "6. Загрузить данные из файла\n"
            "7. Выйти\n"
        )

        choice = input("Выберите действие: ")

        if choice == "1":
            country = input("Введите название страны: ")
            capital = input("Введите название столицы: ")
            add_country_and_capital(country, capital)
        elif choice == "2":
            country = input("Введите название страны, данные о которой хотите удалить: ")
            delete_country(country)
        elif choice == "3":
            country = input("Введите название страны, для которой хотите найти столицу: ")
            find_capital(country)
        elif choice == "4":
            country = input("Введите название страны, данные о которой хотите отредактировать: ")
            new_capital = input("Введите новое название столицы: ")
            edit_country_and_capital(country, new_capital)
        elif choice == "5":
            filename = input("Введите имя файла для сохранения данных: ")
            save_data_to_file(filename)
        elif choice == "6":
            filename = input("Введите имя файла для загрузки данных: ")
            load_data_from_file(filename)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
