from math import floor
name = input()
seasons = int(input())
episodes = int(input())
time_per_episode = float(input())

ads = time_per_episode * 0.2
last_episode_time = time_per_episode + 10

total_time_episodes = (seasons * (episodes - 1)) * (time_per_episode + ads)
total_time_last_episodes = seasons * (last_episode_time + ads)
total_time = total_time_episodes + total_time_last_episodes
print(f'Total time needed to watch the {name} series is {floor(total_time)} minutes.')
