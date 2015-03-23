# -*- coding: utf-8 -*-

import os
import scws
import csv
import re
from svmutil import *

SCWS_ENCODING = 'utf-8'
SCWS_RULES = '/usr/local/scws/etc/rules.utf8.ini'
CHS_DICT_PATH = '/usr/local/scws/etc/dict.utf8.xdb'
CHT_DICT_PATH = '/usr/local/scws/etc/dict_cht.utf8.xdb'
IGNORE_PUNCTUATION = 1

ABSOLUTE_DICT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './dict'))
CUSTOM_DICT_PATH = os.path.join(ABSOLUTE_DICT_PATH, 'userdic.txt')
EXTRA_STOPWORD_PATH = os.path.join(ABSOLUTE_DICT_PATH, 'stopword.txt')
EXTRA_EMOTIONWORD_PATH = os.path.join(ABSOLUTE_DICT_PATH, 'emotionlist.txt')
EXTRA_ONE_WORD_WHITE_LIST_PATH = os.path.join(ABSOLUTE_DICT_PATH, 'one_word_white_list.txt')
EXTRA_BLACK_LIST_PATH = os.path.join(ABSOLUTE_DICT_PATH, 'black.txt')

cx_dict = ['a','n','nr','ns','nt','nz','v','@']#关键词词性词典

def load_scws():
    s = scws.Scws()
    s.set_charset(SCWS_ENCODING)

    s.set_dict(CHS_DICT_PATH, scws.XDICT_MEM)
    s.add_dict(CHT_DICT_PATH, scws.XDICT_MEM)
    s.add_dict(CUSTOM_DICT_PATH, scws.XDICT_TXT)

    # 把停用词全部拆成单字，再过滤掉单字，以达到去除停用词的目的
    s.add_dict(EXTRA_STOPWORD_PATH, scws.XDICT_TXT)
    # 即基于表情表对表情进行分词，必要的时候在返回结果处或后剔除
    s.add_dict(EXTRA_EMOTIONWORD_PATH, scws.XDICT_TXT)

    s.set_rules(SCWS_RULES)
    s.set_ignore(IGNORE_PUNCTUATION)
    return s

def test(weibo,weibo_dict,flag):
    word_dict = dict()
    reader = csv.reader(file('./libsvm-3.17/python/svm/feature1012.csv', 'rb'))
    for w,c in reader:
        word_dict[str(c)] = w 

    sw = load_scws()
    items = []
    for i in range(0,len(weibo)):
        words = sw.participle(weibo_dict[weibo[i]])
        row = dict()
        for word in words:
            if row.has_key(str(word[0])):
                row[str(word[0])] = row[str(word[0])] + 1
            else:
                row[str(word[0])] = 1
        items.append(row)


    f_items = []
    for i in range(0,len(items)):
        row = items[i]
        f_row = ''
        f_row = f_row + str(flag[i])
        for k,v in word_dict.iteritems():
            if row.has_key(k):
                item = str(word_dict[k])+':'+str(row[k])
                f_row = f_row + ' ' + str(item) 
        f_items.append(f_row)

    with open('./libsvm-3.17/python/svm_test/test1012.txt', 'wb') as f:
        writer = csv.writer(f)
        for i in range(0,len(f_items)):
            row = []
            row.append(f_items[i])
            writer.writerow((row))
    f.close()
    
def choose_ad():#分类
    y, x = svm_read_problem('./libsvm-3.17/python/svm/train1012.txt')
    m = svm_train(y, x, '-c 4 -t 0')

    y, x = svm_read_problem('./libsvm-3.17/python/svm_test/test1012.txt')
    p_label, p_acc, p_val  = svm_predict(y, x, m)

    return p_label

def crosscheck(n):#交叉检验
    y, x = svm_read_problem('./libsvm-3.17/python/svm/train1012.txt')
    svm_train(y, x, '-c 4 -v %s -t 0' %n)

def load_one_words():
    one_words = [line.strip('\r\n') for line in file(EXTRA_ONE_WORD_WHITE_LIST_PATH)]
    return one_words

def load_black_words():
    one_words = [line.strip('\r\n') for line in file(EXTRA_BLACK_LIST_PATH)]
    return one_words

single_word_whitelist = set(load_one_words())
single_word_whitelist |= set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

def main():#生成训练集

    sw = load_scws()
    black = load_black_words()
    reader = csv.reader(file('./libsvm-3.17/python/test/20141012_new.csv', 'rb'))
    f_dict = dict()#频数字典
    total = 0#词的总数
    content = []
    lable = []
    for mid,t,c,l in reader:
        text = t + '***' + c
        words = sw.participle(text)
        for word in words:
            if (word[1] in cx_dict) and (3 < len(word[0]) < 30 or word[0] in single_word_whitelist) and (word[0] not in black):#选择分词结果的名词、动词、形容词，并去掉单个词
                total = total + 1
                if f_dict.has_key(str(word[0])):
                    f_dict[str(word[0])] = f_dict[str(word[0])] + 1
                else:
                    f_dict[str(word[0])] = 1
        content.append(text)
        lable.append(l)

    with open('./libsvm-3.17/python/svm/feature1012.csv', 'wb') as f:
        writer = csv.writer(f)
        n = 0
        words = dict()
        for k,v in f_dict.iteritems():#计算单个词的信息量
            if v >= 2 and (float(v)/float(total)) <= 0.8:
                n = n + 1
                words[str(n)] = k
                writer.writerow((n,k))
    f.close()
    
    with open('./libsvm-3.17/python/svm/train1012.txt', 'wb') as f:
        writer = csv.writer(f)
        for i in range(0,len(content)):
            item = []
            row = str(lable[i])
            text = content[i]
            for k,v in words.iteritems():
                if v in text:
                    row = row + ' ' + str(k) + ':' + str(text.count(v))
            item.append(row)
            writer.writerow((item))
    f.close()

def mid_main(data):#是否有情感倾向分类主函数 输入数据：[[题目,内容],[题目,内容]...]

    weibo = []
    weibo_dict = dict()
    flag = []
    for i in range(0,len(data)):
        text = data[i][0] + '***' + data[i][1]
        weibo.append(str(i))
        weibo_dict[str(i)] = text
        flag.append(1)

    test(weibo,weibo_dict,flag)
    lable = choose_ad()#分类

    new_lable = []
    for i in range(0,len(lable)):
        new_lable.append(int(lable[i]))
    
    return new_lable   

def main():#测试用主函数

    reader = csv.reader(file('./libsvm-3.17/python/test/test1012.csv', 'rb'))
    data = []
    for mid,t,c,l in reader:
        row = [t,c]
        data.append(row)

    lable = test_main(data)
    print lable

if __name__ == '__main__':
    main()#生成训练集
            
