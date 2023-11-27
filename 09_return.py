def find_volume(lenght=1, width=1, depth=1):
    return lenght * width * depth, width, "hi"

result = find_volume(5,3,5)
print(result)

result_2 = find_volume(width=50)
print(result_2)

print(result_2[0])

result_3, width, text = find_volume(width=60)

print(result_3)
print(width)
print(text)