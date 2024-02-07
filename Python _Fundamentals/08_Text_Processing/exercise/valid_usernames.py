usernames = input().split(", ")
valid_usernames = []
allowed = ["-", "_"]
for username in usernames:
    is_valid = True
    if 3 <= len(username) <= 16:
        for char in username:
            if char in allowed or char.isalpha() or char.isdigit():
                continue
            else:
                is_valid = False
                break
        if is_valid:
            valid_usernames.append(username)

for valid in valid_usernames:
    if valid is not None:
        print(valid)
