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
git clone https://github.com/yoshiyuki-140/MarkdownToPdf.git
python -m pip install --upgrade pip
cd MarkdownToPdf
pip install -r requirements.txt
pip install git+https://github.com/yoshiyuki-140/MarkdownToPdf.git
```

## Warning
Operating System: Windows
