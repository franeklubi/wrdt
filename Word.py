from typing import List

class Word:
    list: List[str] = []
    score: int = 0

    def __init__(self, passed_word_list: List[str]):
        if ( len(passed_word_list) < 2 ):
            print('not enough words bruh, more than 2, thanks')

        self.list = passed_word_list
