word = input("請輸入單字：")

if word == word[::-1]:
    print(word, "是回文")
else:
    print(word, "不是回文")