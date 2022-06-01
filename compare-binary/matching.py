from difflib import SequenceMatcher

firstbytecode = input("first input : ")
secondbytecode = input("second input : ")
first = list(firstbytecode)
second = list(secondbytecode)

def match_binary():
    for i in first:
        print("i:", i)
    for j in second:
        print("j:", j)
    if i == j:
        pass
    else:
        print(i, j)

print("first input length :", len(firstbytecode)) # 정확도를 대비해 길이 확인
print("second input length :", len(secondbytecode))

showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()

match_binary()
print("show accuracy:", showRatio)