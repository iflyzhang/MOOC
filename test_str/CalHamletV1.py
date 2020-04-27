
def getText():
    txt = open(r"test_data\\Hamlet.txt","r").read()
    txt = txt.lower()
    # print(type(txt))
    for ch in r'I"#$%&()*+,-./:;<=>?@[\\]^_ ,"{I}~':
        '''去除其中的特殊字符'''
        txt = txt.replace(ch," ")
    return txt

hmTxt = getText()
words = hmTxt.split() # 转为列表
print(type(words))
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items()) # 取出所有键值对，并转为列表
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
