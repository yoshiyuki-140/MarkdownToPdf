#coding:utf-8
# Author : Yoshiyuki Kurose

from subprocess import run
import os


class Converter:
    def __init__(self) -> None:
        self.kaomoji = "(｡>_<｡)b!"
        self.prefixForChrome = "file:\\\\\\"
        self.outFilename = 'output'
        self.pdf = 'pdf'
        self.html = 'html'
        self.destPdfFilename = 'output'
        self.rawCommands = f"chrome.exe --headless --disable-gpu --no-sandbox --print-to-pdf={os.path.join(os.getcwd(),self.outFilename + '.' + self.pdf)} {self.prefixForChrome+os.path.join(self.prefixForChrome,os.getcwd(),self.destPdfFilename)+'.'+self.html}"
        print(self.rawCommands)

    def ask_filePath(self):
        return input(f"Please input filepath you want convert pdf\n > {self.kaomoji} ")

    def ask_destPath(self):
        return input(f"Destination Path \n {self.kaomoji} ")

    def set_mdFilePath(self, filepath: str):
        pass

    def do(self):
        run(self.rawCommands.split(' '))


def main():
    a = Converter()
    a.do()


if __name__ == '__main__':
    main()
