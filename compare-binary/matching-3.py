import re
from difflib import SequenceMatcher

def bytecodeLength(one, two):
    one = len(one)
    two = len(two)
    print("first bytecode length:", one)
    print("="*40)
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

print("="*40)
countIt(firstbytecode, secondbytecode)
print("="*40)
accuracy()
print("="*40)
bytecodeLength(firstbytecode, secondbytecode)
