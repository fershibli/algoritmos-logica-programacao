a=("a", 1)
b=("b", 2)
c=("c", 3)

print("original tuples = ", a, b, c)

abc = (a, b, c)
dictionary = dict(abc)

print("dictionary = ", dictionary)

dict_items = dictionary.items()

print("dictionary items =", end=" ")
for item in dict_items:
    print(item, end=" ")