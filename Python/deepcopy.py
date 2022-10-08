def deepcopy_exactly_2(lst):
    deepcopy_list = []
    for inner_list in lst:
        copied_inner_list = inner_list[:]
        deepcopy_list.append(copied_inner_list)
    return deepcopy_list