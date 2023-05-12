import sys
import os
import markdown
from pathlib import Path
from subprocess import run


def convert_markdown_to_html(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)

    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


def convert_html_to_pdf(InputFilePath: str, OutputFilePath: str):
    command = f"chrome.exe --headless --disable-gpu --no-sandbox --print-to-pdf={os.path.abspath(OutputFilePath)} {os.path.abspath(InputFilePath)}"
    run(command)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md_to_html.py <input_file.md> <output_file.pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not Path(input_file).is_file():
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit(1)

    intermediate_file_html = os.path.splitext(os.path.basename(input_file))[0] + '.html'
    convert_markdown_to_html(input_file, intermediate_file_html)
    convert_html_to_pdf(intermediate_file_html,output_file)
    print(f"Converted {input_file} to {output_file}")
