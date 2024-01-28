def concatenate(*strings, **substitutions):
    final_string = "".join(strings)

    for word, sub in substitutions.items():
        final_string = final_string.replace(word, sub)

    return final_string
