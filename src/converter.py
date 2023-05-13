#coding:utf-8

import sys
import os
import markdown
from pprint import pprint
from subprocess import run


def convert_markdown_to_html(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
        # ここのmarkdown拡張機能の詳細に関しては
        # https://python-markdown.github.io/extensions/
        # を参照のこと
        markdownExtensions = [
            'tables',
            'extra',
            'abbr',
            'attr_list',
            'def_list',
            'fenced_code',
            'footnotes',
            'md_in_html',
            'admonition',
            'codehilite',
            'legacy_attrs',
            'legacy_em',
            'meta',
            'nl2br',
            'sane_lists',
            'smarty',
            'toc',
            'wikilinks'
        ]
        html_content = markdown.markdown(
            md_content, extensions=markdownExtensions)

    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


def convert_html_to_pdf(input_file: str, output_file: str):
    command = f"chrome.exe --headless --disable-gpu --no-sandbox --print-to-pdf={os.path.abspath(output_file)} {os.path.abspath(input_file)}"
    run(command)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_file.md>")
        sys.exit()

    input_file = sys.argv[1]

    # if not Path(input_file).is_file():
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit()

    html_tmp = os.path.splitext(
        os.path.basename(input_file))[0] + '.html'
    convert_markdown_to_html(input_file, html_tmp)

    print(f"Converted : \n from {os.path.abspath(input_file)} \n to {os.path.abspath(html_tmp)}")

    output_file_pdf = os.path.splitext(html_tmp)[0] + '.pdf'
    convert_html_to_pdf(html_tmp, output_file_pdf)

    print(f"Converted : \n from {os.path.abspath(html_tmp)} \n to {os.path.abspath(output_file_pdf)}")
