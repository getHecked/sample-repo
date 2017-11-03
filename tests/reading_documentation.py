import re
file = open("test1.txt", 'r',encoding='utf-8').read()
words={}
slist=file.replace("\W+",'').split(" ")
for element in slist:
    if element in words:
        words[element]+= 1
    else:
        words[element]=1
words

lowest = min(words.values())
highest = max(words.values())

for word,freq in words.items():
    if freq==lowest:
        print(f"The least frequent word is '{word_lowest}' with a frequency of: {lowest}")
    if freq==highest:
        print(f"The most frequent word is '{word}' with a frequency of: {highest}")


######################################3
file = open("test1.txt", 'r',encoding='utf-8')
words = {}
words_capital = {}
for s in file:
    if (s[0].isupper()==True):
        words_capital[s] = s
    else:
        words[s] = s

for key,value in sorted(words_capital.items()):
    print(value)

for key,value in sorted(words.items()):
    print(value)
#######################################
word_list = input().split(' ')
print(sum(1 for i in word_list if i[::-1]==i ))
#######################################3
