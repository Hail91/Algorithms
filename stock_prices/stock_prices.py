#!/usr/bin/python
#[100, 90, 80, 50, 20, 10]
import argparse
def find_max_profit(prices):
  profit = []    # Initialize an empty list
  for i in range(0, len(prices)):  # Loop over the input list
    for x in range(i + 1, len(prices)):   # Loop over the list again but starting at the next item in the list
      profit.append(prices[x] - prices[i])  # Find the difference between comparing the left item(The buy) to the right item (the sell) and append the result to profit list.
      x += 1  # Increment x and rerun the loop
  return max(profit)   # Return the max profit from the profit list


    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))