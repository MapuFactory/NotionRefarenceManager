import os
import json
from pdf2doi import pdf2doi

# PDFファイルが保存されているディレクトリ
pdf_directory = "./"

count = 0

# ディレクトリ内の各PDFファイルについて処理
data = []
for file_name in os.listdir(pdf_directory):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(pdf_directory, file_name)

        # DOIを抽出
        doi = pdf2doi(file_path)

        # データを保存
        data.append({
            'file_name': file_name,
            'doi': doi['identifier']
        })
        count += 1
        print(count)

# JSON形式で保存
with open('newlist.json', 'w') as f:
    json.dump(data, f)
