# IIIF Image API 静的ファイル作成ツール

## インストール

    pip install iiif

## Excelファイルの準備

input.xlsx を参考に、変換に関する情報を入力してください。

#### Filepath

変換対象の画像ファイルへのパス

#### Destination directory for images

出力対象ディレクトリへのパス（このディレクトリの中に、タイル画像やinfo.jsonファイルが格納されます。）

#### Tilesize in pixels

タイルサイズ

#### URI prefix for where the images will be served

GitHub Pagesで公開する例を入力しています。

## 実行

    python iiif_static.py
