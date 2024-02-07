exam_h = int(input())
exam_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

exam_time = exam_h * 60 + exam_m
arrival_time = arrival_h * 60 + arrival_m

if arrival_time == exam_time:
    print(f"On time")
elif arrival_time < exam_time:
    difference = exam_time - arrival_time
    if difference <= 30:
        print(f"On time\n{difference} minutes before the start")
    elif 30 < difference < 60:
        print(f"Early\n{difference} minutes before the start")
    elif difference >= 60:
        hours_left = difference // 60
        minutes_left = difference % 60
        print(f"Early\n{hours_left}:{minutes_left:02d} hours before the start")
elif arrival_time > exam_time:
    difference = arrival_time - exam_time
    if difference <= 59:
        print(f"Late\n{difference} minutes after the start")
    elif difference > 59:
        hours_left = difference // 60
        minutes_left = difference % 60
        print(f"Late\n{hours_left}:{minutes_left:02d} hours after the start")