# test.py
# -*- coding:utf-8 -*-
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
