import timeit
from ex1 import array_diff

# Пример функции
def my_function():
    return sum([i for i in range(10000)])

# Замер времени выполнения функции
execution_time = timeit.timeit('my_function()', globals=globals(), number=1000)
print(f'Время выполнения: {execution_time} секунд')