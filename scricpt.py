class Contact:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        # Класс Contact для создания новго контакта
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number

#Функция для  добавления нового контакта
def add_contact(contacts, last_name, first_name, middle_name, phone_number):
    contact = Contact(last_name, first_name, middle_name, phone_number)
    contacts.append(contact)
    print("Контакт успешно добавлен.")

#Функция вывода  списка контактов
def display_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact.last_name} {contact.first_name} {contact.middle_name} {contact.phone_number}")

#Функция для  сохранения контактов в файл
def save_contacts_to_file(contacts, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},{contact.phone_number}\n")
    print("Контакты успешно сохранены в файл.")


#Функция загрузки списка контактов из файла
def load_contacts_from_file(filename):
    contacts = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                contact = Contact(data[0], data[1], data[2], data[3])
                contacts.append(contact)
        print("Контакты успешно загружены из файла.")
        return contacts
    except FileNotFoundError:
        print("Файл не найден.")
        return contacts
#Функция для поиска контакта по заданному ключу (фамилии, имени, отчеству или номеру телефона)
def search_contact(contacts, key):
    results = [contact for contact in contacts if key.lower() in (contact.first_name.lower(), contact.last_name.lower(), contact.middle_name.lower(), contact.phone_number.lower())]
    if results:
        print("Найденные контакты:")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact.last_name} {contact.first_name} {contact.middle_name} {contact.phone_number}")
    else:
        print("Контакт не найден.")

#Функция для копирования контакта из одного файла в другой по номеру строки
def copy_contact_from_file(source_filename, destination_filename, line_number):
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
            if line_number <= 0 or line_number > len(lines):
                print("Некорректный номер строки.")
                return
            contact_data = lines[line_number - 1].strip().split(',')

            with open(destination_filename, 'a', encoding='utf-8') as destination_file:
                destination_file.write(','.join(contact_data) + '\n')
            print("Контакт успешно скопирован.")
    except FileNotFoundError:
        print("Файл не найден.")

def main():
    contacts = []
    filename = "phonebook.txt"

    while True:

        print("\nМеню:")
        print("1. Вывести контакты")
        print("2. Добавить контакт")
        print("3. Сохранить контакты в файл")
        print("4. Загрузить контакты из файла")
        print("5. Поиск контакта")
        print("6. Копирования")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(contacts, last_name, first_name, middle_name, phone_number)
        elif choice == "3":
            save_contacts_to_file(contacts, filename)
        elif choice == "4":
            contacts = load_contacts_from_file(filename)
        elif choice == "5":
            key = input("Ввудите фамилию, имя, отчество или номер телефона для  поиска: ")
            search_contact(contacts, key)
        elif choice == "6":
            source_file = input("Введите имя файла, откуда копировать контакт: ")
            destination_file = input("Введите имя файла, куда копировать контакт: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_contact_from_file(source_file, destination_file, line_number)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Поробуйте снова.")
if __name__ == "__main__":
    main()