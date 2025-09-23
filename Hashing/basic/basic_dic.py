name = {'k': 1, 'u': 2, 'm': 3}
name['a'] = 4
name['r'] = 5
print(name)
# Accessing a value using key
print(name['k'])

# using the method get() Method - returns None if the key is not found - 
# d.get(key, default_val) Returns the value of the item in the dictionary d with the specified key.
#
print(name.get('u'))
# Deleting a key-value pair using del keyword
del name['m']
# Deleting a key-value pair using pop() method
name.pop('a')
# Deleting the last inserted key-value pair using popitem() method
name.popitem()
# Updating a value using key
name['k'] = 10
print(name)
# Iterating through a dictionary
for key in name:
    print(key, name[key])
# Sorting a dictionary by keys
d = dict(sorted(name.items()))
print(d)

def intersect(nums1, nums2):
    freq = {}
    result = []
    
    # Count frequency of nums1 elements
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in nums2:
        if num in freq and freq[num] > 0:
            result.append(num)
            freq[num] -= 1   # decrease count so we don’t overuse

    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))