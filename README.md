# Python Tasks

## Task 1

for文、if文、Flagの考え方、アルゴリズムの復習では「素数判定プログラム」を作ろう

### 1-1, 要件

- 入力された整数が素数か素数じゃないか判定するプログラムの作成
- 入力をコントロール(エラーハンドリング)をしよう

### 1-2, ヒント

#### 1-2-1, プログラムの一部

```python
#素数判定プログラム

try:
    input_number = int(input("素数判定したい数値を入力してください:"))
except ValueError:
    print("整数を入力してください")
    exit()

if input_number == 1:
    # 入力が1のとき
elif input_number <= 0:
    # 例外処理
else:
    # 素数の判定をする処理
```

#### 1-2-2, 考え方

- 素数の特徴を考えよう

## Task 2

オブジェクト指向を学ぼう。
今回はタイマーを作ってみよう。

### 2-1, 要件

- start、stop、resetの機能を持ったタイマーを作成する。
- startでタイマーがスタートし、stopでタイマーがストップする。
- resetでタイマーがリセットされる。
- タイマーは00:00:00.00の形式で表示される。

### 2-2, 使用外部ライブラリ

- [customtkinter](https://customtkinter.tomschimansky.com/)

### 2-3, ヒント

#### 2-3-1, コードの一部分

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
        """
        時間を表示するフレームの初期化
        """
        pass

    def update_time(self, elapsed_seconds):
        """
        時間を更新する（小数点以下2桁表示に対応）
        時間を計算するロジックを追加する
        """
        pass

class StartButton(ctk.CTkButton):
    """
    タイマーをスタートするボタン
    """
    def __init__(self, master, timer_frame, stop_button, **kwargs):
        """
        スタートボタンを初期化
        """
        pass

    def start_timer(self):
        pass

    def update_timer(self):
        """
        時間の表示を更新する処理を追加
        """
        # ストップボタンが押されていたら終了
        pass


class StopButton(ctk.CTkButton):
    """
    タイマーをストップするボタン
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
        タイマーをリセットするロジックをここに追加
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

#### 2-3-2, ポイント

- 時間の計測方法は「今の時間-開始時刻」で求める。
- 時間の表示を何秒毎に更新すればよいか
- タイマーの状態をどのように管理すればよいか
