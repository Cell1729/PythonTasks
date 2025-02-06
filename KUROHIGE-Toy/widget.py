import customtkinter as ctk
from PIL import Image
import window_state_monitor as wsm

FONT_TYPE = ('Arial', 12)

class ResetFrameWidget(ctk.CTkFrame):
    # リセットボタン等を配置
    def __init__(self, master=None):
        super().__init__(master)
        self.window_state_monitor = wsm.WindowStateMonitor()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text='KUROHIGE Toy', font=FONT_TYPE)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.rest_button = ctk.CTkButton(self, text='Reset', font=FONT_TYPE,
                                         command=self.window_state_monitor.reset_triger())
        self.rest_button.grid(row=1, column=0, padx=10, pady=10)

class MainFrameWidget(ctk.CTkFrame):
    # メイン画面を配置
    # ここに画像やボタンを配置する
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.main_label = ctk.CTkLabel(self, text='Main Frame', font=FONT_TYPE)
        self.main_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.buttons = {}
        for i in range(2):
            for j in range(10):
                button = ctk.CTkButton(self, text=f'Button {j}', command=lambda row=i, col=j: self.on_button_click((row, col)), font=FONT_TYPE)
                button.grid(row=j+1, column=i, padx=5, pady=5)
                self.buttons[(i, j)] = button

        self.image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy\images\safe.png'))
        self.image_label = ctk.CTkLabel(self, image=self.image, text="")
        self.image_label.grid(row=1, column=0, padx=10, pady=10)

        self.window_state_monitor = wsm.WindowStateMonitor(self.buttons, self.image_label)
        self.window_state_monitor.reset_triger()

    def on_button_click(self, button_id):
        self.window_state_monitor.button_state(button_id)

    