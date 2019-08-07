# _*_coding:utf-8 _*_
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import fastText as ff
import json
import thulac
import jieba
import re
from sys import argv


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



def read_trainData(path):
    fin = open(path, 'r', encoding='utf8')

    alltext = []

    accu_label = []
    law_label = []
    time_label = []

    line = fin.readline()
    while line:
        d = json.loads(line)
        alltext.append(d['fact'])

        accu_label.append(getlabel(d, 'accu'))
        law_label.append(getlabel(d, 'law'))
        time_label.append(getlabel(d, 'time'))
        line = fin.readline()
    fin.close()

    return alltext, accu_label, law_label, time_label


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
        # if count % 10 == 0:
        #     print(count)
        #     return train_text
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

def read_test (path):
    fin = open(path, 'r', encoding='utf8')
    test_data=[]
    test_lable=[]
    line = fin.readline()
    while line:
        test_data.append(line.strip())
        line = fin.readline()
        test_lable.append(line.strip())
        line =fin.readline()
    fin.close()

    return test_data, test_lable

# fact=argv[1]
if __name__ == '__main__':

     stop_words = read_stop_words('F:/FastTextpredict/stopwords.txt')
     #
     # print('train acc...')
     # classifier = ff.train_supervised(input="acc_train.txt", label="__label__" ,wordNgrams=2)
     # classifier.save_model('acc_train.model.bin')

#load训练好的模型
     classifier = ff.load_model('F:/FastTextpredict/acc_train.model.bin')
#测试模型


     #系统运行的代码
     # list =[]
     # list.append(fact)
     # list =cut_text(list,stop_words)
     # lable, pro = classifier.predict(list)
     # for i,text in enumerate(lable):
     #    print(text[9:]+"的概率为："+str(pro[i]))

     #end here

     fact = '昌宁县人民检察院指控，2014年4月19日下午16时许，被告人段某驾拖车经过鸡飞乡澡塘街子，' \
            '时逢堵车，段某将车停在“冰凉一夏”冷饮店门口，被害人王某的侄子王2某示意段某靠边未果，' \
            '后上前敲打车门让段某离开，段某遂驾车离开，但对此心生怨愤。同年4月21日22时许，被告人' \
            '段某酒后与其妻子王1某一起准备回家，走到鸡飞乡澡塘街富达通讯手机店门口时停下，段某进入' \
            '手机店内对被害人王某进行吼骂，紧接着从手机店出来拿得一个石头又冲进手机店内朝王某头部打去' \
            '，致王某右额部粉碎性骨折、右眼眶骨骨折。经鉴定，被害人王某此次损伤程度为轻伤一级。'

     fact1="南宁市江南区人民检察院指控，2014年9月12日14时许，"\
                                 "被告人冯某去到南宁市江南区白沙北三里，趁无人之机，"\
                                 "用螺丝刀撬开被害人谢某某停放在该处的一辆红旗牌电动车的电门锁，"\
                                 "随后，冯某骑该车逃离现场。在驾车行至江南区江南大道西江码头附近时"\
                                 "，冯某被公安人员抓获。被盗的电动车已被公安机关依法扣押并被返还给被害人"\
                                 "。经南宁市价格认证中心鉴定，被盗的电动车案发时价值2550元。"\
                                 "被告人冯某归案后如实供述了上述事实。"\
                                 "被告人冯某曾因犯故意伤害罪于2008年8月6日被本院判处××，2010年3月6日刑满释放。"

     fact2='经审理查明，被告人赵某在明知被害人吴某未满十四周岁的情况下，' \
           '仍多次与其发生性关系。具体有：1、2008年3月6日，被告人赵某在本市西湖' \
           '区玉古山庄403房间内与吴某发生性关系；2、2008年3月7日至8日，被告人' \
           '赵某在本市裕都宾馆房间内与吴某发生性关系；3、2008年5月，被告人赵某在' \
           '上海市崇明区一出租房内，与处于人工流产恢复期的吴某发生性关系。上述' \
           '事实，被告人赵某在开庭审理过程中亦无异议，并有书证发生情况报告表、' \
           '医院就诊及人流手术材料、住宿登记、学籍卡片、接警单及情况说明、抓获经' \
           '过、户籍证明、证人胡某、唐某、赵某的证言、被害人吴某的陈述等证据予以证实，足以认定。'

     print(fact,end="\n")
     print(fact1,end="\n")
     print(fact2,end="\n")
     list1=[]
     list1.append(fact)
     list1.append(fact1)
     list1.append(fact2)
     list1 = cut_text(list1,stop_words)
     print(list1)
     lable,pro = classifier.predict(list1)
     for i,text in enumerate(lable)  :
         print(text[9:]+"的概率为："+str(pro[i] ) )



     #
     #
     # test_data , test_lable = read_test('cut_data.txt')
     #
     # predict_lable , predict_pro =classifier.predict(test_data)
     # count = 0
     # ok =0
     # for i,text in enumerate(predict_lable):
     #     count+=1
     #     if text[9:] == test_lable[i]:
     #         ok+=1
     #     else :
     #         print(text[9:]+"<--->"+test_lable[i]+str(count))
     # print("成功的个数："+str(ok)+"\n")
     # print("失败的个数："+str(count)+"\n"+"成功率为:")
     # print(1.0*ok/count)




     # print(classifier.predict(fact,k=6))
     # print(result.precision)
     # print(result.recall)