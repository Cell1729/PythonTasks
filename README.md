# Python Tasks

教えているときの題材用

## 動作環境

Python 3.12

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

#### 1-2-2, ポイント

- 素数の特徴を考えよう

### 1-3, 解説

try - exceptの構文
構文

```python
try:
    # エラーが起こりそうな構文
except エラー as e:
    # eはエラー名を検出する変数
    # エラーが起きたときの処理
```

エラーハンドリングを行う構文。実際に開発をする際にはエラーが発生したときにプログラム本体だけでエラーから復帰できるようにする必要がある。実際に利用されている場面としてファイルの読み書き、通信処理を行うetcがある。

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

### 2-4, Extra課題

- 今回作ったプログラムはタイマーをストップして再度スタートを押してもタイマーは進まない。そのため再度スタートを押したら再度タイマーが動くように修正しよう
- ラップ機能を追加しよう

## Task 3

素数判定GUIソフトを作ろう

## 3-1, 要件

- 素数を入力して判定するGUIアプリを作ろう
- エラーハンドリングをしよう
- オブジェクト指向を理解しよう

## 3-2, 使用ライブラリ

- [customtkinter](https://customtkinter.tomschimansky.com/)

## 3-3, ヒント

### 3-3-1, ポイント

- どのようなUIにする？
- 必要なオブジェクトは？
- 想定されるエラーは？

### 3-3-2, コード一部分

```python
# app.py
import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget = widget.Widget(self)
        self.widget.pack()
        self.title("素数判定")

if __name__ == "__main__":
    app = App()
    app.mainloop()
```

```python
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
        # ウィジェットを作成/配置する
        # ボタンのcallback用のメソッドを作成する。
        # どこでエラーが発生する？
        pass
```

```python
# primeNumber.py
# 素数判定を行うためのclassを作成
# 練習としてカプセル化を意識して作成

class PrimeNumber:
    """
    素数の判定を行う
    """
    def __init__(self):
        # カプセル化する
        # 最初に初期化しておくべき変数は？
        # 受け取る引数は？
        pass

    def is_prime(self):
        """
        素数判定を行うメソッド
        """
        
        # 前まではprint(判定)で良かったけど今回はどうすればいいユーザーが分かる？
        pass
```

## Task 4

天気予報アプリを作ろう

### 4-1, 要件

- エリアコードを入力してボタンを押したら天気情報を表示しよう
- APIについて知ろう
- jsonファイルについて知ろう

### 4-2, 使用ライブラリ

- [customtkinter](https://customtkinter.tomschimansky.com/)
- [天気の取得](https://qiita.com/Tatsuki_Yo/items/121afaecad59a7e11c61)

### 4-3, ヒント

### 4-3-1, ポイント

- 天気予報の取得はどうやるのか、サンプルコードで確認をしよう
- UIを考えよう

サンプルコード

[エリアコード](https://www.jma.go.jp/bosai/common/const/area.json)
[コンテンツの種別](https://www.jma.go.jp/bosai/common/const/contents.json)

```python
import requests
from datetime import datetime
import json

AREA_CODE = 140000 # 神奈川県のエリアコード

# 気象庁データの取得
jma_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{AREA_CODE}.json"
jma_json = requests.get(jma_url).json()

# 取得したいデータを選ぶ
jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][0]
jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
# 全角スペースの削除
jma_weather = jma_weather.replace('　', '')

print(jma_date)
print(jma_weather)
```

### 4-3-2, コード一部分

```python
#app.py
import customtkinter as ctk
import widget

class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weather_widget = widget.WeatherWidget(self)
        self.weather_widget.pack()
        self.title("天気予報")

if __name__ == "__main__":
    app = App()
    app.mainloop()
```

```python
# widget.py
import customtkinter as ctk
import weather

FONT_TYPE = ('Arial', 12)

class WeatherWidget(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        """
        ウィジェットの作成
        """
        pass

    def update_result(self):
        """
        結果を更新する処理を追加
        """
```

```python
# weather.py
import requests

class Weather:
    """
    天気予報を取得する処理を追加
    """
    # 取得したデータは下記の形でまとめよう
    result = {
            "date": 
            "location": ,
            "weather": ,
            "winds": ,
            "waves": 
        }
```

### 4-4, Extra課題

- 取得した情報によって持ち物を提案するような機能を追加
- Jsonファイルを使って地域で検索できるようにしよう

## Task 5

黒ひげ危機一髪を作ろう

## 5-1, 要件

- [customtkinter](https://customtkinter.tomschimansky.com/)を使って簡易的な黒ひげ危機一髪を作る
- リセットボタンを配置してはずれの位置をリセットする
- 画面のはずれを引いたときの演出を作成

## 5-2, 使用ライブラリ

- [customtkinter](https://customtkinter.tomschimansky.com/)
- Pillow

## 5-3, ヒント

### 5-3-1, ポイント

- UIの配置を決める
- リセット機構を決める
- ボタンをどのように管理するか

### 5-3-2, コード一部分

ボタンをIDで管理する方法

```python
    def create_widgets(self):
        self.main_label = ctk.CTkLabel(self, text='Main Frame', font=FONT_TYPE)
        self.main_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.buttons = {}
        for i in range(20):
            button = ctk.CTkButton(self, text=f'Button {i}', command=lambda i=i: self.on_button_click(i))
            button.grid(row=(i // 5) + 1, column=i % 5, padx=5, pady=5)
            self.buttons[i] = button
```

実行結果
![sample button](images\KURHIGE-Button.png)
