#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']   # Total number of possible plays in the game of rock, paper, scissors.
  result = []   # Empty list that will contain total number of permutations possible based on n number of games played.
  if n == 0:    # If 0 games are played, return the results array (Which will be empty at this point)  <---This will be the base case
    return [result]
  def rps_recurse(p, res):
    if p == 0:
      result.append(res)
    else:
      for i in plays:
        rps_recurse(p - 1, res + [i])
  rps_recurse(n, [])
  return result





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')