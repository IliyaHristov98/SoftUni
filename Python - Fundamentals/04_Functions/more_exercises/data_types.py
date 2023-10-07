def data_type(type_of_input, value):
    if type_of_input == "int":
        return f"{float(value) * 2:.0f}"
    elif type_of_input == "real":
        return f"{float(value) * 1.5:.2f}"
    else:
        return f"${value}$"


type_of_value = input()
input_value = input()

print(data_type(type_of_value, input_value))
