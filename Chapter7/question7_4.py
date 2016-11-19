digi_map = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y']
}


def phonewords(number, cur=None, lst=None):
    global digi_map
    if not number:
        lst.append(''.join(cur))
        return

    if not cur and not lst:
        cur, lst = [], []

    num_lst = digi_map[number[0]]

    for c in num_lst:
        new_cur = cur + [c]
        phonewords(number[1:], new_cur, lst)

    return lst


def increment(cur_number, max_vals):
    for i in range(0, len(cur_number)):
        cur_number[i] = (cur_number[i] + 1) % max_vals[i]
        if cur_number[i] != 0:
            return cur_number

    return cur_number


def num_2_word(cur_word, number):
    global digi_map
    return ''.join((digi_map[n][c] for c, n in zip(cur_word, number)))


def phonewords_itr(number):
    global digi_map
    cur_word = [0] * len(number)
    end_word = [len(digi_map[c]) for c in number]

    num_itrs = 1

    for num in end_word:
        num_itrs *= num

    lst = [num_2_word(cur_word, number)]

    for i in range(1, num_itrs):
        increment(cur_word, end_word)
        lst.append(num_2_word(cur_word, number))

    return lst


def word_numbers(digits):
    global digi_map
    ret = ['']
    for num in digits:
        letters = digi_map[num]
        ret = [prefix + letter for prefix in ret for letter in letters]
    return ret


rec = phonewords('18001337')
w_itr = phonewords_itr('18001337')
lstcomp = word_numbers('18001337')
print(len(rec), len(w_itr), len(lstcomp))
