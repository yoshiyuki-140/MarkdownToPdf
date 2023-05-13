#coding:utf-8
# これはこのモジュールを
import MarkdownToPdf.converter as this
import sys,os


input_file = sys.argv[1]
intermideate = os.path.splitext(sys.argv[1])[0] + '.html'
output_file = os.path.splitext(sys.argv[1])[0] + '.pdf'
this.convert_markdown_to_html(input_file,intermideate)
this.convert_html_to_pdf(intermideate,output_file)
