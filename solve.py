from __future__ import annotations
import cmudict
import itertools
from pathlib import Path

class Bee:
    centre: str
    surround: str

    def __init__(self: Bee, centre: str, surround: str) -> None:
        self.centre, self.surround = centre, surround

    def letters(self: Bee) -> str:
        return self.centre, self.surround

    def longest(self: Bee) -> str:
        pass

    @staticmethod
    def from_path(path: Path) -> Bee:
        with open(path, 'r') as f:
            c, s = f.read().strip().upper().split('::')
            return Bee(c, s)
        
    def __repr__(self: Bee) -> str:
        return f'{self.centre}::{self.surround}'

def get_paths() -> None:
    return sorted(Path('./data/').glob('*.txt'))

def get_latest_path() -> None:
    return get_paths()[-1]

if __name__ == '__main__':
    b = Bee.from_path(get_latest_path())
    print(b.longest())
