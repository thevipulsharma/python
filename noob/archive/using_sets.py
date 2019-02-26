SetA = set()
SetA.update(['Red'], ['Blue'], ['Green'], ['Orange'])
SetB = set()
SetB.update(['Black'], ['Green'], ['Yellow'], ['Orange'])

SetX = SetA.union(SetB)
SetY = SetA.intersection(SetB)
SetZ = SetA.difference(SetB)

print('{0}\n{1}\n{2}'.format(SetX, SetY, SetZ))
