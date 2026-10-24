def missingPositiveNumber(numbers):
    numbers = set(numbers)
    i = 1
    while True:
        if i not in numbers:
            return i
        i += 1
    return i
