#素数判定プログラム

try:
    input_number = int(input("素数判定したい数値を入力してください:"))
except ValueError:
    print("整数を入力してください")
    exit()

if input_number == 1:
    print("素数ではありません")
elif input_number <= 0:
    print("正の整数を入力してください")
else:
    flag = None

    for i in range(2, input_number):
        if input_number % i == 0:
            flag = True
            break

    if flag:
        print("素数ではありません")
    else:
        print("素数です")