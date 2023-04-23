
users_dict = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        
        except IndexError:
            return "Not enough params. Try again."
        
        except KeyError:
            return 'No such user in Contacts. Use "add" command to add one.'

        except TypeError:
            return "Phone number should contain only numbers."
        
        except ValueError:
            return "Phonebook is empty."

    return inner


def hello(*args):
    return "How can I help you?"


def exit(*args):
    return "Good bye!"

@input_error
def change(*args):
    name = args[0][1]
    phone = args[0][2]

    if name not in users_dict.keys():
        raise KeyError

    users_dict[name] = phone
    return f"Phone number for user {name} is changed to {phone}."


@input_error
def phone(*args):
    name = args[0][1]

    if name not in users_dict.keys():
        raise KeyError

    phone = users_dict.get(name)

    return f"Phone number for user {name} is {phone}."

@input_error
def show_all(*args):
    if len(users_dict) == 0:
        raise ValueError
    
    all_users = ""
    for k, v in users_dict.items():
        all_users += f'{k}: {v}\n' 

    return all_users


@input_error
def add(*args):
    name = args[0][1]
    phone = args[0][2]

    if name in users_dict.keys():
        return f"User {name} is already in Contacts."

    if not phone.isdigit():
        raise ValueError

    users_dict[name] = phone
    return f"Added user {name} with phone number {phone}."


def no_command(*args):
    return "Unknown command, try again."


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'exit': exit,
    'close': exit,
    'good_bye': exit
}


def command_handler(text):
    for keyword, command in COMMANDS.items():
        if text.lower().startswith(keyword):
            #return command, text.replace(keyword, "").strip().split()
            return command, text.split(' ')
    return no_command, None


def main():
    print(hello())
    while True:
        user_input = input(">>>")
        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break


if __name__ == "__main__":
    main()
