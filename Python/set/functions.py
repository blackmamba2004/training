def array_diff(a: list, b: list) -> list:
    b = set(b)
    for i in b:
        for j in a:
            remove_all(a, i)

    return a


def remove_all(arr: list, deleted: int) -> None:
    for i in arr:
        if i == deleted:
            arr.remove(deleted)


