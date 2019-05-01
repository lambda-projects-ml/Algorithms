#!/usr/bin/python

import argparse


# def find_max_profit(prices):
#     result = 0
#     index = 0
#     for x in prices:
#         for y in range(index, len(prices)):
#             print(x, prices[y])
#             if x < prices[y]:
#                 if prices[y]-x > result:
#                     result = prices[y]-x
#         index += 1
#     return result

def find_max_profit(prices):
    cur_min = prices[0]
    result = 0
    for x in prices:
        print(x)
        if x < cur_min:
            cur_min = x
            print(x, cur_min)
            print(x-cur_min)

    return result


# print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))
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
