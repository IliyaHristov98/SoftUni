def fill_the_box(height, length, width, *args):
    volume = height * length * width
    left = 0
    for cube in args:
        if cube == "Finish":
            break

        if volume > 0:
            volume -= cube
        else:
            left += cube

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        left += abs(volume)
        return f"No more free space! You have {left} more cubes."
