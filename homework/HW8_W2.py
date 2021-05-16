def byFreq(pair):
    return pair[1]

def main():
    f = open("./dracula.txt",'r')
    lines = f.read()
    text = lines.lower()


    for ch in "#$%&()*+,-./:;<=>?@[\\]^_'{|}~":
        text = text.replace(ch,' ')
    words = text.split()

    counts = {}
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

# THE TOP 50 WORDS ARE SET TO BE STOP WORDS
    n = 50
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq,reverse=True)
    for i in range(n):
        word,count = items[i]
        w = open("./stopWords.txt", 'a')
        w.write(word+'\n')

    stop_text = open('./stopWords.txt','r').read()
    stop_words = stop_text.split()
    print(stop_words)

    m = eval(input("Output analysis how many words?"))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)

    i= 0
    while i < m:
        word, count = items[i]
        if word not in stop_words:
            print(i,'.',word, ":", count)
            i += 1
        else:
            m += 1
            i += 1

    f.close()
    w.close()



main()
