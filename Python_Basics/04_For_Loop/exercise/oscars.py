actor_name = input()
starting_points = float(input())
judges_count = int(input())

total_points = starting_points

for judges_points in range(judges_count):
    judge_name = input()
    points_given = float(input())
    total_points += len(judge_name) * points_given / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
if total_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!')
