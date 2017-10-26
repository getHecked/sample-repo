file = open("windows.txt", 'r',encoding='utf-8').read()

words={
}

list=file.replace(".", "").replace("'", "").replace("?", "").replace(":", "").replace("\"", "").replace("\n", " ").replace(",", "").split(" ")

for element in list:
    if element in words.keys():
        words[element]+= 1
    else:
        words[element]=1

words
