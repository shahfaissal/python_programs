#import : this syntax will create an empty dict not an empty set
a = {}
print(type(a))

#  an empty set can be created using the below syntax :
b = set()
print(type(b))
b.add(4)
b.add(5)
print(b)