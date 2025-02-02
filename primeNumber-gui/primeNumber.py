# primeNumber.py
# 素数判定を行うためのclassを作成
# 練習としてカプセル化を意識して作成

class PrimeNumber:
    """
    素数の判定を行う

    Attributes
    ----------
    number : int
        素数判定を行う数
    """
    def __init__(self, number):
        # カプセル化する
        self.__number = number
        self.__prime_flag = True

    def is_prime(self):
        """
        素数判定を行うメソッド

        Returns
        -------
        素数です : str
            素数の場合
        素数ではありません : str
            素数でない場合
        """
        if self.__number < 2:
            return "素数ではありません"
        for i in range(2, self.__number):
            if self.__number % i == 0:
                self.__prime_flag = False
                break

        if self.__prime_flag:
            return "素数です"
        else:
            return "素数ではありません"