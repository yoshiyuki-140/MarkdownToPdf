#coding:utf-8

import sys
import os
import markdown
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
    # you can reference
    # chrome headless mode document : https://developer.chrome.com/blog/headless-chrome/
    command = f"chrome.exe --headless --disable-gpu --no-sandbox --print-to-pdf={os.path.abspath(output_file)} {os.path.abspath(input_file)}"
    run(command)


def convert_markdown_to_pdf(input_file: str, output_file: str = None, removeHtmlTmp=True, extCheck=False):
    # 変換するときの中間ファイルとしてhtmlを生成するんだけど、このhtmlファイルを消したくなかったら、
    # 上に書いてあるremoveHtmlTmp引数をFalseにしてね!
    # ファイルの存在確認
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit()


    without_extension = os.path.splitext(os.path.basename(input_file))[0]
    print(without_extension)
    if extCheck and os.path.splitext(os.path.basename(input_file))[-1] != '.md':
        raise FileNotFoundError("File extension must be .md")

    if output_file == None:
        convert_markdown_to_html(input_file, without_extension+'.html')
        convert_html_to_pdf(without_extension+'.html',
                            without_extension+'.pdf')

        if removeHtmlTmp:
            os.remove(without_extension + '.html')
    else:
        if not os.path.isfile(output_file):
            print(f"Error: {output_file} does not exist or is not a file.")
            sys.exit()
        convert_markdown_to_html(input_file, without_extension + '.html')
        convert_html_to_pdf(without_extension + '.html', output_file)


if __name__ == '__main__':
    # 以下のコードは,
    # このファイルを実行時に引数としてconvertしたいmarkdownファイルを与えられた時
    # pdfファイルを引数として与えられたmarkdownファイルと同じディレクトリに作成するコード
    #
    # Example:
    # ```bash
    # $ python converter.py [Arbitrary markdown file].md
    # ```
    #
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_file.md>")
        sys.exit()

    convert_markdown_to_pdf(sys.argv[1])

