from math import ceil

movie_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = (1 / 8) * break_duration
time_for_rest = (1 / 4) * break_duration

time_left = break_duration - time_for_lunch - time_for_rest

if time_left >= episode_duration:
    print(f"You have enough time to watch {movie_name} and left with {ceil(time_left - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(episode_duration - time_left)} more minutes.")

