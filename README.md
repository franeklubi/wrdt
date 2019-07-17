# wrdt - A simple word teacher

wrdt is a python CLI tool designed for fast and *enjoyable* (yeah, right) word learning.

I made it just because I needed it and was too lazy to look for an already made one.

## Installation

It's a script dude, just clone the repo and run it with:

```sh
python3 wrdt.py example.txt
```
Usage:
```
wrdt.py [-h] [-p N] [-l] [-i] path
```

## Args

- flag `-i` 'ignore-case' ignores case when checking the input
- flag  `-l` 'lean' ignores like everything, You'd have to be like at least 70% correct to score a point, heresy
- param `-p` lets You set the amount of points (per word) You want to score before it gets removed from the current session, **and from Your computer, and from the dictionary, hopefully**

## Words file

See the `example.txt` for a quick tutorial on how to make a compatible file yourself!
