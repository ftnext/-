digits = input()
if digits.endswith("00"):
    print(digits[:-2])
else:
    print(int(digits) // 100 + 1)
