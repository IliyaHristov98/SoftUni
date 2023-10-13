def wealthiest(people, minimum):
    for person in people:
        richest_index = people.index(max(people))
        person_index = people.index(person)
        if person < minimum:
            people[richest_index] -= minimum - person
            people[person_index] += minimum - person

    for x in people:
        if x < minimum:
            return "No equal distribution possible"
    else:
        return people


population = [int(i) for i in input().split(", ")]
minimum_wealth = int(input())
print(wealthiest(population, minimum_wealth))
