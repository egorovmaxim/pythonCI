import time

def min(arr):
    minimum = arr[0]
    for item in arr:
        if (item < minimum):
            minimum = item
    return minimum

def max(arr):
    maximum = arr[0]
    for item in arr:
        if (item > maximum):
            maximum = item
    return maximum

def sum(arr):
    sum = 0
    for item in arr:
        sum = sum + item
    return sum

def mult(arr):
    mult = 1
    for item in arr:
        mult = mult * item
    return mult

def run_time(start_time) -> float:
    result = time.time() - start_time
    return result

# тест для получения количества отрицательных чисел
def negative_count(array):
    neg_count = 0
    for item in array:
        if (item < 0):
            neg_count = neg_count + 1
    return neg_count

file = open("numbers.txt", "r")
file = file.read().split(' ')

nums = list(map(int, file))

start_time = time.time()

print("Минимум: %d" % min(nums))
print("Максимум: %d" % max(nums))

try:
    print("Сумма: %d" % sum(nums))
    print("Произведение: %d" % mult(nums))
except OverflowError:
    print("Ошибка переполнения!")
    exit(0)

print("Количество отрицательных чисел: %d" % negative_count(nums))
print("Время выполнения программы: %f секунд" % run_time(start_time))

# пример файла numbers.txt:
# 4 3 -1 -3 2

# вывод
# Минимум: -3
# Максимум: 4
# Сумма: 5
# Произведение: 72
# Количество отрицательных чисел: 2
# Время выполнения программы: 0.000211 секунд