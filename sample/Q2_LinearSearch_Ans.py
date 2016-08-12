# coding: utf-8

li = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 38, 4, 19, 50, 48]
find_num = 38


result = 0

for x in li:
    if x == find_num:
        result = result + 1 
        break;

    result += 1


ans = 3

print(result) 

# Check The Answer
if result == ans:
    print ("Correct!")
else:
    print ("Mistake...")

