def electron_shells(electrons):
    shells = [0]
    n = 1
    while electrons > 0:
        max_electrons_in_shell = 2 * n ** 2
        electrons_in_shell = min(max_electrons_in_shell, electrons)
        shells.append(electrons_in_shell)
        electrons -= electrons_in_shell
        n += 1
    return shells[1:]


number_of_electrons = int(input())
print(electron_shells(number_of_electrons))
