gift_plans = input().split()
command = input().split()

while command != ["No", "Money"]:
    if "OutOfStock" in command:
        for i in range(len(gift_plans)):
            if gift_plans[i] == command[1]:
                gift_plans[i] = "None"
    elif "Required" in command:
        index = int(command[2])
        if 0 <= index < len(gift_plans):
            gift_plans[index] = command[1]
    elif "JustInCase" in command:
        gift_plans[-1] = command[1]
    command = input().split()

while "None" in gift_plans:
    gift_plans.remove("None")

for gifts in gift_plans:
    print(gifts, end=' ')
