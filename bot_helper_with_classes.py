from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value] = record


class Record():
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone] if phone is not None else []

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
        self.value = phone


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
