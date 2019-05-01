#!/usr/bin/python

import argparse


def find_max_profit(prices):
    result = []
    index = 0
    for x in prices:
        for y in range(index, len(prices)):
            if x == prices[y]:
                continue
            else:
                result.append(prices[y]-x)
        index += 1

    maxProfits = max(result)
    return maxProfits


# print(find_max_profit([10, 7, 5, 8, 11, 9]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))

if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
