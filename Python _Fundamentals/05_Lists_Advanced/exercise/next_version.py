def following_version(version):
    if version[2] == 9:
        version[1] += 1
        version[2] = 0
        if version[1] > 9:
            version[1] = 0
            version[0] += 1
    else:
        version[2] += 1

    return version


current_version = [int(i) for i in input().split(".")]
next_version = following_version(current_version)
print(".".join(map(str, next_version)))
