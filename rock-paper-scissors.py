from random import randint

s = input("來玩剪刀石頭布吧\n你要出?")

a = ["剪刀","石頭","布"]

c = a[randint(0, 2)]

print("你出了：", s)
print("電腦出了：", c)

if s == "剪刀":
    if c == "剪刀":
        print("平手")
    elif c == "石頭":
        print("你輸了")
    else:
        print("你贏了")
elif s == "石頭":
    if c == "剪刀":
        print("你贏了")
    elif c == "石頭":
        print("平手")
    else:
        print("你輸了")
else:
    if c == "剪刀":
        print("你輸了")
    elif c == "石頭":
        print("你贏了")
    else:
        print("平手")
