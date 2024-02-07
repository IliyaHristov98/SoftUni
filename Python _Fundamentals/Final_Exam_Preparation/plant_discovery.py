rarity = {}
ratings = {}

n = int(input())
for _ in range(n):
    plant, rare = input().split("<->")
    rarity[plant] = int(rare)

while True:
    given_input = input()
    if given_input == "Exhibition":
        break
    command, rates = given_input.split(": ")

    if rates[0] not in rarity:
        print("error")
        continue

    if command == "Rate":
        plant, rating = rates.split(" - ")
        if plant not in ratings:
            ratings[plant] = [int(rating)]
        else:
            ratings[plant] += [int(rating)]

    elif command == "Update":
        plant, new_rarity = rates.split(" - ")
        rarity[plant] = int(new_rarity)

    elif command == "Reset":
        plant = rates
        ratings[plant] = []

print("Plants for the exhibition:")
for key, value in rarity.items():
    average_rating = 0
    if key in ratings and len(ratings[key]) > 0:
        average_rating = sum(ratings[key]) / len(ratings[key])
    print(f"- {key}; Rarity: {value}; Rating: {average_rating:.2f}")
