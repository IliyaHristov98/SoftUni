# fails = int(input())
# fails_count = 0
# total_grade = 0
# count = 0
# last_problem = ''
# has_failed = False
#
# while fails_count < fails:
#     name = input()
#     if name == 'Enough':
#         print(f'Average score: {total_grade / count:.2f}\n'
#               f'Number of problems: {count}\n'
#               f'Last problem: {last_problem}')
#         break
#     grade = int(input())
#     total_grade += grade
#     if grade <= 4:
#         fails_count += 1
#     count += 1
#     last_problem = name
#     if fails_count == fails:
#         has_failed = True
# if has_failed:
#     print(f'You need a break, {fails_count} poor grades.')

fails = int(input())
fails_count = 0
total_grade = 0
count = 0
last_problem = ''
has_failed = True

while fails_count < fails:
    name = input()
    if name == 'Enough':
        has_failed = False
        break
    grade = int(input())

    if grade <= 4:
        fails_count += 1

    total_grade += grade
    count += 1
    last_problem = name

if has_failed:
    print(f'You need a break, {fails_count} poor grades.')
else:
    print(f'Average score: {total_grade / count:.2f}\n'
          f'Number of problems: {count}\n'
          f'Last problem: {last_problem}')
