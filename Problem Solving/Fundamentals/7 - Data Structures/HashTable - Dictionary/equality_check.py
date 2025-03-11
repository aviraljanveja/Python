# Check if dict1 is equal to dict2
# For two dictionaries to be considered equal:
# 1. They must have the same keys.
# 2. The values associated with those keys must also be identical.
# Even though dict1 and dict2 have the same keys, the values are different,
# so this comparison will return False.

dict1 = {1:"avi", 2:"shrey", 3:"sid"}
dict2 = {1:"sid", 2:"shrey", 3:"avi"}

print(dict1 == dict2)  # Output = False
