ListA = ['Orange', 'Yellow', 'Green', 'Brown']
ListB = [1, 2, 3, 4]

for Value in ListB[1:3]:
    print(Value)

for Value1, Value2 in zip(ListA, ListB):
    print(Value1, '\t', Value2)
