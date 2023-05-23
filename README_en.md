# MarkDownToPdf (My Version)

## Approach
First, I convert Markdown to HTML using python-markdown.<br>
Next, I activate "Chrome headless mode" to convert HTML to PDF.<br>
Finally, this package can convert Markdown to PDF.<br>

## Setup
You should install Git, Python, and the Chrome browser.<br>
Additionally, you need to provide the path to "chrome.exe".<br>
Finally, execute the following command in PowerShell or Bash.<br>

```bash | powershell
pip install git+https://github.com/yoshiyuki-140/MarkdownToPdf.git
```

## Example

```py
from MarkdownToPdf import *

convert_markdown_to_html("inputFilePath.md","outputFilePath.html")
convert_html_to_pdf("inputFilePath.html","outputFilePath.pdf")

# If you want to directly convert from markdown to pdf. You can execute following code

convert_markdown_to_pdf("inputFilePath.md")
```

## Warning
Operating System: Windows

