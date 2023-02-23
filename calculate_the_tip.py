bill = float(input("今日帳單多少？"))
tip_rate = 0.1
tip = bill * tip_rate
total = bill + tip

print(f"在費率 {tip_rate*100}% 的狀況下，小費為 {tip:.2f}，總金額 {total:.2f}。")
