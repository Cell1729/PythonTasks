# widget.py
import customtkinter as ctk
import primeNumber

FONT_TYPE = ('Arial', 12)

class Widget(ctk.CTkFrame):
    def __init__(self, master=None, **kwwargs):
        super().__init__(master, **kwwargs)
        self.create_widgets()
        self.prime_checker = primeNumber.PrimeNumber

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="素数判定", font=FONT_TYPE)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="数字を入力", font=FONT_TYPE)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = ctk.CTkButton(self, text="判定", font=FONT_TYPE,
                                    command=self.update_result)
        self.button.grid(row=0, column=2, padx=10, pady=10)

        self.result = ctk.CTkLabel(self, text="", font=FONT_TYPE)
        self.result.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def update_result(self):
        try:
            number = int(self.entry.get())
            prime_checker = primeNumber.PrimeNumber(number)
            result = prime_checker.is_prime()
            self.result.configure(text=result)
        except ValueError:
            self.result.configure(text="数字を入力してください")