#!/usr/bin/python

import sys


def helper(r, p, s):
    list = []
    if r == 1:
        list.append('Rock')

    if p == 1:
        list.append('Paper')

    if r == 1:
        list.append('Scissors')

        return list


def rock_paper_scissors(n):
    result = []
    if n <= 1:
        return n
    else:
        rock = rock_paper_scissors(n-1)
        print(rock)
        paper = rock_paper_scissors(n-1)
        print(paper)
        scissors = rock_paper_scissors(n-1)
        print(scissors)
        list = helper(rock, paper, scissors)

    result.append(list)
    return result


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
