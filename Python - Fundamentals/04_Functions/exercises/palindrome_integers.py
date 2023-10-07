def palindrome_integer(number):
    return number == number[::-1]


list_of_integers = input().split(", ")

for i in list_of_integers:
    print(palindrome_integer(i))
    