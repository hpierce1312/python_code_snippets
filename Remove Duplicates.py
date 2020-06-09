import argparse
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("-lst", "--list", nargs="+")
args = parser.parse_args()
lst = [str(item) for item in args.list]

def removeDups(lst):
    for i in lst:
        result = "".join(OrderedDict.fromkeys(i))
        print(result, end=" ")
removeDups(lst)