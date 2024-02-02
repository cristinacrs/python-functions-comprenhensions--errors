def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

def higher_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x)

result = higher_ord_func(2, increment)

print(result)

result_2 = high_ord_func_v2(3, increment_v2)

result_3 = high_ord_func_v2(5, lambda x : x + 1)

print(result_2)

print(result_3)