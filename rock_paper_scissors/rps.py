#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']   # Total number of possible plays in the game of rock, paper, scissors.
  result = []   # Empty list that will contain total number of permutations possible based on n number of games played.
  if n == 0:    # If 0 games are played, return the results array (Which will be empty at this point)  <---This will be the base case
    return [result]
  def rps_recurse(p, res):  # Recursive function which will take the total number of plays, or rounds played and a res array as arguments.
    if p == 0: # If total number of plays has recursed down to zero, then append the current res array to the results list.
      result.append(res)
    else:  # Otherwise, loop over the plays list running the rps_recurse function on each iteration of the loop.
      for i in plays:
        rps_recurse(p - 1, res + [i]) # Run the recursive function reducing the number of plays by 1 and appending value of [i] to res array.
  rps_recurse(n, [])   # This is what kicks off the recursion in the main function
  return result





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')