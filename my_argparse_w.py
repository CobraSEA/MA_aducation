import argparse

def last_i(list):
    return list[-1]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, # default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--last', dest='get_last', action='store_const',
                    const=last_i, # default=max,
                    help='last item (default: find the max)')
parser.add_argument('--cnt', dest='count', action='count',
                    help='no (default: find the max)')


args = parser.parse_args()
print(args)
if args.accumulate is not None:
    print(args.accumulate(args.integers))
if args.get_last is not None:
    print(args.get_last(args.integers))
if args.count is not None:
    print(args.count(args.integers))
#else:
#    print(max(args.integers))
# print(args.integers)