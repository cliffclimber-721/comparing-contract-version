from difflib import SequenceMatcher

firstbytecode = input("first input: ")
secondbytecode = input("second input: ")

showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()

print("first input length :", len(firstbytecode)) # 정확도를 대비해 길이 확인
print("second input length :", len(secondbytecode))

print(firstbytecode in secondbytecode)

print("show accuracy:", showRatio)