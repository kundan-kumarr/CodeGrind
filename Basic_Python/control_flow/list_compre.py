cities =["A","B","C"]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# can b reduced to 

capitalized_cities =[city.title() for city in cities]

"""
List comprehensions allow us to create a list using a for loop in one step.

You create a list comprehension with brackets [], including an expression to evaluate for each element in an iterable. 
This list comprehension above calls city.title() for each element city in cities, to create each element in the new list, capitalized_cities. 
"""

"""
Conditionals in List Comprehensions
"""
squares = [x**2 for x in range(9) if x % 2 == 0]

"""
The code above sets squares equal to the list [0, 4, 16, 36, 64], as x to the power of 2 is only evaluated if x is even. 
If you want to add an else, you will get a syntax error doing thi
"""
"""
If you would like to add else, you have to move the conditionals to the beginning of the listcomp, right after the expression, like this.   
"""
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]


"""
Extract First Names
"""

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]


first_names = [name.split()[0].lower() for name in names]
print(first_names)


"""
Filter Names by Scores

Use a list comprehension to create a list of names passed that only include those that scored at least 65.  
"""

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name,scores in scores.items() if scores>=65]
print(passed)   


"""
Multiples of Three

Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = # write your list comprehension here
print(multiples_3)

"""

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)