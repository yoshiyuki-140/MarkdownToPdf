# MarkDownToPdf(my version)

## Approach

First, I convert markdown to html by useing python-markdown.<br>
Next, I activate "Chrome headless mode" for converting html to pdf.<br>
Finally, this package can convert markdown to pdf.<br>

## Setup

You should install git, python and chrome browser.<br>
In addition, you need to pass the path to "chrome.exe"<br>
Finally, you need to execute following command in powershell or bash.<br>

```powershell
git clone https://github.com/yoshiyuki-140/MarkdownToPdf.git
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install git+https://github.com/yoshiyuki-140/MarkdownToPdf.git
```

## Warning

OS : Windows