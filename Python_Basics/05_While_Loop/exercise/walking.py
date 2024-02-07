goal = 10000
current_steps = 0
steps = input()
goal_reached = True

while current_steps < goal:
    if steps == 'Going home':
        steps = input()
        current_steps += int(steps)
        if current_steps < goal:
            goal_reached = False
        break

    current_steps += int(steps)
    if current_steps >= goal:
        break
    steps = input()

if not goal_reached:
    print(f'{goal - current_steps} more steps to reach goal.')
elif goal_reached:
    print(f'Goal reached! Good job!\n'
          f'{current_steps - goal} steps over the goal!')
