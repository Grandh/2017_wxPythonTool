# coding:utf-8

import os,jieba,chardet
import jieba.posseg as pseg

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

# ================= 组合词  ====================
# 基于文本共现图的组合词算法实现
def CompoundWord(segTextList,wordDigraph):
    
    COM_WORD_FLAG = [u'n',u'v',u'a',u'b',u'j',u'l']# 全局变量：允许组合词的词性
    stopWordList = LoadStopWordFromFile(r"./dictionary/compound_black_list.txt") # "./xx 的形式限于windows
    
    length = len(segTextList)
    counter = 0-1
    while 1:
        
        counter += 1
        if counter >= length: break
               
        word,flag = segTextList[counter]
        if flag[0] not in COM_WORD_FLAG: continue
        if word in stopWordList: continue
        ## 统计组合词出现的次数
        tmp_compoundword = [word]
        while 1:
            counter += 1
            if counter >= length: break
            
            next_word,next_flag = segTextList[counter]
            if next_flag[0] not in COM_WORD_FLAG: break
            
            tmp_compoundword.append(next_word)
            
        if len(tmp_compoundword) >= 2: # 超过两个词的组合，考虑为组合词
            com_word = (u"".join(tmp_compoundword)).strip() 
            if com_word not in wordDigraph.keys(): wordDigraph[com_word] = 1
            else: wordDigraph[com_word] += 1
            
if __name__ == "__main__":
    
    allFilePath = u"D:/HealthKnoWebService/训练用的健康文本_2017/alltext_2017.7.31" #example"
    # 加载所有文本
    compoundword_dict = {}
    count = 0
    for root,dirs,filenames in os.walk(allFilePath):
        
        filenumber = len(filenames)
        print "检索到%d篇文档" % filenumber
        
        for filename in filenames:
            
            print count,filename
            filename = (os.path.join(root,filename))
            f = open(filename,'r')
            text = f.read()
            f.close()
            if not text: continue
            
            ustring = result = ""
            try:
                codechardet = chardet.detect(text)['encoding']
                ustring = unicode(text,codechardet)
                result = pseg.cut(ustring)
            except Exception,e:
                print "error-1"
                continue
            seg_result = []
            for word,flag in result:seg_result.append((word,flag))
            # 分词后利用共现词频找到组合词 
            CompoundWord(seg_result,compoundword_dict)
            count += 1
            
    # 保存入文件，组合词+出现次数
    saveCompoundResult = open(u"./compound_result.txt",'w')
    output = u""
    for word in compoundword_dict.keys():
        num = compoundword_dict[word]
        if num <= 5:continue
        output += word + u" " + str(num) + u"\n"
    saveCompoundResult.write(output)