verses = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]

nums = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite(start_verse, end_verse):
    if start_verse != end_verse:
            return [recite(i,i)[0] for i in range(start_verse,end_verse+1)]
    l = []
    s = "On the %s day of Christmas my true love gave to me: " % nums[start_verse-1]
    for i in range(end_verse)[::-1]:
        if i != end_verse-1:
            s = s + ", "
        if end_verse>1 and i == 0:
            s = s + 'and '
        s = s + verses[i]
    s = s + '.'
    l.append(s)
    return l

for i in recite(1,3):
    print(i)