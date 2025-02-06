import customtkinter as ctk
from PIL import Image

FONT_TYPE = ('Arial', 12)

class ResetFrameWidget(ctk.CTkFrame):
    # リセットボタン等を配置
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text='KUROHIGE Toy', font=FONT_TYPE)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.rest_button = ctk.CTkButton(self, text='Reset', font=FONT_TYPE)
        self.rest_button.grid(row=1, column=0, padx=10, pady=10)

class MainFrameWidget(ctk.CTkFrame):
    # メイン画面を配置
    # ここに画像やボタンを配置する
    def __init__(self, master=None):
        super().__init__(master)
        self.create_button()

    def create_button(self):        
        self.buttons = {}
        # 左右に縦に10個ボタンを配置
        for i in range(3):
            if i != 1:
                # i は調節が必要
                for j in range(10):
                    button = ctk.CTkButton(self, text=f'Button {j}', command=lambda row=i, col=j: self.on_button_click(f"{row}-{col}"), font=FONT_TYPE)
                    button.grid(row=j, column=i, padx=20, pady=5)
                    self.buttons[j] = button

        # configureで更新
        self.image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy\images\safe.png'), size=(500, 500))
        self.image_label = ctk.CTkLabel(self, image=self.image, text="")
        self.image_label.grid(row=0, column=1, padx=20, pady=20, rowspan=10)

    def on_button_click(self, button_id):
        print(f'Button {button_id} clicked')