


def merge_all(list_sets):
    dic = {}

    i = 0
    while i < len(list_sets):
        v = list_sets[i]
        for k in v:
            if k not in dic:
                dic[k] = i
            else:
                tmp = v.union(list_sets[dic[k]])
                list_sets.remove(v)
                list_sets.remove(list_sets[dic[k]])
                list_sets.append(tmp)
                merge_all(list_sets)
                break

        i += 1

    return list_sets


print merge_all([set([1,2]), set([3,4]), set([2,3]), set([5,6,7])])