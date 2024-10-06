def arreange(numbers):
    no_zeros = []
    zero_count = 0
    for num in numbers:
        if num != 0:
            no_zeros.append(num)

        else:
            zero_count += 1
    no_zeros.extend([0] * zero_count)
    return no_zeros

result = arreange([5, 0, 34, 9, 0, 13, 8])
print(result)

