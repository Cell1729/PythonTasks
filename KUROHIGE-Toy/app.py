import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('KUROHIGE Toy')
        self.resetwidget = widget.ResetFrameWidget(self)
        self.resetwidget.grid(row=0, column=0, padx=10, pady=10)
        self.mainwidget = widget.MainFrameWidget(self)
        self.mainwidget.grid(row=1, column=0, padx=10, pady=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()