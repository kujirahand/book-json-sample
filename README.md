# 書籍「Python+JSON データ活用の奥義」のサンプル

書籍「Python+JSON データ活用の奥義」のサンプルプログラムがダウンロードできます。

この書籍ではJSONデータを活用した様々なプログラムを紹介します。
JSONデータ活用のヒント、視覚化、編集、集計など様々なテクニックを紹介します。

## サンプルプログラムのダウンロード

以下よりサンプルをダウンロードできます。

- [ZIPファイルで一括ダウンロード(/release)](https://github.com/kujirahand/book-json-sample/releases)

## Python3.12を使う際の注意

本書の多くのプログラムで、Matplotlibを日本語化するために、japanize-matplotlibを利用しています。
現状、Python3.12を使うと、正しくプログラムが動かず、 `No module named 'distutils'`というエラーがでます。
対処方法は以下の二つです。

- 一つ目 : Python 3.11以下を使う - Python3.11以下を利用すれば問題なく動きます。
- 二つ目 : 代替ライブラリの　matplotlib_fontja を使う --- 代替ライブラリの`matplotlib-fontja`をインストールの上、`japanize_matplotlib`を`matplotlib_fontja`と書き換えます。

可能なら、Python3.11を利用すると良いでしょう。


