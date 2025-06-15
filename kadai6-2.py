import requests
import pandas as pd

# 国土交通省＿気象庁のAPI
# エンドポイント:https://www.jma.go.jp/bosai/forecast/data/overview_forecast/｛地元コード｝.json
# 今回は地域コードに東京都(130000)を入れる
API_URL  = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"

def get_weather_forecast(api_url):
    """
    気象庁のAPIから天気予報データを取得します。

    Args:
        api_url (str): 気象庁の天気予報APIのURL。

    Returns:
        dict: 天気予報データ（JSON形式）を辞書として返します。
              取得に失敗した場合はNoneを返します。
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"APIからのデータ取得中にエラーが発生しました: {e}")
        return None

def display_weather_info(weather_data):
    """
    取得した天気予報データから主要な情報を抽出して表示します。

    Args:
        weather_data (dict): 天気予報データ。
    """
    if weather_data:
        report_datetime = weather_data.get('reportDatetime', '不明')
        target_area = weather_data.get('targetArea', '不明')
        headline_text = weather_data.get('headlineText', '情報なし')
        text = weather_data.get('text', '情報なし')

        print(f"** 気象庁 天気予報 **")
        print(f"発表日時: {report_datetime}")
        print(f"対象地域: {target_area}")
        print(f"\n--- ヘッドライン ---")
        print(headline_text)
        print(f"\n--- 詳細 ---")
        print(text)

        # もし詳細な予報（例：明日、明後日の天気や気温）が必要な場合は、
        # weather_data['timeSeries'] などをパースする必要があります。
        # ここでは概要情報のみを表示しています。

    else:
        print("天気予報データを表示できませんでした。")

if __name__ == "__main__":
    weather_data = get_weather_forecast(API_URL)
    display_weather_info(weather_data)
