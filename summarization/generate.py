"""
            分段提取摘要
This file is based on https://github.com/letiantian/TextRank4ZH/tree/master/example/example01.py.
We adjust some parameter to make it work better.
"""

#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence


def summarization_generate(texts):
    tr4w = TextRank4Keyword()
    summarization = ""

    for text in texts:
        if len(text) < 2:
            continue
        tr4w.analyze(text=text, lower=True, window=10)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

        summarization += '\n关键词：\n'
        for item in tr4w.get_keywords(10, word_min_len=2):
            summarization += item.word + '、'
        summarization = summarization[:-1] 

        if len(tr4w.get_keyphrases(keywords_num=30, min_occur_num=2)) != 0:
            summarization += '\n关键短语：\n'

            for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
                summarization += phrase + '、'

            summarization = summarization[:-1]

        summarization += '\n摘要：\n'
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source = 'all_filters')

        for item in tr4s.get_key_sentences(num=2):
            summarization += item.sentence + '\n'

    with open('./result.txt','w',encoding='utf-8') as result:
        result.write(summarization)

if __name__ == "__main__":
    path = sys.argv[-1]
    try:
        texts = codecs.open(path, 'r', 'utf-8').read().split('\n')
        summarization_generate(texts)
    except:
        print('cannot find filepath: ' + path)
