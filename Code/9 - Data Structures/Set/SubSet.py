# In-built Subset function & its manual implementation.
a = {2, 3}
b = {1, 2, 3}

print(a.issubset(b))  # True
print(b.issubset(a))  # False

# Manual Implementation :

# def subSet(set_a, set_b):
#     for val in set_a:
#         if val not in set_b:
#             return False
#     return True
#
# print(subSet(a, b))  # True
# print(subSet(b, a))  # False
