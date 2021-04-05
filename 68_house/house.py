from typing import List


map = {
    1: 'This is the house that Jack built.',
    2: 'This is the malt that lay in the house that Jack built.',
    3: 'This is the rat that ate the malt that lay in the house that Jack built.',
    4: 'This is the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    5: 'This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    6: 'This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    7: 'This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    8: 'This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    9: 'This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    10: 'This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    11: 'This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
    12: 'This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.'
}


def recite(start_verse: int, end_verse: int) -> List[str]:
    if start_verse == end_verse:
        return [map[start_verse]]
    s = []
    for i in range(start_verse, end_verse + 1):
        s.append(recite(i, i)[0])
    return s


if __name__ == '__main__':
    print(len(recite(1, 12)))