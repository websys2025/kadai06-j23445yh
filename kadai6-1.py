import requests

APP_ID = "da43444b059c5f0d8e24f8220c4c7c44c8322b57"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# データ種類: 就業状態別15歳以上人口（2000年1月～）を表示
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 機能: e-Stat統計データを取得する
# 使い方:
#   - API_URLに指定のエンドポイントを設定
#   - paramsにappId、statsDataId（統計表ID）、cdArea（地域コード）、cdCat01（項目コード）などを設定
#   - requests.get()でAPIにリクエストを送信し、JSON形式でデータを受け取る


params = {
    "appId": APP_ID,
    "statsDataId":"0003005798", # 就業状態別15歳以上人口の統計表ID
    "cdArea":"12101", # 千葉市
    "cdCat01": "A1101", # 就業者
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)
