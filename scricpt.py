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
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},{contact.phone_number}\n")
    print("Контакты успешно сохранены в файл.")


#Функция загрузки списка контактов из файла
def load_contacts_from_file(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contact = Contact(data[0], data[1], data[2], data[3])
                contacts.append(contact)
        print("Контакты успешно загружены из файла.")
        return contacts
    except FileNotFoundError:
        print("Файл не найден.")
        return contacts
    
