from difflib import SequenceMatcher

print("================Input=================")
firstbytecode = input("first input : ")
secondbytecode = input("second input : ")
print("================Length================")
first = list(firstbytecode)
second = list(secondbytecode)

def match_binary():
    print("======================================")
    for idx1, value1 in enumerate(first):
        print("idx1", idx1, "value1", value1)
    print("======================================")
    for idx2, value2 in enumerate(second):
        print("idx2", idx2, "value2", value2)
    if value1 == value2:
        pass
    else:
        print("in first bytecode", value1)
        print("in second bytecode", value2)

print("first input length :", len(firstbytecode)) # 정확도를 대비해 길이 확인
print("second input length :", len(secondbytecode))

showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()

match_binary()
print("================Accuracy==============")
print("show accuracy:", showRatio)