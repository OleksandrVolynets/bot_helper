def input_error(func):
    def inner(*args):
        if len(*
               args) < 1:
            try:
                func(*args)
            except:
                print(
                    f"You didn't enter anything. Please enmter the command or enter command HELP")
        else:
            try:
                func(*args)
            except KeyError:
                print(f"Enter the correct command")
            except IndexError:
                print(f"Enter the user name and the phone number")
            except ValueError:
                print(f"Please enter the correct data")
    return inner


COMMANDS = {'help': 'list of all commands with comments',
            'hello': 'greating with you)',
            'add': 'add new contact and phone number.syntax(add name number)',
            'change': 'changes the number of an existing contact. syntax(change name number)',
            'phone': 'output number of an existing contact. syntax(phone name)',
            'show_all': 'output all contacts and numbers',
            'close or exit or good bye': 'finished the programm'}

CONTACTS = {'s': 93745632975693, 'r': 566566777}


def helps(s=None):
    return COMMANDS


def hello(s=None):
    return f'Hello, how can I hep you?\nTo see all posible commands enter Help'


def add(s):
    split_s = s.split()
    CONTACTS[split_s[1]] = split_s[2]
    return f"Added contact {split_s[1]} with phone number {split_s[2]}"


def change(s):
    split_s = s.split()
    CONTACTS[split_s[1]] = split_s[2]
    return f"Contact {split_s[1]} now has a phone number {split_s[2]}"


def phone(s):
    name = s.split()[1]
    return f"{name}'s phone number is {CONTACTS.get(name)}"


def show_all(s=None):
    return CONTACTS


def quit(s=None):
    return f"Good bye!"


ALL_COMMANDS = {'hello': hello, 'help': helps, 'add': add, 'change': change, 'phone': phone,
                'show_all': show_all, 'close': quit, 'exit': quit, 'good bye': quit}


@input_error
def main(user_input):
    command = user_input.lower().split()[0]
    print(ALL_COMMANDS[command](user_input))


if __name__ == '__main__':
    print(hello())
    while True:
        user_input = input(
            'Enter the command: ')
        main(user_input)

        if user_input.lower() in ('close', 'exit', 'good bye'):
            break
