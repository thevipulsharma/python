MyTuple = (1, 2, 3, (4, 5, 6, (7, 8, 9)))
MyTuple = MyTuple.__add__((10, 11, 12, (13, 14, 15)))
for Value1 in MyTuple:
    if type(Value1) == int:
        print(Value1)
    else:
        for Value2 in Value1:
            if(type(Value2) == int):
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)
