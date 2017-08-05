# encoding:utf-8

import os,sys,jieba,chardet
import jieba.posseg as pseg
import tkFileDialog

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global stopword_file,userdict_file
stopword_file = u"./tool01_stopword_list.txt"
userdict_file = u"./tool01_usrdict.txt"

# 从文件中读取词语列表，存于数组中返回
# 文件中的数据格式： 每词一行 (适用该格式的有：主题词停用表、关键词黑名单等)
def LoadStopWordFromFile(file_path):
    
    if not os.path.exists(file_path): 
        print "commonFunction erro : no such file"
        return []

    # 读取文件数据
    File = open(file_path,"r")
    List = File.read()
    File.close()

    # 对文件数据进行编码检测，并转为unicode编码
    tmpList = List
    try:
        cc = chardet.detect(List)['encoding']
        try: List = unicode(List,cc)
        except Exception,e:  List = tmpList
    except Exception,e: pass
    
    # 将文件数据以回车分隔，读出存于WordList列表中
    WordList = []
    stopwordList = List.split(u"\n")
    for stopword in stopwordList:
        if stopword not in WordList:
            WordList.append(stopword)
    return WordList

def LoadDictFromFile(file_path):
    
    if not os.path.exists(file_path): 
        print "commonFunction erro : no such file"
        return []

    # 读取文件数据
    File = open(file_path,"r")
    List = File.read()
    File.close()

    # 对文件数据进行编码检测，并转为unicode编码
    tmpList = List
    try:
        cc = chardet.detect(List)['encoding']
        try: List = unicode(List,cc)
        except Exception,e:  List = tmpList
    except Exception,e: pass
    
    # 将文件数据以回车分隔，读出存于WordList列表中
    WordList = []
    dictList = List.strip().split(u"\n")
    for wordwithflag in dictList:
        word = wordwithflag.split(u' ')[0]
        if word not in WordList:
            WordList.append(word)
    return WordList

# 向词典中保存文件
def SaveWordToFile(file_path,List):
    File = open(file_path,"w")
    output = u""
    for word in List:
        output += word+u"\n"
    output=output[:-1].strip()
    File.write(output)
    
# 获取文件夹的路径，返回文件名与文件路径列表
def getDirectoryPath():
    
    fname = tkFileDialog.askdirectory(title=u"选择文件",initialdir="D:/HealthKnoWebService/训练用的健康文本_2017/example")
    file_list_result = []
    
    for root,dirs,filenames in os.walk(fname):
        if not filenames:break
        filenumber = len(filenames)
        for filename in filenames:
            filename = (os.path.join(root,filename))
            file_list_result.append(filename)
    
    show_directory = fname.split("/")[-1]
    return show_directory,file_list_result  # 返回文件全路径

# 获取目标文件的标题、内容以及分词结果
def getFileContentAndSeg(file_name):
    
    file = open(file_name,'r')
    text = file.read()
    file.close()

    seg_content = u""
    sotpword_list = []
    health_dict_list = []
    global stopword_file,userdict_file
    if os.path.exists(stopword_file):
        sotpword_list = LoadStopWordFromFile(stopword_file)
    if os.path.exists(userdict_file):
        jieba.load_userdict(userdict_file)
        health_dict_list = LoadDictFromFile(userdict_file)

    ALL_STOP = sotpword_list + health_dict_list
    ustring = u""
    seg_result = []
    try:
        codechardet = chardet.detect(text)['encoding']
        ustring = unicode(text,codechardet)
        result = pseg.cut(ustring)
        for word,flag in result:
            seg_content += word + u"  "
            if flag[0] in [u'x',u'm',u'e']:continue
            elif word in ALL_STOP:continue
            elif flag in [u'nrt',u'ns',u'nr',u'nz']:continue
            seg_result.append((word,flag))
    except Exception,e:
        seg_content = "error"
        seg_result = []

    return seg_content,seg_result

# 面对ui视图封装显示功能
def showContentAndSeg(id,\
                      openID,filename_list,\
                      st_textTitle,tc_textContent,\
                      list_segResultBow):
    openID.SetLabel(str(id))

    # 调用文本处理函数
    file_path = filename_list[id]
    content,seg_result = getFileContentAndSeg(file_path)
    
    # 显示该文本结果
    st_textTitle.SetLabel(file_path.split(u"/")[-1])
    tc_textContent.SetLabel(content)
        
    list_segResultBow.DeleteAllItems() 
    seg_result_bow = list(set(seg_result))
    for word,flag in seg_result_bow:
        index = list_segResultBow.InsertStringItem(sys.maxint,word)
        list_segResultBow.SetStringItem(index,1,flag)
        