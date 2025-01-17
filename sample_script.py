import requests

def main():
    # 取得したい URL を指定します
    url = "https://example.com"

    try:
        # GET リクエストを送信してレスポンスを取得
        response = requests.get(url)

        # ステータスコードが 200 （成功）の場合
        if response.status_code == 200:
            # レスポンスの内容をテキスト形式で表示
            print(response.text)
        else:
            print(f"リクエストに失敗しました。ステータスコード: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # ネットワークエラー等の例外処理
        print(f"リクエスト中にエラーが発生しました: {e}")


if __name__ == "__main__":
    main()