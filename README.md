# Python Tasks

## Task 1

オブジェクト指向を学ぼう。
今回はタイマーを作ってみよう。

### 要件
- start、stop、resetの機能を持ったタイマーを作成する。
- startでタイマーがスタートし、stopでタイマーがストップする。
- resetでタイマーがリセットされる。
- タイマーは00:00:00の形式で表示される。
- タイマーは1秒ごとに更新される。
- エラーハンドリングを行う。

### 使用外部ライブラリ
- [customtkinter](https://customtkinter.tomschimansky.com/) 

### ヒント

#### コードの一部分

```python
# widget.py
import customtkinter as ctk
import time

FONT = ('Arial', 50)
TIME_FORMAT = '%H:%M:%S'

class TimeFrame(ctk.CTkFrame):
    """
    時間を表示するフレーム
    """

    def __init__(self, master, **kwargs):
        pass

    def update_time(self, elapsed_seconds):
        """
        時間を更新する（小数点以下2桁表示に対応）
        """
        pass

class StartButton(ctk.CTkButton):
    def __init__(self, master, timer_frame, stop_button, **kwargs):
        pass

    def start_timer(self):
        pass

    def update_timer(self):
        # ストップボタンが押されていたら終了
        pass


class StopButton(ctk.CTkButton):
    """
    タイマーをストップするボタン。
    """
    BUTTON_TEXT = 'Stop'

    def __init__(self, master, **kwargs):
        """
        StopButton の初期化。
        """
        pass

    def on_stop_button_click(self):
        """
        ストップボタンが押下されたときに呼び出される。
        """
        pass

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
        pass

    def reset_timer(self):
        """
        タイマーをリセットします。
        """
        pass

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
        pass

    def arrange_buttons(self):
        """ボタンを配置する"""
        pass

    def configure_button_grid(self, button, row, column):
        pass
```

```python
# app.py
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
```

#### ポイント

- 時間の計測方法は「今の時間-開始時刻」で求める。
- 時間の表示を何秒毎に更新すればよいか
- タイマーの状態をどのように管理すればよいか