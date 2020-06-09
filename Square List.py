import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-lst", "--list", nargs="+", type=int, action="append")
args = parser.parse_args()

lst = [i for i in args.list]

def square(lst):
    newLst = []
    for innerLst in lst:
        squares = []
        for item in innerLst:
            squares.append(item ** 2)
        newLst.append(squares)
    return newLst

print(square(lst))