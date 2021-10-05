import random

def check_yours(S):
    # 檢查輸入 1.長度位數 2. 是否重複
    if len(S) != 4:
        return False
    l = [i for i in S]
    if len(l) == len(set(l)):
        return True
    return False
def give_ans():
    # 生成答案
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(num)
    ans = ''.join(num[0:4])
    return ans
def compare(a, y):
    # 生成幾A幾B
    A = 0; B = 0
    for i in range(len(y)):
        if y[i] == a[i]:
            A += 1
        elif y[i] in a:
            B += 1
    if A == len(a):
        return True
    return f'{A}A{B}B，加油！'

# 生成答案
A = give_ans()

# 輸入你的答案
yours = str(input('請輸入四位數字：'))

while True:
    if check_yours(yours):
        if compare(A, yours) == True:
            print('答對了，恭喜你！')
            break
        else:
            print(compare(A, yours))
            yours = str(input('再接再厲：'))
    else:
        yours = str(input('好好給，謝謝：'))
