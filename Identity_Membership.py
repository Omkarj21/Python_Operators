# Identity operators : Two variables that are equal does not imply that they are identical... This Refers to Address of Object.
x1 = 5 # Single objects
y1 = 5 # Single objects
x2 = 'Hello' # Single objects
y2 = 'Hello' # Single objects
x3 = [1,2,3] # Multiple objects
y3 = [1,2,3] # Multiple objects

# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)
# ---------------------------------------
# Membership operators : This Refers to Contents of Object.
x = 'Hello world' # Single objects
y = {1:'a',2:'b'} # Multiple objects
# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)
# ---------------------------------------