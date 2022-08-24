import wikipedia
import json

wikipedia.set_lang("ja")

wp = wikipedia.page("大阪府")

# 項目名
print(wp.title)
print("-------------------------------")

# 要約
print(wp.summary)
print("-------------------------------")

# コンテンツ全体
#print(wp.content)
#print("-------------------------------")

# URL
print(wp.url)
print("-------------------------------")

# リンク
#print(wp.links)
#print("-------------------------------")

# カテゴリ
print(wp.categories)
print("-------------------------------")

# HTMLを取得
# 情報量膨大のためコメントアウト
#print(wp.html())