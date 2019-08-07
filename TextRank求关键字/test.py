# coding=utf-8
import jieba
import re

fact_str ='公诉机关指控：2016年3月28日20时许，被告人颜某在本市洪山区马湖新村' \
          '足球场马路边捡拾到被害人谢某的VIVOX5手机一部，并在同年3月28日21时起' \
          '，分多次通过支付宝小额免密支付功能，秘密盗走被害人谢某支付宝内人民币3723元' \
          '。案发后，被告人颜某家属已赔偿被害人全部损失，并取得谅解。' \
          '公诉机关认为被告人颜某具有退赃、取得谅解、自愿认罪等处罚情节，' \
          '建议判处被告人颜某一年以下××、××或者××，并处罚金。'
fact_str = re.sub(r'\r', '', fact_str)
fact_str = re.sub(r'\t', '', fact_str)
fact_str = re.sub(r'\n', '', fact_str)
fact_str = re.sub(r'([0-9]{4}年)?[0-9]{1,2}月([0-9]{1,2}日)?', '', fact_str)
fact_str = re.sub(r'[0-9]{1,2}时([0-9]{1,2}分)?许?', '', fact_str)
with open("stopwords.txt","r" ,encoding="UTF-8") as f:
    stopwords =f.readline()
    print(stopwords)
#stopwords =f.readline()

cut_list = jieba.cut(fact_str)
print(cut_list)
