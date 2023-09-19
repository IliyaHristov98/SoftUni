needed_book = input()
count = 0
current_book = input()

while current_book != needed_book:

    if current_book == "No More Books":
        print(f'The book you search is not here!\n'
              f'You checked {count} books.')
        break
    count += 1
    current_book = input()
if current_book == needed_book:
    print(f'You checked {count} books and found it.')
