# For two dictionaries to be considered equal:
# 1. They must have the same keys.
# 2. The values associated with those keys must also be identical.
# 3. The order doesn't matter.

dict1 = {1:"avi", 2:"shreyas", 3:"sid"}
dict2 = {3:"sid", 1:"avi", 2:"shreyas"}

print(dict1 == dict2)  # Output = True
