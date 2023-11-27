def sum_with_range(min,max):
    sum = 0

    for x in range(min,max):
        sum += x
    return sum

result = sum_with_range(1,10)
print(result, result + 10)

