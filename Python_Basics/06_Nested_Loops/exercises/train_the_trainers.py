judges_count = int(input())
name = input()
total_score = 0
presentations = 0

while not name == 'Finish':
    score = 0
    presentations += 1
    average_score = 0

    for i in range(judges_count):
        judge_score = float(input())
        score += judge_score

    average_score = score / judges_count
    total_score += average_score

    print(f'{name} - {average_score:.2f}.')
    name = input()

print(f"Student's final assessment is {total_score / presentations:.2f}.")
