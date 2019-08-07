import jieba
import re
import json

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

def read_stop_words(stops_words_path):
    fin = open(stops_words_path, 'r', encoding='utf8')
    stop_words = []
    line = fin.readline()
    while line:
        stop_words.append(line.strip())
        line = fin.readline()
    fin.close()
    return stop_words
def cut_text(alltext, stop_words):
    train_text =[]
    for fact_str in alltext :
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


def read_test_data (path) :
    fin = open(path, 'r', encoding='utf8')

    alltext = []
    cri = []
    line = fin.readline()
    while line:
        d = json.loads(line)
        alltext.append(d['fact'])
        cri.append(getlabel(d, 'accu'))
        line = fin.readline()
    fin.close()
    return alltext, cri

if __name__ =='__main__' :
    alltext,cri=read_test_data('test.json')
    stop_words = read_stop_words('stopwords.txt')
    cut_test =cut_text(alltext,stop_words)
    cutfile = open('cut_data.txt','w',encoding='utf-8')
    count = 0
    for i,text in enumerate(cut_test) :
        cutfile.write(text+"\n")
        cutfile.write(str(cri[i]).replace("[","").replace("]","").replace("'","")+"\n")
    cutfile.close()

