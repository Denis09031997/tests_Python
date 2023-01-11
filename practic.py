def func_test():
    assert without([2, 1, 2, 3, 4], 2, 3) == [1, 4]


def func_test2():
    assert without([], 2) == []


def func_test3([2, 1, 2, 3, 4], 2, 3):
    original = [2, 1, 2, 3, 4]
    assert without(original, 2, 3) is not original