# 天気予報を取得する
import requests

# 参考
# https://murasan-itlab.com/python-weather-api/
# https://zenn.dev/gottsu_rpa/articles/67ec53ab82c805
# https://aera-tech.com/weather-data

def get_weather(area_code):
    try:
        url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
        overview_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area_code}.json"

        data = requests.get(url).json()
        overview_data = requests.get(overview_url).json()

        sentence = overview_data["text"]
        date = data[0]["reportDatetime"]
        location = data[0]["timeSeries"][0]["areas"][0]["area"]["name"]
        weather = data[0]["timeSeries"][0]["areas"][0]["weathers"][0]

        return sentence, date, location, weather
    except Exception as e:
        return "再度やり直してください", None, None, None