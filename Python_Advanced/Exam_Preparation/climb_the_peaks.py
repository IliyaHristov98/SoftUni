from collections import deque

portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
conquered = []

for peak, needed in peaks.items():

    while portions and stamina:
        daily = portions.pop() + stamina.popleft()

        if daily >= needed:
            conquered.append(peak)
            break

if len(conquered) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print("Conquered peaks:")
    print("\n".join(conquered))
