ListA = [0, 1, 2, 3]
ListB = [4, 5, 6, 7]
ListA.extend(ListB)
print(ListA)
ListA.append(-5)
print(ListA)
ListA.remove(-5)
print(ListA)
ListX = ListA + ListB
print(ListX)
