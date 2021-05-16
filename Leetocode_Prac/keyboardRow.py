def findWords(words):
    first = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    second = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    third = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

    lines = [first, second, third]

    result = []

    for word in words:

        add = True

        for row in lines:
            if word[0].lower() in row:
                result_row = row
                break
        for char in word:

            if char.lower() not in result_row:
                add = False
                break

        if add == True:
            result.append(word)

    return result


print(findWords(["Hello","Alaska","Dad","Peace"]))
