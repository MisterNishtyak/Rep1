def stringi(s):
    for sym in set(s):
        c = 0
        for sub_sym in s:
            if sym == sub_sym:
                c += 1
        print(sym, c)
stringi('dwwqwew')