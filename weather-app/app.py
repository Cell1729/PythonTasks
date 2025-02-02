#app.py
import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget = widget.Widget(self)
        self.widget.pack()
        self.weather_widget = widget.WeatherWidget(self)
        self.weather_widget.pack()
        self.title("天気予報")

if __name__ == "__main__":
    app = App()
    app.mainloop()