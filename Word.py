from typing import List

class Word:
    list: List[str] = []
    score: int = 0

    def __init__(self, passed_word_list: List[str]):
        self.list = passed_word_list
