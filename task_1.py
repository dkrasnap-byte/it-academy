def extract_even_nums(arr: list[int]) -> list[int]:
    if not arr:
        return []
    res = set(num for num in arr if num % 2 == 0)
    return sorted(list(res), reverse=True)


if __name__ == '__main__':
    print(extract_even_nums([1, 2, 2, 4, 15, 3, 4, 5, 6, 7, 8, 9]))
