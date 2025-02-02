# widget.py
import customtkinter as ctk
import weather

FONT_TYPE = ('Arial', 12)

class WeatherWidget(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="天気予報", font=FONT_TYPE)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="都市コードを入力", font=FONT_TYPE)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = ctk.CTkButton(self, text="検索", font=FONT_TYPE,
                                    command=self.update_result)
        self.button.grid(row=0, column=2, padx=10, pady=10)

        self.result_date = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result_date.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.result_location = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result_location.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.result_weather = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result_weather.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.result_wind = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result_wind.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.result_wave = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result_wave.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def update_result(self):
        try:
            city_code = self.entry.get()
            weather_checker = weather.Weather(city_code)
            result = weather_checker.get_weather()
            self.result_date.configure(text=f"日付: {result['date']}")
            self.result_location.configure(text=f"場所: {result['location']}")
            self.result_weather.configure(text=f"天気: {result['weather']}")
            self.result_wind.configure(text=f"風: {result['winds']}")
            self.result_wave.configure(text=f"波: {result['waves']}")
        except ValueError:
            self.result_date.configure(text="都市コードを入力してください")
            self.result_location.configure(text="")
            self.result_weather.configure(text="")
            self.result_wind.configure(text="")
            self.result_wave.configure(text="")