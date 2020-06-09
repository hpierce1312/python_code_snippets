import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-lst", "--list", nargs="+")
    args = parser.parse_args()
    lst = [float(item) for item in args.list]
    def Avg(lst):
        return sum(lst) / len(lst)
    print('Average = ', Avg(lst))

except:
    print("User input is incorrect type. Please input -lst followed by numeric values")