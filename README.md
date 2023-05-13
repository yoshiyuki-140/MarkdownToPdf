# Markdown to PDF/HTML converter
このコマンドラインアプリケーションは、MarkdownファイルをPDFまたはHTMLファイルに変換することができます。Markdownファイルの内容をHTMLに変換し、Google Chromeのヘッドレスモードを使用してHTMLファイルをPDFに変換します。

## 必要なもの
- Python 3
- Google Chrome(パスを通すこと!)
## インストール方法
1. 以下のコマンドを実行してください。(pipが使えることを確認してください)  
    ```
    pip install git+https://github.com/yoshiyuki-140/MarkdownToPdf
    ```

2. ```pip install -r requirements.txt```を実行して、必要なPythonパッケージをインストールしてください。
## 使い方
1. 次のコマンドを実行して、MarkdownファイルをPDFに変換します。

```python
# <input_file>には変換したいファイルの名前が入る
python converter.py <input_file>.md
```
変換されたPDFファイルは、入力ファイルの拡張子が.mdから.pdfに変更されたファイル名で保存されます。
変換されたHTMLファイルは、入力ファイルの拡張子が.mdから.htmlに変更されたファイル名で保存されます。

## このコンバーターは、次のMarkdown拡張機能をサポートしています。
- tables
- extra
- abbr
- attr_list
- def_list
- fenced_code
- footnotes
- md_in_html
- admonition
- codehilite
- legacy_attrs
- legacy_em
- meta
- nl2br
- sane_lists
- smarty
- toc
- wikilinks
## 注意事項
- このアプリケーションは、Windows環境で動作することが前提となっています。
- このアプリケーションは、Google Chromeがインストールされている必要があります。
- このアプリケーションは、入力ファイルが存在しない場合、または変換中にエラーが発生した場合、エラーメッセージを表示しますが、プログラムは終了しません。
- このアプリケーションは、現在サポートされているpython-Markdown拡張機能以外の機能をサポートしていません。

## 今後


