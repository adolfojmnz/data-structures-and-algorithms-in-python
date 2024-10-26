def binary_search(
    iterable: list[int] | tuple[int], target: int, low: int = 0, high: int | None = None
) -> int:
    """A recursive implementation of the binary search algorithm."""
    low = low if low is not None else 0
    high = high if high is not None else len(iterable) - 1
    mid = (low + high) // 2

    # Base condition
    if low > high:
        return -1

    if target == iterable[mid]:
        return mid

    if target > iterable[mid]:
        low = mid + 1

    if target < iterable[mid]:
        high = mid - 1

    return binary_search(iterable, target, low, high)


if __name__ == "__main__":
    iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    test_cases = (
        (1, 0),
        (2, 1),
        (4, 3),
        (6, 5),
        (8, 7),
        (9, 8),
        (-1, -1),
        (10, 9),
        (33, -1),
        (0, -1),
    )
    for n, case in enumerate(test_cases):
        passed = binary_search(iterable, case[0]) == case[1]
        print(f"TEST {n} {"PAST" if passed else "FAILED"}")
