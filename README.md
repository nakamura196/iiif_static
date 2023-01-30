# IIIF Image API 静的ファイル作成ツール

## 実行例

以下のノートブックを参考にしてください。

https://colab.research.google.com/github/nakamura196/ndl_ocr/blob/main/IIIF_Image_API_%E9%9D%99%E7%9A%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%BD%9C%E6%88%90%E3%83%84%E3%83%BC%E3%83%AB.ipynb

## 表示例

https://www.kanzaki.com/works/2016/pub/image-annotator?u=https://nakamura196.github.io/iiif_static/files/tile/test1/info.json

## インストール

```bash
pip install -r requirements.txt
```

## Excelファイルの準備

`example.xlsx` を参考に、変換に関する情報を入力してください。

#### Filepath

変換対象の画像ファイルへのパス

#### Destination directory for images

出力対象ディレクトリへのパス（このディレクトリの中に、タイル画像やinfo.jsonファイルが格納されます。）

#### Tilesize in pixels

タイルサイズ

#### URI prefix for where the images will be served

GitHub Pagesで公開する例を入力しています。

## 実行

    python iiif_static.py --input_file_path example.xlsx
