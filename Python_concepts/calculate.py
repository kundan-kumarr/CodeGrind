"""
Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long.
 Tiles come in packages of 6.

a. How many tiles are needed?
b. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

"""
# a.

first_floor = 9*7
second_floor =5*7

total_tiles = first_floor +second_floor
print(total_tiles)

#b.

total_packages =17*6

left_tiles = total_packages-total_tiles
print(left_tiles)