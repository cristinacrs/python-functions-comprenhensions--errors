set_countries = {'col', 'mex', 'ca', 'usa', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 3, 66, 8, 9, 1}
print(set_numbers)

set_types = {'Lana', 1, False, 1, 'Freya', 'Keisi'}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuple = set((1, 5, 67, 89))
print(set_from_tuple)

list_1 = [1, 'a', 3, 'b', 'c', 4, 5, 5]
set_from_list = set(list_1)
print(set_from_list)

unique_list = list(set_from_list)
print(unique_list)