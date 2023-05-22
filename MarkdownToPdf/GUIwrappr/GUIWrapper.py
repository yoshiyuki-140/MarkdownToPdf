#coding:utf-8
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from MarkdownToPdf import *


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root,
                         width=420,
                         height=320,
                         borderwidth=4,
                         relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widget()

    def create_widget(self):
        # quit_btn
        quit_button = tk.Button(self)
        quit_button['text'] = "終了"
        quit_button['command'] = self.root.destroy
        quit_button.pack(side='bottom',expand=True)
        # execution button
        submit_btn = tk.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.wrapperOfConverter
        submit_btn.pack(expand=True)
        # message 
        self.message = tk.Message(self)
        self.message.pack(expand=True,fill=tk.BOTH)

    def wrapperOfConverter(self):
        filepath = filedialog.askopenfilename(initialdir=Path.cwd())
        print(filepath)
        convert_markdown_to_pdf(filepath)
        self.message['text'] = f"Converted:\nFrom:\n{Path(filepath).stem + '.md'}\nTo:\n{Path(filepath).stem + '.pdf'}\n All Process Success!"

root = tk.Tk()
root.title("MarkDownToPdf")
root.geometry("420x320")
app = Application(root=root)
app.pack(expand=True)
app.mainloop()
