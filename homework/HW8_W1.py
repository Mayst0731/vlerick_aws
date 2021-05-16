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

    n = eval(input("Output analysis how many words?"))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq,reverse=True)
    for i in range(n):
        word,count = items[i]
        print(word,":",count)
    f.close()


main()
