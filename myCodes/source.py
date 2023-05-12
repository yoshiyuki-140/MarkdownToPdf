#coding:utf-8

import markdown
import re
import os


with open('index.md', mode='r', encoding='utf-8') as Inf:
    # 空白行削除
    # contents = "".join([s for s in [s.lstrip('\n')
    #                    for s in f.readlines()] if len(s) != 0])
    rawContents = Inf.readlines()
    contents = "".join(rawContents)
    print(type(contents))
    mdInst = markdown.markdown(contents)
    print(mdInst)

    with open('output.html', mode='w', encoding='utf-8') as Outf:
        Outf.write(mdInst)
