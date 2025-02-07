import random
from PIL import Image
import customtkinter as ctk

OUTBUTTONS = 3

class WindowStateMonitor:
    def __init__(self, buttons, image_label):
        self.matrix = [[False for _ in range(2)] for _ in range(10)]
        self.buttons = buttons
        self.image_label = image_label

    def button_state(self, button_id):
        """
        ボタンのコールバック
        はずれボタンが押されたら画像を変える
        真偽値はreset_trigerの値
        """
        col, row = button_id
        # ここが可笑しい
        if self.matrix[col-1][row]:
            print(f"button id :{col} , {row} is danger")
            self.change_image()
        else:
            print(f"matrix[{col-1}][{row}] is {self.matrix[col-1][row]}")
            print(f"button id :{col} , {row} is safe")
            self.buttons[button_id].configure(state="disabled")

    def change_image(self):
        new_image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy/images/out.png'), size=(500, 500))
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image  # 参照を保持するため

    def reset_triger(self):
        """
        buttonは座標で管理する必要がある
        暫定返り値
        button_id: int - (col, row)
        True: はずれ False: セーフ

        追加機能予定
        - 画像の変更
        - 無効化されていたボタンの有効化
        """
        # 2行10列の行列を作成
        self.matrix = [[False for _ in range(2)] for _ in range(10)]
        # 3つのTrueをランダムに配置
        true_positions = random.sample(range(20), OUTBUTTONS)
        for pos in true_positions:
            col, row = divmod(pos, 2)
            self.matrix[col][row] = True

        print(self.matrix)
        
        # ボタンを有効化
        for button in self.buttons.values():
            button.configure(state="normal")
        
        # 画像を初期状態に戻す
        initial_image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy/images/safe.png'), size=(500, 500))
        self.image_label.configure(image=initial_image)
        self.image_label.image = initial_image
