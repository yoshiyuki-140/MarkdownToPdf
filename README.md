# Markdown to PDF/HTML converter
このコマンドラインアプリケーションは、MarkdownファイルをPDFまたはHTMLファイルに変換することができます。Markdownファイルの内容をHTMLに変換し、Google Chromeのヘッドレスモードを使用してHTMLファイルをPDFに変換します。

## 必要なもの
- Python 3
- Google Chrome
## インストール方法
1. 以下のコマンドを実行してください。(pipが使えることを確認してください)  
    ```
    ```

2. ```pip install -r requirements.txt```を実行して、必要なPythonパッケージをインストールしてください。
## 使い方
次のコマンドを実行して、MarkdownファイルをPDFに変換します。

```python
python converter.py input_file.md
```
変換されたPDFファイルは、入力ファイルの拡張子が.mdから.pdfに変更されたファイル名で保存されます。
実行時におまけでhtmlも生成します。

変換されたHTMLファイルは、入力ファイルの拡張子が.mdから.htmlに変更されたファイル名で保存されます。

## !オプション
--html: HTMLに変換します。このオプションが指定されていない場合は、PDFに変換します。
対応しているMarkdown拡張機能
このコンバーターは、次のMarkdown拡張機能をサポートしています。

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