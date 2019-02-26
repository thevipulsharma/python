def DisplayMulti(ArgCount = 0, *VarArgs):
    print('You passed '+str(ArgCount)+' arguments. ', VarArgs)

DisplayMulti(2, 'Hello', 'World!')
