input_list = input().split(", ")
target = input()


def search_algorithm(list_of_elements, target_element):
    variable_index = -1
    for i in list_of_elements:
        if i == target_element:
            variable_index = list_of_elements.index(i)

    return variable_index


result = search_algorithm(input_list, target)
if result != -1:
    print(f"The target element {target} is at index {result}.")
else:
    print(f"The target element {target} was not found in the list.")
