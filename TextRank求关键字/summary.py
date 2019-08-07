import jieba
# from bm25 import BM25
from textrank import TextRank
import utils
from snownlp import seg
from sys import argv

fact =argv[1]
# fact = '公诉机关指控：2016年3月28日20时许，被告人颜某在本市洪山区马湖新村足球场马路边捡拾到被害人谢某的VIVOX5手机一部，' \
#       '并在同年3月28日2、1时起，分多次通过支付宝小额免密支付功能，秘密盗走被害人谢某支付宝内人民币3723元。案发后，被告人颜某家属已赔偿被害人全部损失，' \
#       '并取得谅解。公诉机关认为被告人颜某具有退赃、取得谅解、自愿认罪等处罚情节，建议判处被告人颜某一年以下××、××或者××，并处罚金。'
if __name__ == '__main__':
    
    sents = utils.get_sentences(fact)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        # words = list(jieba.cut(sent))
        words = utils.filter_stop(words)
        doc.append(words)
    # print(doc)
    # s = BM25(doc)
    # print(s.f)
    # print(s.df)
    # print(s.idf)

    rank = TextRank(doc)
    rank.text_rank()
    for index in rank.top_index(3):
        print(sents[index])


