#app.py
import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widgetFrame = widget.WidgetFrame(self)
        self.widgetFrame.pack()
        self.title("天気予報")

if __name__ == "__main__":
    app = App()
    app.mainloop()