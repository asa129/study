import random

print("1 から 100 までの数字を当ててください。")

answer = random.randint(1, 100)

count = 0
while True:
    count += 1
    num = int(input("入力してください:　"))
    if num > answer:
        print("もっと小さい数字です")
    elif num < answer:
        print("もっと大きい数字です")
    else:
        print(f"正解！ {count} 回で当てました")
        break
