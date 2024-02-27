def greates_common_divisor(a, b):

    if a == b or b == 0:
        return a
    elif a > b:
        a = a - b
        return greates_common_divisor(a, b)
    else:
        b = b - a
        return greates_common_divisor(a, b)


num1 = 24
num2 = 36
gcd = greates_common_divisor(num1, num2)
print(f"Greatest common divisor for numbers: {num1} and {num2} is: {gcd}")

