import re

n = int(input())
regex = r"\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+"

for i in range(n):
    barcode = input()
    if re.findall(regex, barcode):
        matched = re.findall(regex, barcode)
        digit_regex = r"[0-9]+"
        if re.findall(digit_regex, barcode):
            digits = re.findall(digit_regex, barcode)
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
