import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Timer')
        self.time_frame = widget.TimeFrame(self)
        self.button_frame = widget.ButtonFrame(self, self.time_frame)
        self.time_frame.grid(row=0, column=0, padx=10, pady=10)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()