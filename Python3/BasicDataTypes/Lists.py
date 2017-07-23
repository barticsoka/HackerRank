n = int('12')
inp = ['insert 0 5',
       'insert 1 10',
       'insert 0 6',
       'print',
       'remove 6',
       'append 9',
       'append 1',
       'sort',
       'print',
       'pop',
       'reverse',
       'print']


def ex(n, inp):
    l = []
    for i in inp:
        s = list(i.split())
        if hasattr(l, s[0]):
            getattr(l, s[0])(*map(int, s[1:]))
        else:
            print(l)


ex(n, inp)
