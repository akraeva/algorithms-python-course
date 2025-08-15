# Stepick.org — Алгоритмы в Python — просто, наглядно, с нуля!
# 1. Базовые алгоритмы и анализ сложности


# 1.1 Алгоритмы на примерах


def m_1_1_1():
    def find_min(nums):
        min_num = nums[-1]
        for num in nums:
            if min_num > num:
                min_num = num
        return min_num


def m_1_1_2():
    def count_vowels(string):
        result = sum(1 for ch in string if ch.lower() in "аеёиоуыэюя") if string else 0
        return result


def m_1_1_3():
    def sum_list(nums):
        acc = 0
        for num in nums:
            acc += num
        return acc


def m_1_1_4():
    def find_index(nums, num):
        for i, n in enumerate(nums):
            if n == num:
                return i
        return -1


def m_1_1_5():
    def count_increases(nums):
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                counter += 1
        return counter


def m_1_1_6():
    def max_abs(nums):
        result = nums[-1]
        for num in nums:
            if abs(num) > abs(result):
                result = num
        return result


# 1.2 Анализ сложности: O-нотация


def m_1_2_1():
    def linear_search(nums, n):
        for num in nums:
            if num == n:
                return True
        return False


def m_1_2_2():
    def sum_of_squares(n):
        return sum(map(lambda x: x**2, range(1, n + 1)))


def m_1_2_3():
    def count_pairs(nums):
        res = sum(
            1
            for i in range(len(nums) - 1)
            for j in range(i + 1, len(nums))
            if arr[i] == arr[j]
        )
        return res


def m_1_2_4():
    def count_doublings(n):
        i = 0
        while 2**i < n:
            i += 1
        return i


# 1.3 Линейный и бинарный поиск


def m_1_3_1():
    def linear_search(nums, num):
        for i in range(len(nums)):
            if nums[i] == num:
                return i
        return -1


def m_1_3_2():
    def last_occurrence(nums, num):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == num:
                return i
        return -1


def m_1_3_3():
    def binary_search(nums, num):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == num:
                return mid
            elif nums[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# 1.4 Сортировка выбором и пузырьком


def m_1_4_1():
    def is_sorted(arr):
        for i in range(1, len(arr) - 1):
            if arr[i - 1] > arr[i]:
                return False
        return True


def m_1_4_2():
    def selection_sort(nums):
        count = len(nums)
        for i in range(count):
            min = i
            for j in range(i, count):
                if nums[j] < nums[min]:
                    min = j
            if min != i:
                nums[i], nums[min] = nums[min], nums[i]
        return nums


def m_1_4_3():
    def selection_sort_desc(nums):
        count = len(nums)
        for i in range(count):
            max = i
            for j in range(i, count):
                if nums[j] > nums[max]:
                    max = j
            if min != i:
                nums[i], nums[max] = nums[max], nums[i]
        return nums


def m_1_4_4():
    def bubble_sort(nums):
        count = len(nums)
        for i in range(count - 1):
            is_sorted = True
            for j in range(count - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_sorted = False
            if is_sorted:
                break
        return nums


def m_1_4_5():
    def sort_by_age(data):
        count = len(data)
        for i in range(count):
            min = i
            for j in range(i + 1, count):
                if data[j]["age"] < data[min]["age"]:
                    min = j
            if min != i:
                data[i], data[min] = data[min], data[i]
        return data
