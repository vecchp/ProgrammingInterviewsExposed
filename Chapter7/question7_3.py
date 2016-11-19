

def combs(s, cur=None, lst=None):
    if not cur or not lst:
        cur, lst = [], []

    for i, c in enumerate(s):
        new_cur = cur + [c]
        lst.append(''.join(new_cur))
        combs(s[i+1:], new_cur, lst)

    return lst

o = combs(['a', 'b', 'c'])
t = combs(['w', 'x', 'y', 'z'])
f = combs(['w', 'x', 'y', 'z', '1'])
print(3, o, len(o))
print(4, t, len(t))
print(5, f, len(f))