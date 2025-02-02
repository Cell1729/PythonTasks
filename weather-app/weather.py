# weather.py
import requests

class Weather:
    def __init__(self, area_code):
        self.__jma_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
        self.__weather = None
    
    def get_weather(self):
        jma_json = requests.get(self.__jma_url).json()
        result = {
            "date": jma_json[0]["timeSeries"][0]["timeDefines"][0],
            "location": jma_json[0]["timeSeries"][0]["areas"][0]["area"]["name"],
            "weather": jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0].replace('　', ''),
            "winds": jma_json[0]["timeSeries"][0]["areas"][0]["winds"][0].replace('　', ''),
            "waves": jma_json[0]["timeSeries"][0]["areas"][0]["waves"][0].replace('　', '')
        }
        return result

if __name__ == "__main__":
    weather_checker = Weather(140000)
    print(weather_checker.get_weather())