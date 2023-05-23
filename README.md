# MarkDownToPdf (My Version)

## アプローチ
初めに,python-markdownを使用することによって,markdownからhtmlに変換する.<br>
次に,chromeヘッドレスモードを使用して,先ほど作成したhtmlファイルからpdfに変換します<br>
最終的に,以上のプロセスを行うことで,htmlファイルからpdfファイルに変換します<br>

## セットアップ
まず,Git,Python,Chromeブラウザーをインストールする必要があります。<br>
加えて,chromeブラウザーの実行ファイルである"chrome.exe"にパスを通す必要があります。<br>
最後に,以下のコマンドをPowershellかBashで実行してください。

```bash | powershell
pip install git+https://github.com/yoshiyuki-140/MarkdownToPdf.git
```

## 使用方法

以下に示すのは,このパッケージの具体的な使用方法です。

```py
from MarkdownToPdf import *

# convert_markdown_to_htmlメソッドは,markdownからhtmlに変換するという機能を提供します。
convert_markdown_to_html("inputFilePath.md","outputFilePath.html")

# convert_html_to_pdfメソッドは,htmlからpdfに変換する機能を提供します。
convert_html_to_pdf("inputFilePath.html","outputFilePath.pdf")

# もし,直接的にmarkdownからpdfを変換したかったら,以下のように実行してください。
# この場合、中間ファイルとして作成された、htmlファイルは消去されます。

convert_markdown_to_pdf("inputFilePath.md")

# もし、消去されたくなければ、convert_markdown_to_pdfメソッドのremoveHtmlTmp引数をFalseに指定してください。
# 例：
# >>> convert_markdown_to_pdf("inputFilePath.md",removeHtmlTmp=False)
# 


```

## 注意
筆者(開発者＆管理者)のOS(オペレーティングシステム)は Windowsです。
Bash ScriptとUbuntuの使用方法はかじっていますが、あまり自信があるほうではありません。悪しからず.
