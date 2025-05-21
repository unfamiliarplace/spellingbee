# Spelling Bee

A simple solver for [the NYT Spelling Bee game](https://www.nytimes.com/puzzles/spelling-bee).

Data files are entered under `data` with a single line like this:

`N::AOEBJW`

In this example, `N` is the middle letter, and `AOEBJW` are the surrounding ones (clockwise from 12 o'clock, but that has no effect at present).

## Dependencies

Requires `cmudict`.
