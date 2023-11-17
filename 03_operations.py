set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#interseccion
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#difference
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#symetric_difference
#union sin los elementos en comun
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
