T = ('AAAaaa', 'ab')
# T = ('Aa', 'ab', 'AaAa', 'AaAaAa', 'ABBA')
def counter(T):
    M = []
    unic = []
    d = {}
    # to lower
    for t in T:
        M.append(t.lower())
    # finding unic
    for el in "".join(M):
        if el not in unic:
            unic.append(el)
    # copy of unic
    unic_buff = []
    for el in unic:
        unic_buff.append(el)
    # looking for
    for m in M:
        am_unic = 0
        for el in m:
            if el in unic:
                am_unic += 1
                unic.remove(el)
        d[m] = am_unic
        # reset unic
        unic.clear()
        for el in unic_buff:
            unic.append(el)
    # fdfds
    maxx = 0
    results = []
    for key, value in d.items():
        if value > maxx:
            maxx = value
    for key, value in d.items():
        if value == maxx:
            results.append(len(key))
    return (max(results))
counter(T)