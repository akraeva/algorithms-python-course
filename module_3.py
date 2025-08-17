# Stepick.org — Алгоритмы в Python — просто, наглядно, с нуля!
# 3. Рекурсия и оптимизация


# 3.1 Основы рекурсии, стек вызовов


def m_3_1_1():

    def count_digits(n):
        if n < 10:
            return n
        return n % 10 + count_digits(n // 10)

    # print(count_digits(1234) == 10)


def m_3_1_2():

    def reverse(s):
        if len(s) == 1:
            return s
        return s[-1] + reverse(s[: len(s) - 1])

    # print(reverse("hello") == "olleh")


def m_3_1_3():

    def count_nested_lists(lst):
        count = 0
        for i in lst:
            if isinstance(i, list):
                count += 1 + count_nested_lists(i)
        return count

    # print(count_nested_lists([1, [2, 3], [4, [5, 6]], 7]) == 3)


def m_3_1_4():

    def deep_sum(data):
        num_sum = 0
        for i in data:
            if isinstance(i, int):
                num_sum += i
            elif isinstance(i, list):
                num_sum += deep_sum(i)
        return num_sum

    # print(deep_sum([1, [2, 3], [4, [5, [6]]]]) == 21)


# 3.2 Рекурсивный обход JSON


def m_3_2_1():
    def count_strings(obj):
        if isinstance(obj, dict):
            return sum(count_strings(v) for v in obj.values())
        elif isinstance(obj, list):
            return sum(count_strings(i) for i in obj)
        elif isinstance(obj, str):
            return 1
        return 0


def m_3_2_2():
    def collect_emails(obj):
        strings = []

        if isinstance(obj, dict):
            for value in obj.values():
                strings.extend(collect_emails(value))
        elif isinstance(obj, list):
            for item in obj:
                strings.extend(collect_emails(item))
        elif isinstance(obj, str):
            if "@" in obj:
                strings.append(obj)

        return strings


def m_3_2_3():
    def find_by_key(obj, target_key):
        results = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == target_key:
                    results.append(value)
                results.extend(find_by_key(value, target_key))
        elif isinstance(obj, list):
            for item in obj:
                results.extend(find_by_key(item, target_key))

        return results


def m_3_2_4():
    def contains_key(obj, target_key):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == target_key or contains_key(value, target_key):
                    return True
        elif isinstance(obj, list):
            for item in obj:
                if contains_key(item, target_key):
                    return True
        return False


def m_3_2_5():
    def replace_value(obj, key, new_value):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    obj[k] = new_value
                else:
                    replace_value(v, key, new_value)
        elif isinstance(obj, list):
            for item in obj:
                replace_value(item, key, new_value)
        return obj


def m_3_2_6():
    def print_json(obj, indent=0):
        if isinstance(obj, dict):
            for key, value in obj.items():
                print("  " * indent + f"Key: {key}")
                print_json(value, indent + 1)
        elif isinstance(obj, list):
            for item in obj:
                print_json(item, indent)
        else:
            print("  " * indent + f"Value: {obj}")


# 3.3 Бинарный поиск


def m_3_3_1():
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1


def m_3_3_2():
    def lower_bound(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1

    # print(lower_bound([1, 2, 4, 6, 8], 5) == 3)


def m_3_3_3():
    def search_string(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    # print(search_string(["apple", "banana", "cherry", "date"], "cherry") == 2)
