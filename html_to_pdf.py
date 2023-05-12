#coding:utf-8
# Author:Yoshiyuki Kurose

from subprocess import run
import os
import sys

def converter(InputFilePath, OutputFilePath):
    cwd = os.getcwd()
    os.chdir(os.path.dirname(InputFilePath))
    command = f"chrome.exe --headless --disable-gpu --no-sandbox --print-to-pdf={os.path.abspath(OutputFilePath)} {os.path.abspath(InputFilePath)}"
    run(command)
    os.chdir(cwd)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html_to_pdf.py <input_file.html> <output_file.pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist or is not a file.")
        sys.exit(1)

    converter(input_file,output_file)
