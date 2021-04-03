"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = '27_yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full house'
FOUR_OF_A_KIND = 'four of a kind'
LITTLE_STRAIGHT = 'little straight'
BIG_STRAIGHT = 'big straight'
CHOICE = 'choice'


def score(dice, category):
    s = 0
    if category == ONES:
        s = dice.count(1)
    elif category == TWOS:
        s = dice.count(2) * 2
    elif category == THREES:
        s = dice.count(3) * 3
    elif category == FOURS:
        s = dice.count(4) * 4
    elif category == FIVES:
        s = dice.count(5) * 5
    elif category == SIXES:
        s = dice.count(6) * 6
    elif category == FULL_HOUSE:
        un = set(dice)
        if len(list(un)) == 2:
            if dice.count(list(un)[0]) in (2,3):
                s = sum(dice)
    elif category == FOUR_OF_A_KIND:
        un = set(dice)
        for i in un:
            if dice.count(i) >= 4 :
                s = 4 * i
    elif category == LITTLE_STRAIGHT:
        dice.sort()
        if dice == [1, 2, 3, 4, 5]:
            s = 30
    elif category == BIG_STRAIGHT:
        dice.sort()
        if dice == [2, 3, 4, 5, 6]:
            s = 30
    elif category == CHOICE:
        s = sum(dice)
    elif category == YACHT:
        if len(set(dice)) == 1:
            s = 50
    return s
