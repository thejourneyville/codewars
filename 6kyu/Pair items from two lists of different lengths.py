def pair_items(list1, list2):

    if any([len(list1) == 0, len(list2) == 0]):
        return [[]]
    elif len(list1) == len(list2):
        return [list(zip(list1, list2))]
    else:
        identify = len(list1) < len(list2)
        big_list = [list1, list2][identify]
        if identify:
            small_list = list1
        else:
            small_list = list2

    combos = []
    mover = 0
    ele1, ele2 = None, None
    for ele1 in range(1):
        for ele2 in range(len(big_list)):
            if ele1 != ele2:
                if ele1 + mover < len(big_list):
                    if (big_list[ele2], big_list[ele1 + mover]) not in combos:
                        combos.append((big_list[ele1 + mover], big_list[ele2]))
        mover += 1
    combos.append((big_list[ele1 + mover], big_list[ele2]))


    flat_seq = []
    for tup in combos:
        flat_seq.append(tup[0])
        flat_seq.append(tup[1])

    flat_seq_length = len(flat_seq)
    small_list_length = len(small_list)
    print(flat_seq)

    outer, inner = [], []
    idx = 0
    while idx < flat_seq_length:
        if len(list1) > len(list2):
            inner.append((flat_seq[idx], small_list[idx % small_list_length]))
        else:
            inner.append((small_list[idx % small_list_length], flat_seq[idx]))
        idx += 1
        if len(inner) == small_list_length:
            if inner not in outer:
                outer.append(inner)
            inner = []

    return outer






# [[(63, 48), (71, 10), (63, 46), (81, 92)], [(63, 48), (95, 10), (63, 46), (79, 92)]]

# [[(63, 48), (71, 10), (81, 46), (95, 92)], [(63, 48), (71, 10), (81, 46), (79, 92)],
# [(63, 48), (71, 10), (95, 46), (79, 92)], [(63, 48), (81, 10), (95, 46), (79, 92)],
# [(71, 48), (81, 10), (95, 46), (79, 92)]]



#[[('a', 'x'), ('b', 'y')], [('a', 'x'), ('c', 'y')], [('b', 'x'), ('c', 'y')]])
print(pair_items([63, 71, 81, 95, 79],[48, 10, 46, 92]))