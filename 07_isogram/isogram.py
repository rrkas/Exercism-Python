def is_isogram(string):
    for i in range(len(string)):
        if (string[i]).lower().isalpha() and string[i].lower() in string[i+1:].lower():
            return False
    return True