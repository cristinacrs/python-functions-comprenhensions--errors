set_countries = {'col', 'mex', 'ca', 'usa', 'col'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar', 'uk'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('arg') #manda error porque no existe

#si no existe continua ejecutando
set_countries.discard('arg')
print(set_countries)

set_countries.clear()
print(set_countries)
