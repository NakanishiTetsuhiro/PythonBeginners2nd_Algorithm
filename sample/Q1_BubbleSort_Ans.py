# coding: utf-8

result = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

# range(): resultの大きさ(15)から1を引いた値(14)から0までマイナス１ずつ減らしていく
# range()はPython2.7でrange()のメモリ効率をよくした版（あんまりわかってないので詳しくは調べてください）3.5ではrange()がrange()のように実装されてrange()は廃止されている
for index in range(len(result)-1, 0, -1):
    for low in range(index):

        if result[low] > result[low+1]:
            # 隣り合った数字をSwap
            tmp           = result[low+1]
            result[low+1] = result[low]
            result[low]   = tmp



ans = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

print(result) 

# Check The Answer
if result == ans:
    print ("Correct!")
else:
    print ("Mistake...")

