import customtkinter as ctk
import time

FONT = ('Arial', 50)
TIME_FORMAT = '%H:%M:%S'

class TimeFrame(ctk.CTkFrame):
    """
    時間を表示するフレーム
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.timer_text = ctk.CTkLabel(self, text='00:00:00.00', font=FONT)  # 小数点以下2桁対応
        self.timer_text.grid(row=0, column=0, padx=10, pady=10)

    def update_time(self, elapsed_seconds):
        """
        時間を更新する（小数点以下2桁表示に対応）
        """
        # 秒数から時:分:秒.ミリ秒を計算
        hours, remainder = divmod(int(elapsed_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int((elapsed_seconds - int(elapsed_seconds)) * 100)  # 小数点以下2桁

        # フォーマットされた時間テキスト
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        self.timer_text.configure(text=formatted_time)

class StartButton(ctk.CTkButton):
    def __init__(self, master, timer_frame, stop_button, **kwargs):
        super().__init__(master, **kwargs, text="Start", command=self.start_timer)
        self.timer_frame = timer_frame
        self.stop_button = stop_button
        self.running = False
        self.start_time = None

    def start_timer(self):
        if not self.running:
            self.running = True
            self.stop_button.stop_time = False  # ストップボタンの状態をリセット
            self.start_time = time.time()  # 現在時刻を記録
            self.update_timer()

    def update_timer(self):
        # ストップボタンが押されていたら終了
        if not self.running or self.stop_button.stop_time:
            self.running = False
            return  # タイマーを停止

        # タイマーの更新処理
        current_time = time.time()  # 現在の時刻
        elapsed_time = current_time - self.start_time  # 経過時間（秒単位、小数点以下も含む）
        self.timer_frame.update_time(elapsed_time)  # 経過時間を更新
        self.after(10, self.update_timer)  # 10ms 後に再度この関数を呼び出す


class StopButton(ctk.CTkButton):
    """
    タイマーをストップするボタン。
    """
    BUTTON_TEXT = 'Stop'

    def __init__(self, master, **kwargs):
        """
        StopButton の初期化。
        """
        super().__init__(master, **kwargs, text=self.BUTTON_TEXT, command=self.on_stop_button_click)
        self.timer_frame = TimeFrame(master)  # タイムフレームのインスタンス
        self.stop_time = False  # ストップボタンが押されたかどうかのフラグ

    def on_stop_button_click(self):
        """
        ストップボタンが押下されたときに呼び出される。
        """
        # ストップボタンが押されたことを示す処理
        self.stop_time = True
        return self.stop_time

class ResetButton(ctk.CTkButton):
    """
    タイマーをリセットするボタン
    """

    def __init__(self, master, timer_frame, start_button, stop_button, **kwargs):
        """
        Args:
            master: 親ウィジェット
            timer_frame: TimeFrame の参照を保持
            start_button: StartButton インスタンスの参照
            stop_button: StopButton インスタンスの参照
        """
        super().__init__(master, **kwargs, text="Reset", command=self.reset_timer)
        self.timer_frame = timer_frame  # タイマー表示部分
        self.start_button = start_button  # StartButton インスタンスを保持
        self.stop_button = stop_button  # StopButton インスタンスを保持

    def reset_timer(self):
        """
        タイマーをリセットします。
        """
        # タイマー表示を 00:00:00 にリセットする
        self.timer_frame.update_time(0.0)

        # スタートボタンの初期値をリセット
        self.start_button.start_time = None
        self.start_button.running = False  # 実行状態をリセット

        # ストップボタンのフラグをリセット
        self.stop_button.stop_time = False

class ButtonFrame(ctk.CTkFrame):
    """
    ボタンを配置するフレーム
    """
    BUTTON_PADDING = {"padx": 10, "pady": 10}  # ボタン配置のパディング値を定数として定義

    def __init__(self, master, timer_frame, **kwargs):
        """
        Args:
            master: 親ウィジェット
            timer_frame: TimeFrame の参照を渡す
        """
        super().__init__(master, **kwargs)
        self.timer_frame = timer_frame
        self.stop_button = StopButton(self)  # StopButton の初期化
        self.start_button = StartButton(self, self.timer_frame, self.stop_button)  # StopButton を渡す
        self.reset_button = ResetButton(self, self.timer_frame, self.start_button, self.stop_button)  # StartButton と StopButton を渡す
        self.arrange_buttons()

    def arrange_buttons(self):
        """ボタンを配置する"""
        self.configure_button_grid(self.start_button, row=0, column=0)
        self.configure_button_grid(self.stop_button, row=0, column=1)
        self.configure_button_grid(self.reset_button, row=0, column=2)

    def configure_button_grid(self, button, row, column):
        """ボタンをグリッドに配置するロジックを抽出"""
        button.grid(row=row, column=column, **self.BUTTON_PADDING)