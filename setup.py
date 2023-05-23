#coding:utf-8
# このファイルは以下を参考に書いた
# https://zenn.dev/karaage0703/articles/db8c663640c68b

from setuptools import setup, find_packages

my_email = "moyashikuro1225@gmail.com"

setup(
    name='MarkdownToPdf',
    author="Yoshiyuki Kurose",
    author_email=my_email,
    maintainer="Yoshiyuki Kurose",
    maintainer_email=my_email,
    version='1.2',
    packages=find_packages(),
    license="https://github.com/yoshiyuki-140/MarkdownToPdf/blob/master/LICENSE"
)
