# enumerate(iterable, start=0)
person =['Sam','Veronica','Ram','smith','zhu']

# for i , person in zip(range(len(person)),person):
#     print(i,person)

#  printing separately
for i, person in enumerate(person):
    print(i,person)

# changing index and printing separately
for i, person in enumerate(person,1000):
    print(i,person)

# printing the tuples in object directly
for i in enumerate(person):
    print(i)


# changing start index to 3 from 0
person1 = "sam"
print(list(enumerate(person1,3)))


"""
Enumerate

Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

"""

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]


for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)
