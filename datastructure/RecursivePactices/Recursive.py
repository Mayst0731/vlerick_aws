# def fun_add(n):
#     if len(str(n)) == 1:
#         return n
#     else:
#         return n % 10 + fun_add(n // 10)
#
#
# print(fun_add(1234567))


def word_split(phrase, list_of_words, output=None):
    '''
    Note: This is a very "python-y" solution.
    '''

    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):], list_of_words, output)

    # Finally return output if no phrase.startswith(word) returns True
    return output


print(word_split('themanran',['clown','ran','man']))
print(word_split('manran',['clown','ran','man']))
print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))