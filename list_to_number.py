str = input("数字のリストを入力してください(数字と数字の間はスペースで区切ってください):")
number = str.split()

numbers = [float(i) for i in number]

print(numbers)

total = sum(numbers)
average = total / len(numbers)

print("合計:",total)
print("平均:",average)