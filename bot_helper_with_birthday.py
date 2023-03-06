from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, max_count):
        count = 0
        for item in self.data:
            if count < max_count:
                count += 1
                yield self.data[item]
        else:
            raise StopIteration


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):

    @Field.value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError('Incorrect name. Name must be string')


class Phone(Field):

    @Field.value.setter
    def value(self, value):
        if not value.isnumeric():
            raise ValueError('Phone number must be digits.')
        elif len(value) > 12:
            raise ValueError('Phone number is too long')
        elif len(value) < 10:
            raise ValueError('Phone number is too short')
        else:
            self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        birthday = datetime.strptime(value, '%Y-%m-%d').date()
        if birthday > today:
            raise ValueError('Incorrect date')


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = [phone] if phone is not None else []
        self.birthday = birthday

    def add_phone(self, phone_number):
        self.phone.append(phone_number)

    def change_number(self, old_number, new_number):
        self.phone.remove(old_number)
        self.phone.append(new_number)

    def delete_phone_number(self, phone_number):
        self.phone.remove(phone_number)

    def days_for_birthday(self):
        today = datetime.now().date()
        birthday_this_year = datetime(
            today.year, self.birthday.value.month, self.birthday.value.day).date()
        if birthday_this_year > today:
            return f"{(birthday_this_year - today).days} days to birthday"
        elif birthday_this_year < today:
            return f"{((birthday_this_year.replace(year=today.year + 1)) - today).days} days to birthday"
        else:
            return f"The birthday is today"


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
    print(name.value)
    name.value = "Jion"
    print(name.value)

    print('All Ok)')

    ab = AddressBook()
    n1 = Name('Billl')
    b1 = Birthday('2021-08-30')
    ph1 = Phone('1234567890')
    rec1 = Record(n1, ph1)
    ab.add_record(rec1)
    n2 = Name('Racs')
    ph2 = Phone('12345678901')
    rec2 = Record(n2, ph2)
    ab.add_record(rec2)
    n3 = Name('Back')
    ph3 = Phone('12345678901')
    rec3 = Record(n3, ph3)
    ab.add_record(rec3)
    n4 = Name('Jan')
    ph4 = Phone('12345678901')
    rec4 = Record(n4, ph4)
    ab.add_record(rec4)
    n5 = Name('Jon')
    ph5 = Phone('12345678901')
    rec5 = Record(n5, ph5)
    ab.add_record(rec5)

    ab.iterator(6)
    ab.iterator(3)

    print('all_ok!!!')
