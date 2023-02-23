email = input("請輸入電子郵件地址：")

domain = email.split("@")[1]

if domain == "gmail.com":
    print("這是由 Google 提供的電子郵件")
elif domain == "yahoo.com":
    print("這是由 Yahoo 提供的電子郵件")
elif domain == "hotmail.com" or domain == "outlook.com" or domain == "live.com":
    print("這是由 Microsoft 提供的電子郵件")
elif domain == "aol.com":
    print("這是由 AOL 提供的電子郵件")
else:
    print("這是自定義網域的電子郵件")