from __future__ import annotations
import cmudict
from pathlib import Path
from nltk.corpus import words as nltk_words

BASE_DICT = set()

class Bee:
    bid: str
    centre: str
    surround: str
    letters: set[str]

    usable_words: set

    def __init__(self: Bee, bid: str, centre: str, surround: str) -> None:
        self.bid = bid
        self.centre, self.surround = centre, surround
        self.letters = {self.centre}.union(set(self.surround))

        self.usable_words = set()

    def is_usable_word(self: Bee, s: str) -> bool:
        return (self.centre in s) and (all(c in self.letters for c in s))
    
    def get_usable_words(self: Bee) -> set[str]:
        if not self.usable_words:
            self.usable_words = set(filter(lambda w: self.is_usable_word(w), BASE_DICT))
        return self.usable_words

    def is_pangram(self: Bee, s: str) -> bool:
        return set(s) == self.letters

    def get_pangrams(self: Bee) -> set[str]:
        return set(filter(lambda w: self.is_pangram(w), self.get_usable_words()))

    @staticmethod
    def from_path(path: Path) -> Bee:
        with open(path, 'r') as f:
            c, s = f.read().strip().upper().split('::')
            return Bee(path.stem, c, s)
        
    def __repr__(self: Bee) -> str:
        return f'{self.centre}::{self.surround}'

def get_paths() -> None:
    return sorted(Path('./data/').glob('*.txt'), reverse=True)

def get_latest_path() -> None:
    return get_paths()[0]

def load_base_dictionary() -> None:
    global BASE_DICT
    BASE_DICT |= set(s.upper() for s in cmudict.words())
    BASE_DICT |= set(str(s).upper() for s in nltk_words.words())

def print_all_pangrams() -> None:
    for path in get_paths():
        b = Bee.from_path(path)
        print(f'{b.bid} : ', end='')
        print(' ; '.join(b.get_pangrams()))

def print_all_stats() -> None:
    for path in get_paths():
        b = Bee.from_path(path)
        print(f'{b.bid} : ', end='')
        print(f'{len(b.get_usable_words()):>4} words ; pangram(s): ', end='')
        print(' ; '.join(b.get_pangrams()))

if __name__ == '__main__':
    load_base_dictionary()
    print_all_stats()
