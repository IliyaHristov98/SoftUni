from pyfiglet import figlet_format


def print_message():
    message = input()
    print(figlet_format(message))


print_message()
