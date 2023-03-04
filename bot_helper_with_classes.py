from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value] = record


class Record():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def add_phone(self, phone_number):
        self.phone.append(phone_number)

    def change_number(self, old_number, new_number):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
            return f'Phone number {old_number} has been changed on {new_number}'
        except:
            return f'Wrong old number {old_number}, please enter correct old number'

    def delete_phone_number(self, phone_number):
        try:
            self.phone.remove(phone_number)
            return f'{phone_number} was deleted'
        except:
            return f'Wrong phone number {phone_number}, please enter correct phone number'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone):
        self.phone = []
        self.phone.append(phone)
