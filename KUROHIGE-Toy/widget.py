import customtkinter as ctk
from PIL import Image
import window_state_monitor as wsm

FONT_TYPE = ('Arial', 12)

class ResetFrameWidget(ctk.CTkFrame):
    # リセットボタン等を配置
    def __init__(self, master=None, main_frame_widget=None):
        super().__init__(master)
        self.main_frame_widget = main_frame_widget
        self.window_state_monitor = None
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text='KUROHIGE Toy', font=FONT_TYPE)
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.reset_button = ctk.CTkButton(self, text='Reset', font=FONT_TYPE,
                                         command=self.reset_button_callback)
        self.reset_button.grid(row=1, column=0, padx=10, pady=10)

    def reset_button_callback(self):
        # MainFrameWidgetのbuttonsとimage_labelを取得してWindowStateMonitorに渡す
        if self.main_frame_widget:
            buttons = self.main_frame_widget.buttons
            image_label = self.main_frame_widget.image_label
            self.window_state_monitor = wsm.WindowStateMonitor(buttons, image_label)
            self.window_state_monitor.reset_triger()

class MainFrameWidget(ctk.CTkFrame):
    # メイン画面を配置
    # ここに画像やボタンを配置する
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.buttons = {}
        for i in range(3):
            if i != 1:
                for j in range(10):
                    button = ctk.CTkButton(self, text=f'Button{j} - {i}', command=lambda col=j, row=i: self.on_button_click((col, row)), font=FONT_TYPE)
                    button.grid(row=j, column=i+1, padx=20, pady=10)
                    self.buttons[(j,i)] = button

        self.image = ctk.CTkImage(light_image=Image.open(r'KUROHIGE-Toy/images/safe.png'), size=(500, 500))
        self.image_label = ctk.CTkLabel(self, image=self.image, text="")
        self.image_label.grid(row=0, column=2, padx=10, pady=10, rowspan=10)

        self.window_state_monitor = wsm.WindowStateMonitor(self.buttons, self.image_label)

    def on_button_click(self, button_id):
        self.window_state_monitor.button_state(button_id)