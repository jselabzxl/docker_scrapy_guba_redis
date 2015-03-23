# -*- coding: utf-8 -*- 

import os
import scws
import csv
import re
import random
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

def load_one_words():
    one_words = [line.strip('\r\n') for line in file(EXTRA_ONE_WORD_WHITE_LIST_PATH)]
    return one_words

def load_black_words():
    one_words = [line.strip('\r\n') for line in file(EXTRA_BLACK_LIST_PATH)]
    return one_words

single_word_whitelist = set(load_one_words())
single_word_whitelist |= set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

def naivebayes_main(data):#分类主函数 输入数据：[[题目，内容],[题目，内容]...]

    reader = csv.reader(file('./data1025.csv','rb'))
    train_data = []
    train_lable = []
    for mid, t, c, l in reader:
        train_data.append([t,c])
        train_lable.append(l)
    f_p,f_n,f_w = freq_main(train_data,train_lable)
    result_lable = naivebayes_sentiment_dict_weight(f_n,f_p,f_w,data)
    return result_lable

def check_test():

    result = []
    result_nodict = []
    #for i in range(0,10):#交叉检验的循环
    reader = csv.reader(file('./cross_validation_test/data1025.csv', 'rb'))
    data = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[]}
    #data_lable = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[]}
    number = 0
    for mid,t,c,l in reader:
        if str(l) == '1':
            number = number + 1
        flag = random.randint(1, 8)
        if flag == 1:
            item = data['1']
            item.append([t,c,l])
            data['1'] = item
        elif flag == 2:
            item = data['2']
            item.append([t,c,l])
            data['2'] = item
        elif flag == 3:
            item = data['3']
            item.append([t,c,l])
            data['3'] = item
        elif flag == 4:
            item = data['4']
            item.append([t,c,l])
            data['4'] = item
        elif flag == 5:
            item = data['5']
            item.append([t,c,l])
            data['5'] = item
        elif flag == 6:
            item = data['6']
            item.append([t,c,l])
            data['6'] = item
        elif flag == 7:
            item = data['7']
            item.append([t,c,l])
            data['7'] = item
        else:
            item = data['8']
            item.append([t,c,l])
            data['8'] = item

    for i in range(1,9):
        test_data = []
        train_data = []
        test_flag = []
        train_flag = []
        for k,v in data.iteritems():
            if k == str(i):
                for j in range(0,len(v)):
                    test_data.append([v[j][0],v[j][1]])
                    test_flag.append(v[j][2])
            else:
                for j in range(0,len(v)):
                    train_data.append([v[j][0],v[j][1]])
                    train_flag.append(v[j][2])

##        train(train_data,train_flag,i)
##        test(test_data,test_flag,i)
        f_p,f_n,f_w = freq_main(train_data,train_flag,i)
        result_lable_nodict = naivebayes(f_n,f_p,f_w,test_data,test_flag,i)
        result_lable = naivebayes_sentiment_dict_weight(f_n,f_p,f_w,test_data,test_flag,i)

        #交叉检验，生成混淆矩阵
##        p_n,r_n,f_n,p0_n,r0_n,f0_n = check(test_flag,result_lable_nodict)
##        p,r,f,p0,r0,f0 = check(test_flag,result_lable)
##        result_nodict.append([i,p_n,r_n,f_n,p0_n,r0_n,f0_n])
##        result.append([i,p,r,f,p0,r0,f0])
##
##    with open('./cross_validation_test/sentiment_dict/result1025.csv', 'wb') as f:#加入情感词典后的分类结果
##        writer = csv.writer(f)
##        for i in range(0,len(result)):
##            writer.writerow((result[i]))
##
##    with open('./cross_validation_test/no_sentiment_dict/result1025.csv', 'wb') as f:#不加情感词典的分类结果
##        writer = csv.writer(f)
##        for i in range(0,len(result_nodict)):
##            writer.writerow((result_nodict[i])) 

def train(data,lable,flag):#生成训练集
    with open('./cross_validation_test/train%s.txt'% flag,'wb')as f:
        writer = csv.writer(f)
        for i in range(len(data)):
            text = str(i)+'***'+ data[i][0]+'***'+data[i][1] + '***' + lable[i]
            item = []
            item.append(text)
            writer.writerow((item))
    f.close()

def test(data,lable,flag):#生成测试集
    with open('./cross_validation_test/test%s.txt'% flag,'wb')as f:
        writer = csv.writer(f)
        for i in range(len(data)):
            text = str(i)+'***'+ data[i][0]+'***'+data[i][1]+ '***' + lable[i]
            item = []
            item.append(text)
            writer.writerow((item))
    f.close()

#def freq_main(train_data,train_flag,count):#统计正、负类词频
def freq_main(train_data,train_flag):
    data_positive = []
    data_negative = []
    data_total = []

    for i in range(len(train_data)):
        if train_flag[i] == '1':
            data_positive.append(train_data[i])
            data_total.append(train_data[i])
        elif train_flag[i] =='0':
            data_negative.append(train_data[i])
            data_total.append(train_data[i])

##    freq_positive = freq_word(data_positive, 'positive',count)
##    freq_negative = freq_word(data_negative, 'negative',count)
##    freq_all = freq_word(data_total,'total',count)
    freq_positive = freq_word(data_positive, 'positive')
    freq_negative = freq_word(data_negative, 'negative')
    freq_all = freq_word(data_total,'total')
    
    return freq_positive,freq_negative,freq_all

def freq_word(data,flag):
    lable = []
    sw = load_scws()
    black = load_black_words()
    freq_word_dict = {}
    for i in range(len(data)):
        text = data[i][0] + '***' + data[i][1]
        words = sw.participle(text)
        total = 0
        for word in words:
            if (word[1] in cx_dict) and (3 < len(word[0]) < 30 or word[0] in single_word_whitelist) and (word[0] not in black):#选择分词结果的名词、动词、形容词，并去掉单个词
                try:
                    freq_word_dict[word[0]] += 1
                except KeyError:
                    freq_word_dict[word[0]] = 1

    sorted_freq_word = sorted(freq_word_dict.iteritems(), key = lambda(k, v):v, reverse = True)
    result_freq_word = [(k, v) for k,v in sorted_freq_word]

##    with open('./cross_validation_test/freq_word_train%s_%s.csv' %(count,flag),'wb')as fw:
##        writer = csv.writer(fw)
##        item = []
##        for i in range(len(result_freq_word)):
##            row = result_freq_word[i]
##            writer.writerow((row))
    return result_freq_word

def naivebayes(data_negative,data_positive,data_total,test_data,test_flag,count):
    
    negative_dict = {}
    negative = []
    negative_total = 0#negative类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_negative)):
        w = data_negative[i][0]
        c = data_negative[i][1]
        negative_dict[w] = c#negative类下某个单词出现的次数之和
        negative.append(w)
        negative_total = negative_total+int(c)
    negative_word_count = len(negative_dict)#negative类下单词总数（不算重复单词）
##    print 'the number of words in negative(include duplication):%s'%negative_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(negative_dict))
    
  
    positive_dict = {}
    positive = []
    positive_total = 0#positive类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_positive)):
        w = data_positive[i][0]
        c = data_positive[i][1]
        positive_dict[w] = c#positive类下某个单词出现的次数之和
        positive.append(w)
        positive_total = positive_total + int(c)
    positive_word_count = len(positive_dict)#positive类下单词总数
    
##    print 'the number of words in negative(include duplication):%s'%positive_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(positive_dict))

    total_word = []
    total_freq = []
    total = 0#文档中单词个数之和
    for i in range(len(data_total)):
        w = data_total[i][0]
        c = data_total[i][1]
        total_word.append(w)
        total_freq.append(c)
        total = total + int(c)
##    print 'total number of words:%s'%total

    #计算三个类的先验概率
    p_positive = float(positive_word_count)/float(total)
    p_negative = float(negative_word_count)/float(total)
    #p_neutral = float(neutral_word_count)/float(total)
##    print p_positive
##    print p_negative
    #print p_neutral

    #对测试数据分词
    lable = []#放分类后的类标签
    sw = load_scws()
    for i in range(len(test_data)):
        text = test_data[i][0] + '***' + test_data[i][1]
        words = sw.participle(text)
        prob = []
        p_p = 1#记录属于positive类的概率
        p_n = 1
        for word in words:
            if word[0] in negative_dict:
                p_w_n = (float(negative_dict[word[0]])+1)/(float(negative_total)+len(total_word))
            else:
                p_w_n = 1/(float(negative_total)+total)#计算P(w|negative)
            p_n = p_n * p_w_n

            if word[0] in positive_dict:
                p_w_p = (float(positive_dict[word[0]])+1)/(float(positive_total)+len(total_word))
##        elif word[0] in sentiment_word_positive:
##            p_w_p = ((float(positive_total)+total)/(float(negative_total)+total))/(float(positive_total)+total)#计算P(w|positive)
            else:
                p_w_p = 1/(float(positive_total)+total)
            p_p = p_p * p_w_p

        p_p = p_p * p_positive
        p_n = p_n * p_negative
        prob.append(p_n)
        prob.append(p_p)
        lable.append(prob.index(max(prob)))

##    with open('./cross_validation_test/no_sentiment_dict/classify_result1025_%s.txt'%count,'wb')as fw:
##        for i in range(len(lable)):
##            fw.write(str(lable[i])+'\r\n')
    return lable

def naivebayes_sentiment_dict(data_negative,data_positive,data_total,test_data):
    
    negative_dict = {}
    negative = []
    negative_total = 0#negative类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_negative)):
        w = data_negative[i][0]
        c = data_negative[i][1]
        negative_dict[w] = c#negative类下某个单词出现的次数之和
        negative.append(w)
        negative_total = negative_total+int(c)
    negative_word_count = len(negative_dict)#negative类下单词总数（不算重复单词）
##    print 'the number of words in negative(include duplication):%s'%negative_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(negative_dict))
    

    positive_dict = {}
    positive = []
    positive_total = 0#positive类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_positive)):
        w = data_positive[i][0]
        c = data_positive[i][1]
        positive_dict[w] = c#positive类下某个单词出现的次数之和
        positive.append(w)
        positive_total = positive_total + int(c)
    positive_word_count = len(positive_dict)#positive类下单词总数
    
##    print 'the number of words in negative(include duplication):%s'%positive_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(positive_dict))

    total_word = []
    total_freq = []
    total = 0#文档中单词个数之和
    for i in range(len(data_total)):
        w = data_total[i][0]
        c = data_total[i][1]
        total_word.append(w)
        total_freq.append(c)
        total = total + int(c)
##    print 'total number of words:%s'%total

    #读入情感词典
    sentiment_word_negative = []
    sentiment_word_positive = []
    positive_words = []
    f = open('./naivebayes/sentiment_word_negative.txt')
    for line in f :
        sentiment_word_negative.append(line.strip())
    f = open('./naivebayes/sentiment_word_positive.txt')
    for line in f:
        sentiment_word_positive.append(line.strip())
    f = open('./naivebayes/positive_words.txt')
    for line in f:
        positive_words.append(line.strip())
    

    #计算三个类的先验概率
    p_positive = float(positive_word_count)/float(total)
    p_negative = float(negative_word_count)/float(total)
    #p_neutral = float(neutral_word_count)/float(total)
##    print p_positive
##    print p_negative
    #print p_neutral

    #对测试数据分词
    lable = []#放分类后的类标签
    sw = load_scws()
    for i in range(len(test_data)):
        text = test_data[i][0] + '***' + test_data[i][1]
        words = sw.participle(text)
        prob = []
        p_p = 1#记录属于positive类的概率
        p_n = 1
        for word in words:

            #weight使得一个新的特征词分到两个类的概率相等
            if word[0] in negative_dict:
                if word[0] in positive_dict:
                    weight = (float(negative_dict[word[0]])+1)*(float(positive_total)+len(total_word))/((float(positive_dict[word[0]])+1)*(float(negative_total)+len(total_word)))
                else:
                    weight = (float(negative_dict[word[0]])+1)*(float(positive_total)+len(total_word))/(float(negative_total)+len(total_word))
            else:
                if word[0] in positive_dict:
                    weight = (float(positive_total)+len(total_word))/((float(positive_dict[word[0]])+1)*(float(negative_total)+len(total_word)))
                else:
                    weight = (float(positive_total)+len(total_word))/(float(negative_total)+len(total_word))
    
            if word[0] in negative_dict:
                if word[0] in sentiment_word_negative:
                    p_w_n = 1.2*(float(negative_dict[word[0]])+1)/(float(negative_total)+len(total_word))
                else:
                    p_w_n = (float(negative_dict[word[0]])+1)/(float(negative_total)+len(total_word))

            elif word[0] in sentiment_word_negative:
                p_w_n = 1.2/(float(negative_total)+total)
            else:
                p_w_n = 1/(float(negative_total)+total)#计算P(w|negative)
                
            p_n = p_n * p_w_n

            #如果词在情感字典里，则给词加权重
            if word[0] in positive_dict:
                if word[0] in sentiment_word_positive:
                    p_w_p = 1.2*(float(positive_dict[word[0]])+1)/(float(positive_total)+len(total_word))
                else:
                    p_w_p = (float(positive_dict[word[0]])+1)/(float(positive_total)+len(total_word))
            elif word[0] in sentiment_word_positive:
                p_w_p = (1.2*weight)/(float(positive_total)+total)#计算P(w|positive)
            else:
                count = 0 
                for i in range(len(positive_words)):
                    if positive_words[i] in words[0]:
                        count += 1
                if count == 0:
                    p_w_p = 1/(float(positive_total)+total)
                else:
                    p_w_p = (1.2*weight)/(float(positive_total)+total)            
            p_p = p_p * p_w_p

        p_p = p_p * p_positive
        p_n = p_n * p_negative
        prob.append(p_n)
        prob.append(p_p)
        lable.append(prob.index(max(prob)))

    with open('./cross_validation_test/classify_result1025_%s.txt'%count,'wb')as fw:
        for i in range(len(lable)):
            fw.write(str(lable[i])+'\r\n')
##    print 'weight for positive class is:%s'%weight
    return lable

def naivebayes_sentiment_dict_weight(data_negative,data_positive,data_total,test_data):#手动加权重
    
    negative_dict = {}
    negative = []
    negative_total = 0#negative类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_negative)):
        w = data_negative[i][0]
        c = data_negative[i][1]
        negative_dict[w] = c#negative类下某个单词出现的次数之和
        negative.append(w)
        negative_total = negative_total+int(c)
    negative_word_count = len(negative_dict)#negative类下单词总数（不算重复单词）
##    print 'the number of words in negative(include duplication):%s'%negative_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(negative_dict))
    

    positive_dict = {}
    positive = []
    positive_total = 0#positive类下单词总数（包含一个单词的多次出现）
    for i in range(len(data_positive)):
        w = data_positive[i][0]
        c = data_positive[i][1]
        positive_dict[w] = c#positive类下某个单词出现的次数之和
        positive.append(w)
        positive_total = positive_total + int(c)
    positive_word_count = len(positive_dict)#positive类下单词总数
    
##    print 'the number of words in negative(include duplication):%s'%positive_total
##    print 'the number of words in negative_dict(no duplication):%s'%(len(positive_dict))

    total_word = []
    total_freq = []
    total = 0#文档中单词个数之和
    for i in range(len(data_total)):
        w = data_total[i][0]
        c = data_total[i][1]
        total_word.append(w)
        total_freq.append(c)
        total = total + int(c)
##    print 'total number of words:%s'%total

    #读入情感词典
    sentiment_word_negative = []
    sentiment_word_positive = []
    positive_words = []
    f = open('./sentiment_word_negative.txt')#负面情感词典
    for line in f :
        sentiment_word_negative.append(line.strip())
    f = open('./sentiment_word_positive.txt')#正面情感词典
    for line in f:
        sentiment_word_positive.append(line.strip())
    f = open('./positive_words.txt')#自己添加的正面情感词
    for line in f:
        positive_words.append(line.strip())
    

    #计算三个类的先验概率
    p_positive = float(positive_word_count)/float(total)
    p_negative = float(negative_word_count)/float(total)
    #p_neutral = float(neutral_word_count)/float(total)
    print p_positive
    print p_negative
    #print p_neutral

    #对测试数据分词
    lable = []#放分类后的类标签
    sw = load_scws()
    for i in range(len(test_data)):
        text = test_data[i][0] + '***' + test_data[i][1]
        words = sw.participle(text)
        prob = []
        p_p = 1#记录属于positive类的概率
        p_n = 1
        for word in words:
    
            if word[0] in negative_dict:
                if word[0] in sentiment_word_negative:
                    p_w_n = 1.2*(float(negative_dict[word[0]])+1)/(float(negative_total)+len(total_word))
                else:
                    p_w_n = (float(negative_dict[word[0]])+1)/(float(negative_total)+len(total_word))

            elif word[0] in sentiment_word_negative:
                p_w_n = 1.2/(float(negative_total)+total)
            else:
                p_w_n = 1/(float(negative_total)+total)#计算P(w|negative)
                
            p_n = p_n * p_w_n

            #如果词在情感字典里，则给词加权重
            if word[0] in positive_dict:
                if word[0] in sentiment_word_positive:
                    p_w_p = 1.2*(float(positive_dict[word[0]])+1)/(float(positive_total)+len(total_word))
                else:
                    p_w_p = (float(positive_dict[word[0]])+1)/(float(positive_total)+len(total_word))
            elif word[0] in sentiment_word_positive:
                p_w_p = 3/(float(positive_total)+total)#计算P(w|positive)
            else:
                count = 0 
                for i in range(len(positive_words)):
                    if positive_words[i] in words[0]:
                        count += 1
                if count == 0:
                    p_w_p = 1/(float(positive_total)+total)
                else:
                    p_w_p = 3/(float(positive_total)+total)            
            p_p = p_p * p_w_p

        p_p = p_p * p_positive
        p_n = p_n * p_negative
        prob.append(p_n)
        prob.append(p_p)
        lable.append(prob.index(max(prob)))

##    with open('./cross_validation_test/sentiment_dict/classify_result1025_%s.txt'%number,'wb')as fw:
##        for i in range(len(lable)):
##            fw.write(str(lable[i])+'\r\n')
    return lable

def check(t_lable,f_lable):

    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(0,len(t_lable)):
        if (str(t_lable[i]) == '1') and (str(f_lable[i]) == '1'):
            tp = tp + 1
        if (str(t_lable[i]) == '1') and (str(f_lable[i]) == '0'):
            fn = fn + 1
        if (str(t_lable[i]) == '0') and (str(f_lable[i]) == '1'):
            fp = fp + 1
        if (str(t_lable[i]) == '0') and (str(f_lable[i]) == '0'):
            tn = tn + 1

    p = float(tp)/float(tp+fp)
    r = float(tp)/float(tp+fn)
    f = float(2*p*r)/float(p+r)

    p0 = float(tn)/float(tn+fn)
    r0 = float(tn)/float(tn+fp)
    f0 = float(2*p0*r0)/float(p0+r0)

    print i,tp,fp,tn,fn
    print t_lable,f_lable
    return p,r,f,p0,r0,f0

##if __name__ == '__main__':
##    check_test()
