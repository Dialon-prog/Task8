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
        