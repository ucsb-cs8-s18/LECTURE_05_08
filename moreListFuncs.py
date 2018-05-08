# moreListFuncs.py

def lastEvenInt(someList):
    """ return the last even integer in the list """

    evenNumbers = []
    for x in someList:
        if x%2 == 0:
            evenNumbers.append(x) # OR newList = newList + [x]
    
    if evenNumbers != []:   # OR   if len(evenNumbers)>0
       return evenNumbers[-1]
    else:
        return None

def test_lastEvenInt_1():
    assert lastEvenInt([3, 5, 6, 2])==2

def test_lastEvenInt_2():
    assert lastEvenInt([3, 5, 7])==None

def test_lastEvenInt_3():
    assert lastEvenInt([3, 5, 4, 7, 8])==8
