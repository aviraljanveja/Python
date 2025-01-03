# Slicing in Strings

# Use start:end:step to slice strings.
# start is inclusive, end is exclusive.
# step determines the direction and increment.

text = "python"

print(text[::])  # Output = python (full string, step defaults to 1)
print(text[:3])  # Output = pyt (start defaults to 0)
print(text[3:])  # Output = hon (end defaults to length)
print(text[::-1])  # Output = nohtyp (step = -1, reverses the string)
