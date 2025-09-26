"""
Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro?
 Print True if it is and False if not.

"""
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

is_density = san_francisco_pop_density > rio_de_janeiro_pop_density
print(is_density)

"""
or

"""
if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)