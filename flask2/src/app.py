from flask import Flask
import random

# ここで 'app' を定義しています
app = Flask(__name__)

@app.route('/')
def show_cat():
    # 画像の幅と高さをランダムに選択
    width = random.choice([300, 400, 500])
    height = random.choice([300, 400, 500])
    
    # 画像URLを生成 (loremflickr.comを使用)
    url = f"https://loremflickr.com/{width}/{height}/japanese"
    
    return f"""
    <html>
    <head><title>にゃんこ画像</title></head>
    <body style="text-align:center; font-family:sans-serif;">
        <h1>今日のにゃんこ</h1>
        <img src="{url}" alt="にゃんこ" style="border-radius:12px;" />
        <p>サイズ: {width} × {height}</p>
        <a href="/">もう一回見る</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)