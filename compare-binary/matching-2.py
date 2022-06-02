from difflib import SequenceMatcher

print("=============== Input ================")
firstbytecode = input("first input : ")
secondbytecode = input("second input : ")
print("=============== Length ===============")
first = list(firstbytecode)
second = list(secondbytecode)

def match_binary():
    print("======================================")
    for i in range(len(first)):
        print("i:", first[i])
    print("======================================")
    for j in range(len(second)):
        print("j:", second[j])
    if first[i] == second[j]:
        pass
    elif first[i] != second[j]:
        print("in first bytecode", first[i])
        print("in second bytecode", second[j])

print("first input length :", len(firstbytecode)) # 정확도를 대비해 길이 확인
print("second input length :", len(secondbytecode))

showRatio = SequenceMatcher(None, firstbytecode, secondbytecode).ratio()

match_binary()
print("=============== Accuracy =============")
print("show accuracy:", showRatio)