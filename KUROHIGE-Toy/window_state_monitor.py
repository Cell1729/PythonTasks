import random
from PIL import Image
import customtkinter as ctk

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
        row, col = button_id
        if self.matrix[row][col]:
            self.change_image()
        else:
            self.buttons[button_id].configure(state="disabled")

    def change_image(self):
        new_image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy/images/out.png'), size=(200, 200))
        self.image_label.configure(image=new_image)
        self.image_label.image = new_image  # 参照を保持するため

    def reset_triger(self):
        """
        buttonは座標で管理する必要がある
        暫定返り値
        button_id: int - (row,col)
        True: はずれ False: セーフ

        追加機能予定
        - 画像の変更
        - 無効かされていたボタンの有効化
        """
        # 2列10行の行列を作成
        self.matrix = [[False for _ in range(2)] for _ in range(10)]
        
        # 3つのTrueをランダムに配置
        true_positions = random.sample(range(20), 3)
        for pos in true_positions:
            row, col = divmod(pos, 2)
            self.matrix[row][col] = True
        
        # ボタンを有効化
        for button in self.buttons.values():
            button.configure(state="normal")