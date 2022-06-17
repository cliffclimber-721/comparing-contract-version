import re
from difflib import SequenceMatcher

def lengthOfbytecode(one, two):
    one = len(one)
    two = len(two)
    print("first bytecode length:", one)
    print("second bytecode length:", two)

def accuracy():
    showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()
    print(showRatio)

def countIt(one,two):
    one = one.lower()
    two = two.lower()
    total = []
    count = 0
    for i in one:
        if i in total:
            pass
        elif re.search(i, two):
            total.append(i)
            count = count + 1
    print("matching total:", count)

firstbytecode = input("First Bytecode:")
secondbytecode = input("Second Bytecode:")

countIt(firstbytecode, secondbytecode)
accuracy()
lengthOfbytecode(firstbytecode, secondbytecode)
