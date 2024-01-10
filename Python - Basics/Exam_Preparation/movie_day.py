time_for_filming = int(input())
number_of_scenes = int(input())
time_per_scene = int(input())
preparation_time = 0.15 * time_for_filming

total_time = preparation_time + (number_of_scenes * time_per_scene)
if total_time < time_for_filming:
    print(f"You managed to finish the movie on time! You have {round(time_for_filming - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(total_time - time_for_filming)} minutes.")
