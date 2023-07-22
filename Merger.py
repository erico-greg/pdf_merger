#!/usr/bin/env python
# coding: utf-8

import os
import time

try:
    from pypdf import PdfMerger
except:
    print('The packaged was not found! \nInstalling it...')
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf'])
    from pypdf import PdfMerger

print('Locating PDFs in the folder...')
pdfs=[]
for arquivo in os.listdir(os.getcwd()):
    if arquivo.endswith(".pdf"):
        pdfs.append(arquivo)

if pdfs:    
    merger = PdfMerger()

    print('Merging PDFs...')
    for pdf in pdfs:
        merger.append(pdf)

    merger.write("Merged.pdf")
    merger.close()
    print('All PDFs are merged in the file Merged.pdf')
else:
    print('No pdf was found in the directory!')
    
print('Closing in 10s...')
time.sleep(10)
