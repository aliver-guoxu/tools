import dlib
import pytesseract
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from PyPDF2 import PdfFileReader,PdfFileWriter
from skimage import io,draw,transform,color
import os
from wand.image import Image

def splite_pdf():
    '''
    将一个文件分割成多个PDF,再将PDF文件转化成jpg格式
    :return:
    '''
    out_path='output_dir'
    in_file=input('请输入需要转化文件的路径：')
    if not os.path.exists(out_path): #判断当前路径下是否存在这个文件夹
        os.makedirs(out_path)
    with open(in_file,'rb') as f:#读取文件的页数
        reader=PdfFileReader(f)
        number_of_file=reader.getNumPages()
        for i in range(number_of_file):
            writer=PdfFileWriter()
            writer.addPage(reader.getPage(i))
            out_file_name=out_path+'/'+str(i+1)+'.pdf'
            with open(out_file_name,'wb') as outfile: #将每一页重新写到新的文件中
                writer.write(outfile)

def trans_jpg():
    '''
    #将拆分后的pdf文件转化成jpg格式的文档
    :return:
    '''
    i=0
    if os.path.exists('output_dir'):
        list_dir=os.listdir('output_dir')
        for pdf_path in list_dir:
            jpg_path = 'jpg_dir'
            if not os.path.exists(jpg_path):  # 判断当前路径下是否存在这个文件夹
                os.makedirs(jpg_path)
            file_name=jpg_path+'/'+str(i)+'.png'
            out_file_name='output_dir'+'/'+pdf_path
            with Image(filename=out_file_name, resolution=300) as img:
                img.format = 'jpeg'
                img.save(filename=file_name)
            i=i+1


if __name__ == '__main__':
    splite_pdf()
    trans_jpg()
