import random

while True:
    low = 1
    high = 50
    number = random.randint(low, high)
    count = 0

    while True:
        guess = input(f"請猜一個介於{low}到{high}之間的數字：")
        if not guess.isdigit():
            print("錯誤：請輸入一個正整數。")
            continue
        guess = int(guess)
        if guess < low or guess > high:
            print(f"錯誤：請輸入介於{low}到{high}之間的數字。")
            continue
        count += 1
        if guess == number:
            print(f"恭喜！您猜對了！您總共猜了{count}次。")
            break
        elif guess < number:
            print("太小了，請再猜一次。")
        else:
            print("太大了，請再猜一次。")

    again = input("是否繼續玩？(輸入y或n)")
    if again.lower() == 'y':
        continue
    else:
        break
