def count_words(sentence):
    sentence = sentence.lower()
    for char in """\n\t",.!&@$%^#()[]_-\\@°+=*%;?<>:""":
        sentence = sentence.replace(char, ' ')

    words = dict()
    sentence = sentence.split(" ")
    for word in sentence:
        while (len(word) > 1) and (word[0] == "'") and (word[-1] == "'"): # word is between one or more '
            word = word[1:-1]
        if word not in [" ", '']:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1

    return words