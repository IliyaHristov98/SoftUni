def loading_bar(number):
    percentage = (number // 10) * 10
    list_of_percentage_signs = ((number // 10) * "%")
    list_of_dots = (10 - number // 10) * "."
    if percentage < 100:
        return f'{percentage}% [{list_of_percentage_signs + list_of_dots}]\n' \
               f'Still loading...'
    else:
        return f"100% Complete!\n" \
               f"[{list_of_percentage_signs}]"


input_number = int(input())
print(loading_bar(input_number))
