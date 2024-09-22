from __future__ import annotations
import cmudict
from pathlib import Path
from nltk.corpus import words as nltk_words

class Bee:
    bid: str
    centre: str
    surround: str
    letters: set[str]

    def __init__(self: Bee, bid: str, centre: str, surround: str) -> None:
        self.bid = bid
        self.centre, self.surround = centre, surround
        self.letters = {self.centre}.union(set(self.surround))

    def is_usable_word(self: Bee, s: str) -> bool:
        return (self.centre in s) and (all(c in self.letters for c in s))
    
    def get_usable_words(self: Bee) -> set[str]:
        return set(filter(lambda w: self.is_usable_word(w), get_base_dictionaries()))

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

def get_base_dictionaries() -> set[str]:
    words = set()
    words = words.union(set(s.upper() for s in cmudict.words()))
    words = words.union(set(str(s).upper() for s in nltk_words.words()))
    return words

def print_all_pangrams() -> None:
    for path in get_paths():
        b = Bee.from_path(path)
        print(f'{b.bid} : {b.get_pangrams()}')

if __name__ == '__main__':
    print_all_pangrams()
