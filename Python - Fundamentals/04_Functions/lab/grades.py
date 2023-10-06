def grade_in_words(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    else:
        return "Excellent"


grade_in_number = float(input())
print(grade_in_words(grade_in_number))
