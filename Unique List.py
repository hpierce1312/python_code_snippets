lst = [['apple','orange','banana'],['peach','mango','apple'],['banana','pear','lemon','apple']]

def listunique(lst):
    uniquelst = []
    lst1 = []
    duplist = []

    for i in lst:
        for n in i:
            lst1.append(n)

    for i in lst1:
        count = lst1.count(i)
        if count > 1:
            duplist.append(i)
        else:
            uniquelst.append(i)

    print(uniquelst)

listunique(lst)