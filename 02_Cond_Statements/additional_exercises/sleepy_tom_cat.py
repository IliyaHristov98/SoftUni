DAYS_IN_THE_YEAR = 365
PLAY_TIME_NORM_PER_YEAR = 30000
REST_DAY_PLAY_TIME = 127
WORK_DAY_PLAY_TIME = 63

rest_days_per_year = int(input())
work_days_per_year = DAYS_IN_THE_YEAR - rest_days_per_year

total_play_on_rest_days = rest_days_per_year * REST_DAY_PLAY_TIME
total_play_on_work_days = work_days_per_year * WORK_DAY_PLAY_TIME
total_play_time_per_year = total_play_on_work_days + total_play_on_rest_days

play_difference_in_hours_less = (PLAY_TIME_NORM_PER_YEAR - total_play_time_per_year) // 60
play_difference_in_minutes_less = (PLAY_TIME_NORM_PER_YEAR - total_play_time_per_year) % 60
play_difference_in_hours_more = (total_play_time_per_year - PLAY_TIME_NORM_PER_YEAR) // 60
play_difference_in_minutes_more = (total_play_time_per_year - PLAY_TIME_NORM_PER_YEAR) % 60

if total_play_time_per_year >= PLAY_TIME_NORM_PER_YEAR:
    print(f'Tom will run away\n'
          f'{play_difference_in_hours_more} hours and {play_difference_in_minutes_more} minutes more for play')
else:
    print(f'Tom sleeps well\n'
          f'{play_difference_in_hours_less} hours and {play_difference_in_minutes_less} minutes less for play')