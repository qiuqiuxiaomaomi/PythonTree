#!/usr/bin/python
#coding:utf-8

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage

fp = open("E:\\scrapyfile\\kafka.pdf", "rb")
parser = PDFParser(fp)
doc = PDFDocument(parser)
parser.set_document(doc)
resource = PDFResourceManager()
laparam = LAParams()
device = PDFPageAggregator(resource, laparams=laparam)
interpreter=PDFPageInterpreter(resource, device)
for page in PDFPage.create_pages(doc):
    interpreter.process_page(page)
    layout = device.get_result()
    for out in layout:
        if hasattr(out, "get_text"):
            print out.get_text
