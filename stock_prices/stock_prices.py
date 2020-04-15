#!/usr/bin/python
#[100, 90, 80, 50, 20, 10]
import argparse
def find_max_profit(prices):
  profit = []
  for i in range(0, len(prices)):
    for x in range(i + 1, len(prices)):
      profit.append(prices[x] - prices[i])
      x += 1
  return max(profit)


    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))