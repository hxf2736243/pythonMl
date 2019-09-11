from pyhanlp import *

sentence = "我爱自然语言处理技术！"
s_hanlp = HanLP.segment(sentence)

for term in s_hanlp:
    print(term.word, term.nature)

s_dep = HanLP.parseDependency(sentence)
print(s_dep)



