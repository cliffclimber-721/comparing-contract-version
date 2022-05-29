from difflib import SequenceMatcher

firstbytecode = input("first input: ")
secondbytecode = input("second input: ")
first = list(firstbytecode)
second = list(secondbytecode)

print("first input length :", len(firstbytecode)) # 정확도를 대비해 길이 확인
print("second input length :", len(secondbytecode))

showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()

for first in second:
    for i in range(0, first):
        if first == second[i]:
            print(first)
            i+=1
            print(i)


print("show accuracy:", showRatio)