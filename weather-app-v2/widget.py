import customtkinter as ctk
import json

FONT_TYPE = ('Meiryo', 12)
FONT_TYPE_TITLE = ('Meiryo', 18)
FONT_TYPE_LABEL = ('Meiryo', 14)

JSON_FILE = r"weather-app-v2\area.json"

class WidgetFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.load_areas()
        self.contents()
        
    def load_areas(self):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.areas = {area['region']: {sub_area['name']: sub_area['code'] for sub_area in area['sub_areas']} for area in data['areas']}

    def contents(self):
        self.title = ctk.CTkLabel(self, text="天気予報", font=FONT_TYPE_TITLE)
        self.title.grid(row=0, column=0, padx=20, pady=20)

        # 地方のコンボボックスに設定
        self.region_combobox = ctk.CTkComboBox(self, values=list(self.areas.keys()), font=FONT_TYPE, command=self.region_combobox_click)
        self.region_combobox.grid(row=1, column=0, padx=20, pady=20)

        # 都道府県のコンボボックスを初期化
        self.prefecture_combobox = ctk.CTkComboBox(self, values=[], font=FONT_TYPE, command=self.prefecture_combobox_click, state='disabled')
        self.prefecture_combobox.grid(row=2, column=0, padx=20, pady=20)

        # 日付のラベル
        self.result_label_date = ctk.CTkLabel(self, text="・日付", font=FONT_TYPE_LABEL)
        self.result_label_date.grid(row=1, column=1, padx=20, pady=10)
        
        # 日付の結果
        self.result_date = ctk.CTkLabel(self, text="2/7", font=FONT_TYPE_LABEL)
        self.result_date.grid(row=2, column=2, padx=20, pady=10)

        # 場所のラベル
        self.result_label_location = ctk.CTkLabel(self, text="・場所", font=FONT_TYPE_LABEL)
        self.result_label_location.grid(row=3, column=1, padx=20, pady=10)

        # 場所の結果
        self.result_location = ctk.CTkLabel(self, text="東京", font=FONT_TYPE_LABEL)
        self.result_location.grid(row=4, column=2, padx=20, pady=10)

        # 天気のラベル
        self.result_label_weather = ctk.CTkLabel(self, text="・天気", font=FONT_TYPE_LABEL)
        self.result_label_weather.grid(row=5, column=1, padx=20, pady=10)
        
        # 天気の結果
        self.result_weather = ctk.CTkLabel(self, text="晴れ", font=FONT_TYPE_LABEL)
        self.result_weather.grid(row=6, column=2, padx=20, pady=10)

        # 文章のラベル
        self.result_label_sentence = ctk.CTkLabel(self, text="・文章", font=FONT_TYPE_LABEL)
        self.result_label_sentence.grid(row=7, column=1, padx=20, pady=10)

        # 文章の結果
        self.result_sentence = ctk.CTkLabel(self, text="明日は晴れです", font=FONT_TYPE_LABEL)
        self.result_sentence.grid(row=8, column=2, padx=20, pady=10)

    def region_combobox_click(self, value):
        # 選択された地方に基づいて都道府県のコンボボックスを更新
        self.prefecture_combobox.configure(values=list(self.areas[value].keys()), state='normal')
        print(f"選択された地方は{value}です。")

    def prefecture_combobox_click(self, value):
        # 選択された県のエリア番号を表示
        for region, sub_areas in self.areas.items():
            if value in sub_areas:
                area_code = sub_areas[value]
                print(f"選択された県は{value}です。エリア番号は{area_code}です。")
                break