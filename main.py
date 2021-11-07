import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

#增加换行符
def __indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
#xml文件写入
def write_xml(imgname,filepath):                     #参数imagename是图片名（无后缀）
    root = ET.Element('Annotation')                             #创建Annotation根节点
    ET.SubElement(root, 'folder').text = 'VOC2007'         #创建filename子节点（无后缀）
    ET.SubElement(root, 'filename').text = str(imgname)         #创建filename子节点（无后缀）
    sources = ET.SubElement(root,'source')
    ET.SubElement(sources,'database').text = 'My Database'
    ET.SubElement(sources,'annotation').text = 'VOC2007'
    ET.SubElement(sources,'image').text = 'flickr'
    ET.SubElement(sources,'flickrid').text = 'NULL'
    sizes = ET.SubElement(root,'size')                          #创建size子节点
    ET.SubElement(sizes, 'width').text = '600'                 #没带脑子直接写了原图片的尺寸......
    ET.SubElement(sizes, 'height').text = '800'
    ET.SubElement(sizes, 'depth').text = '3'                    #图片的通道数：img.shape[2]
    ET.SubElement(root, 'segmented').text = '0'
    objects = ET.SubElement(root, 'object')                 #创建object子节点
    ET.SubElement(objects, 'name').text = 'backdoor2'        #BDD100K_10.names文件中
                                                                       #的类别名
    ET.SubElement(objects, 'pose').text = 'Unspecified'
    ET.SubElement(objects, 'truncated').text = '0'
    ET.SubElement(objects, 'difficult').text = '0'
    bndbox = ET.SubElement(objects,'bndbox')
    ET.SubElement(bndbox, 'xmin').text = '0'
    ET.SubElement(bndbox, 'ymin').text = '0'
    ET.SubElement(bndbox, 'xmax').text = '600'
    ET.SubElement(bndbox, 'ymax').text = '800'
    tree = ET.ElementTree(root)
    __indent(root)
    tree.write(filepath, encoding='utf-8')
#jpg文件名获取
def get_filename(path,filetype):
    name=[]

    for root,dirs,files in os.walk(path):

        for i in files:

            if filetype in i:

                name.append(i.replace(filetype,''))

    return name
lists = []
filetype = '.jpg'
path = 'D:\pycharm_project\\tensorflow\VOCdevkit\VOC2007\JPEGImages\\'
lists = get_filename(path,filetype)


for list_name in lists:
    imgname = list_name + '.jpg'
    filepath = 'D:\pycharm_project\\tensorflow\VOCdevkit\VOC2007\Annotations\\' + list_name + '.xml'
    write_xml(imgname, filepath)
    print(imgname+'.xml'+'successfully generated!')

# imgname = lists[3]+'.jpg'
# filepath = 'D:\pycharm_project\\tensorflow\VOCdevkit\VOC2007\Annotations\\'+lists[3]+'.xml'
# write_xml(imgname,filepath)