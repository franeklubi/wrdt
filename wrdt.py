#!/bin/env python3
import random
from typing import List
from difflib import SequenceMatcher as SM
import argparse
import os.path

from Word import *

points_max: int = 3


# add and parse args
parser = argparse.ArgumentParser()
parser.add_argument(
    "path", help="the file with words you want to learn"
)
parser.add_argument(
    "-p", "--points-max", help="max points per word, default=3",
    type=int, metavar='N', default=3
)
parser.add_argument(
    "-l", "--lean", help="you won't have to be /that/ accurate",
    action="store_true"
)
parser.add_argument(
    "-i", "--ignore-case", help="case insensitive checking",
    action="store_true"
)
args = parser.parse_args()


def validateFile(path: str) -> bool:
    """
    Args:
        path (str):     path to check

    Returns:
        bool:           True if the path exists, False otherwise
    """

    if ( not os.path.exists(path) ):
        return False
    return True


def loadData(path: str) -> List[Word]:
    """
    Args:
        path (str):     path to the words file

    Returns:
        List[Word]:     var of type Word with words from file and score 0
    """

    words: List[Word] = []

    with open(path) as f:
        for line in f:
            word_list = [word.strip() for word in str(line).split('-')]
            if ( ':' in line or '#' in line or line.strip() == '' ):
                continue
            elif ( len(word_list) < 2 ):
                print('line \'%s\' not imported' % str(line).strip())
            else:
                words.append(Word(word_list))

    return words


def ask(word: Word, to_guess: int) -> str:
    """
    Args:
        word (Word):    Word class containing all the word's data
        to_guess (int): which word to replace with '?' and return as an answer

    Returns:
        str:            the word user has to guess to earn a point
    """

    # copying list with words
    copy = list(word.list)

    # extracting an answer
    answer = copy[to_guess]

    # replacing to_guess word
    copy[to_guess] = "?"

    # creating a str from a list;           removing the last dash \/
    print( ''.join([copy[x] + " - " for x in range(len(copy))])[:-3] )

    return answer


def isCorrect(correct: str, answer: str) -> bool:
    """
    Args:
        correct (str):  the correct word to check against
        answer (str):   the user's answer

    Returns:
        bool:           True if the answer is correct, false otherwise
    """

    if ( args.lean ):
        # if the word similarity is over 70%, cut it a lil slack mate
        return SM(None, correct, answer).ratio() > 0.70
    else:
        # oh god i'm so strict boo hoo
        return correct == answer


def main(path: str):
    """
    Args:
        path (str):     path to the words file
    """

    # loading word data
    words = loadData(path)

    # main guessing loop
    while len(words) != 0:
        # chosen is the index of
        chosen = random.randint(0, len(words)-1)

        # determining which word are we going to be asked for
        to_guess = random.randint(0, len(words[chosen].list)-1)

        # prompting user with the word to input
        correct = ask(words[chosen], to_guess)
        answer = input('>')

        # if the -i flag is set, convert all the strings to lowercase
        if ( args.ignore_case ):
            answer = answer.lower()
            correct = correct.lower()

        if ( isCorrect(correct, answer) ):
            print('good!\n')

            # adding point
            words[chosen].score += 1

            if words[chosen].score == points_max:
                words.pop(chosen)
        else:
            print('correct:', correct, '\n')

    print('you\'re all done! :D\n', 'now fuck off')


if __name__ == '__main__':
    if ( args.points_max < 1 ):
        points_max = 1
    else:
        points_max = args.points_max

    if ( validateFile(args.path) ):
        main(args.path)
    else:
        parser.error('wrong path >:(')
