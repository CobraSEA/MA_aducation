"""
Lab 6.7 using argparse
"""
if __name__ == '__main__':
    print('String parcer initialized!')

    import argparse

    parser = argparse.ArgumentParser(description='some actions with args')
    # parser.add_argument('arguments', type=str, help='two strings and int arg', nargs='+')
    parser.add_argument('--l', type=str, dest='lang', help='lang variable', default='ua')
    parser.add_argument('--c', type=str, dest='word', help='keyword variable', default='word')
    parser.add_argument('--m', type=int, dest='value', help='value variable', default=0)

    args = parser.parse_args()

    if args.lang is not None:
        print(args.lang)
    if args.word is not None:
        print(args.word)
    if args.value is not None:
        print(args.value)
