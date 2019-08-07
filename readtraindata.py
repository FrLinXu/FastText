# _*_coding:utf-8 _*_
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fastText as ff
import json
import thulac
import jieba
import re
def gettime(time):
    # 将刑期用分类模型来做
    v = int(time['imprisonment'])

    if time['death_penalty']:
        return -2
    elif time['life_imprisonment']:
        return -1
    else:
        return v


def getlabel(d, kind):
    global law
    global accu

    # print(d)
    if kind == 'punish_of_money':
        return d['meta']['punish_of_money']
    if kind == 'relevant_articles':
        return d['meta']['relevant_articles']
    if kind == 'criminals':
        return d ['meta']['criminals']
    if kind == 'law':
        return d['meta']['relevant_articles']
    if kind == 'accu':
        accu = []
        accus = d['meta']['accusation']

        for t in accus:
            t = t.replace("[", "").replace("]", "")
            accu.append(t)
        return accu


    if kind == 'time':
        return gettime(d['meta']['term_of_imprisonment'])


def read_trainData(path):
    fin = open(path, 'r', encoding='utf8')

    alltext = []
    criminals = []
    accu_label = []
    law_label = []
    time_label = []
    punish_of_money = []
    relevant_articles=[]
    line = fin.readline()
    while line:
        d = json.loads(line)
        alltext.append(d['fact'])
        criminals.append(getlabel(d,'criminals'))
        relevant_articles.append(getlabel(d ,'relevant_articles'))
        punish_of_money.append(getlabel(d,'punish_of_money'))
        accu_label.append(getlabel(d, 'accu'))
        law_label.append(getlabel(d, 'law'))
        time_label.append(getlabel(d, 'time'))
        line = fin.readline()
    fin.close()

    return alltext, accu_label, law_label, time_label,criminals,relevant_articles,punish_of_money

def cut_text(alltext, stop_words):
    # count = 0
    # cut = thulac.thulac(seg_only=True)
    # train_text = []
    # for text in alltext:
    #     count += 1
    #     if count % 10 == 0:
    #        print(count)
    #        return train_text
    #     cut_list = cut.cut(text, text=True)
    #     print(count)
    #     train_text.append(cut_list)
    train_text =[]
    count=0
    for fact_str in alltext :
        # count += 1
        #         # if count % 1000 == 0:
        #         #     print(count)
        #         #     return train_text
        fact_str = re.sub(r'\r', '', fact_str)
        fact_str = re.sub(r'\t', '', fact_str)
        fact_str = re.sub(r'\n', '', fact_str)
        fact_str = re.sub(r'([0-9]{4}年)?[0-9]{1,2}月([0-9]{1,2}日)?', '', fact_str)
        fact_str = re.sub(r'[0-9]{1,2}时([0-9]{1,2}分)?许?', '', fact_str)
        fact_list=[]
        cut_list = jieba.cut(fact_str)
        for w in cut_list:
            if w in stop_words:
                continue
            elif '省' in w:
                continue
            elif '市' in w:
                continue
            elif '镇' in w:
                continue
            elif '村' in w:
                continue
            elif '路' in w:
                continue
            elif '县' in w:
                continue
            elif '区' in w:
                continue
            elif '城' in w:
                continue
            elif '府' in w:
                continue
            elif '庄' in w:
                continue
            elif '道' in w:
                continue
            elif '车' in w:
                continue
            elif '店' in w:
                continue
            elif '某' in w:
                continue
            elif '辆' in w:
                continue
            elif '房' in w:
                continue
            elif '馆' in w:
                continue
            elif '场' in w:
                continue
            elif '街' in w:
                continue
            elif '墙' in w:
                continue
            elif '牌' in w:
                continue
            elif '某' in w:
                continue
            else:
                fact_list.append(w)
        train_text.append(" ".join(fact_list))

    return train_text

def read_stop_words(stops_words_path):
    fin = open(stops_words_path, 'r', encoding='utf8')
    stop_words = []
    line = fin.readline()
    while line:
        stop_words.append(line.strip())
        line = fin.readline()
    fin.close()
    return stop_words
def cut_name (text):
    return text
def cut_place(text):

    return text

if __name__ == '__main__':

     print('reading stopwords')
     stop_words = read_stop_words("stopwords.txt")

     print('reading train data')
     alltext, accu_label, law_label, time_label,criminals ,relevant_articles,punish_of_money= read_trainData('data_train.json')
     print(accu_label)

     print('cut name...')
     train_data = cut_name (alltext)
     print('cut place...')
     train_data =cut_place(train_data)
     print('cut text...')
     train_data = cut_text(train_data,stop_words)
     print(accu_label[1])
     print('prepare train data...')
     f_acc = open("acc_train.txt", 'w',encoding="utf-8")
     f_law = open("acc_law.txt", 'w',encoding="utf-8")
     f_time = open("acc_time.txt", 'w',encoding="utf-8")

     for i,text in enumerate(train_data):
         f_acc.write( text + " __label__" + str(accu_label[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace(",","")+" \n")
         f_law.write(text + " __label__" + str(law_label[i]) + "\n")
         f_time.write( text +" __label__" + str(time_label[i])+"\n")

     f_acc.close()
     f_law.close()
     f_time.close()
     # file = open("adata.txt","w",encoding="utf-8")
     # file.write("criminals\tdeath_penalty\timprisonment\tlife_imprisonment\tpunish_of_money\taccusation\trelevant_articles\tfact\n")
     # for i,text in enumerate (alltext):
         # if (i+1) %200 ==0 :
         #     print(i)
         #     break
         #
         # if time_label[i] >= 0:
         #
         #     file.write(str(criminals[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "")+
         #                "\tfalse\t"+str(time_label[i])+"\tfalse"+"\t"+str(punish_of_money[i])+"\t"+
         #                str(accu_label[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "") +"\t"+str(relevant_articles[i]).replace("[", "").replace("]", "")+"\t"+text+"\n") #有期
         # elif time_label[i] == -1:
         #     file.write(str(criminals[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "")+
         #                "\tfalse\t"+"0"+"\ttrue"+"\t"+str(punish_of_money[i])+"\t"+
         #                str(accu_label[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "") +"\t"+str(relevant_articles[i]).replace("[", "").replace("]", "")+"\t"+text+"\n") #无期
         # elif time_label[i] == -2:
         #     file.write(str(criminals[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "")+
         #                "\tture\t"+"0"+"\tfalse"+"\t"+str(punish_of_money[i])+"\t"+
         #                str(accu_label[i]).replace("[", "").replace("]", "").replace("'", "").replace("'", "") +"\t"+str(relevant_articles[i]).replace("[", "").replace("]", "")+"\t"+text+"\n") #死
     # file.close()