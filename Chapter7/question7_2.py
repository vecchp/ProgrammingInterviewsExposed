def perms_slow(s, cur=None, lst=[]):
    if not s:
        lst.append(''.join(cur))
    for i, c in enumerate(s):
        if not cur:
            cur = []
        perms_slow(s[:i] + s[i + 1:], cur + [c], lst)

    return lst


def perms_fast(s, cur=None, checker=None):
    if not cur:
        cur = []

    if not checker:
        checker = [False] * len(s)

    if len(cur) == len(s):
        print(''.join(cur))
        return

    for i, c in enumerate(s):
        if checker[i]:
            continue
        checker[i] = True
        perms_fast(s, cur + [c], checker)
        checker[i] = False

#from itertools import permutations
#perms = [''.join(p) for p in permutations('hatbatfatmatchatc')]
#print(perms)


def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

#print(combs_fast('hatbatfatmatchatc'))


print(permutations('hatbatfatmatchatc'))
