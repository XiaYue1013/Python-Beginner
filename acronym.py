input("輸入一段話")

a = ""

for w in str.split():
  a += w[0].upper()

print(a)