"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
> sieve(2)
3
> prime(4)
7
> sieve(5)
11
> prime(1)
2
"""
import functools
import cProfile


def test_func(func):
    test_list = func_eratosfen(12)
    for i, el in enumerate(test_list):
        assert el == func(i + 1)
        print(f'n = {i + 1}, el = {el} Test OK')
    assert 541 == func(100)
    print(f'n = {100}, el = {541} Test OK')
    assert 7919 == func(1000)
    print(f'n = {1000}, el = {7919} Test OK')
    assert 104729 == func(10000)
    print(f'n = {10000}, el = {104729} Test OK')


"""
Первый — с помощью алгоритма «Решето Эратосфена».
"""


def func_eratosfen(n):
    """
    Решето Эратосфена
    Находит простые числа до заданного натурального числа
    :param n: Натуральное число
    :return: Список простых чисел до числа n
    """
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]


@functools.lru_cache()
def func1(n, size=None):
    """
    Рекурсия + меморизация
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n * 4
    primes = func_eratosfen(size)
    if len(primes) < n:
        size *= 4
        return func1(n, size)
    else:
        return primes[n - 1]


# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK

# "les_4_task_2.func1(1)"
# 100 loops, best of 5: 124 nsec per loop
# UserWarning: The test results are likely unreliable.
# The worst time (40.5 usec) was more than four times slower than the best time (124 nsec).

# "les_4_task_2.func1(2)"
# 100 loops, best of 5: 130 nsec per loop
# UserWarning: The test results are likely unreliable.
# The worst time (22.3 usec) was more than four times slower than the best time (130 nsec).

# "les_4_task_2.func1(3)"
# 100 loops, best of 5: 125 nsec per loop
# UserWarning: The test results are likely unreliable.
# The worst time (23.7 usec) was more than four times slower than the best time (125 nsec).

# "les_4_task_2.func1(4)"
# 100 loops, best of 5: 120 nsec per loop
# UserWarning: The test results are likely unreliable.
# The worst time (21.9 usec) was more than four times slower than the best time (120 nsec).

# "les_4_task_2.func1(5)"
# 100 loops, best of 5: 124 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.5 usec) was more than four times slower than the best time (124 nsec).

# "les_4_task_2.func1(100)"
# 100 loops, best of 5: 122 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (26.5 usec) was more than four times slower than the best time (122 nsec).

# "les_4_task_2.func1(1000)"
# 100 loops, best of 5: 126 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (61.2 usec) was more than four times slower than the best time (126 nsec).

# "les_4_task_2.func1(10000)"
# 100 loops, best of 5: 127 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (486 usec) was more than four times slower than the best time (127 nsec).

# cProfile.run("func1(1)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(2)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(3)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:27(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:35(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(4)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:27(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:35(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(5)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:27(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:35(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(100)")
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     2    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#     2    0.000    0.000    0.000    0.000 les_4_task_2.py:27(<listcomp>)
#     2    0.000    0.000    0.000    0.000 les_4_task_2.py:35(<listcomp>)
#   2/1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(1000)")
#     1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#     2    0.003    0.002    0.004    0.002 les_4_task_2.py:26(func_eratosfen)
#     2    0.001    0.000    0.001    0.000 les_4_task_2.py:27(<listcomp>)
#     2    0.000    0.000    0.000    0.000 les_4_task_2.py:35(<listcomp>)
#   2/1    0.000    0.000    0.004    0.004 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func1(10000)")
#     1    0.000    0.000    0.048    0.048 <string>:1(<module>)
#     2    0.036    0.018    0.046    0.023 les_4_task_2.py:26(func_eratosfen)
#     2    0.006    0.003    0.006    0.003 les_4_task_2.py:27(<listcomp>)
#     2    0.004    0.002    0.004    0.002 les_4_task_2.py:35(<listcomp>)
#   2/1    0.001    0.001    0.047    0.047 les_4_task_2.py:48(func1)
#     1    0.000    0.000    0.048    0.048 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def func2(n, size=None):
    """
    Рекурсия
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n
    primes = func_eratosfen(size)
    if len(primes) < n:
        size *= 4
        return func2(n, size)
    else:
        return primes[n - 1]


# test_func(func2)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func2(1)"
# 100 loops, best of 5: 159 nsec per loop

# "les_4_task_2.func2(2)"
# 100 loops, best of 5: 173 nsec per loop

# "les_4_task_2.func2(3)"
# 100 loops, best of 5: 2.86 usec per loop

# "les_4_task_2.func2(4)"
# 100 loops, best of 5: 3.34 usec per loop

# "les_4_task_2.func2(5)"
# 100 loops, best of 5: 4.05 usec per loop

# "les_4_task_2.func2(100)"
# 100 loops, best of 5: 332 usec per loop

# "les_4_task_2.func2(1000)"
# 100 loops, best of 5: 3.81 msec per loop

# "les_4_task_2.func2(10000)"
# 100 loops, best of 5: 44.5 msec per loop

# cProfile.run("func2(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       2/1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:33(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       2/1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:33(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       2/1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:33(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       3/1    0.000    0.000    0.000    0.000 les_4_task_2.py:194(func2)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:26(func_eratosfen)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:33(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#       3/1    0.000    0.000    0.004    0.004 les_4_task_2.py:194(func2)
#         3    0.003    0.001    0.004    0.001 les_4_task_2.py:26(func_eratosfen)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:33(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func2(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.053    0.053 <string>:1(<module>)
#       3/1    0.001    0.000    0.053    0.053 les_4_task_2.py:194(func2)
#         3    0.040    0.013    0.052    0.017 les_4_task_2.py:26(func_eratosfen)
#         3    0.008    0.003    0.008    0.003 les_4_task_2.py:33(<listcomp>)
#         3    0.004    0.001    0.004    0.001 les_4_task_2.py:41(<listcomp>)
#         1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def func3(n, size=None):
    """
    Цикл
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n
    primes = func_eratosfen(size)
    while len(primes) < n:
        size *= 4
        primes = func_eratosfen(size)
    return primes[n - 1]


# test_func(func3)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func3(1)"
# 100 loops, best of 5: 158 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (55.1 usec) was more than four times slower than the best time (158 nsec).

# "les_4_task_2.func3(2)"
# 100 loops, best of 5: 166 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.9 usec) was more than four times slower than the best time (166 nsec).

# "les_4_task_2.func3(3)"
# 100 loops, best of 5: 2.74 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (25.6 usec) was more than four times slower than the best time (2.74 usec).

# "les_4_task_2.func3(4)"
# 100 loops, best of 5: 3.38 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (26.2 usec) was more than four times slower than the best time (3.38 usec).

# "les_4_task_2.func3(5)"
# 100 loops, best of 5: 3.76 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (26.8 usec) was more than four times slower than the best time (3.76 usec).

# "les_4_task_2.func3(100)"
# 100 loops, best of 5: 334 usec per loop

# "les_4_task_2.func3(1000)"
# 100 loops, best of 5: 3.8 msec per loop

# "les_4_task_2.func3(10000)"
# 100 loops, best of 5: 46.9 msec per loop

# cProfile.run("func3(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:308(func3)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 les_4_task_2.py:308(func3)
#         3    0.004    0.001    0.005    0.002 les_4_task_2.py:44(func_eratosfen)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("func3(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.050    0.050 <string>:1(<module>)
#         1    0.001    0.001    0.050    0.050 les_4_task_2.py:308(func3)
#         3    0.039    0.013    0.049    0.016 les_4_task_2.py:44(func_eratosfen)
#         3    0.006    0.002    0.006    0.002 les_4_task_2.py:51(<listcomp>)
#         3    0.004    0.001    0.004    0.001 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.050    0.050 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

@functools.lru_cache()
def func4(n, size=None):
    """
    Цикл
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n
    primes = func_eratosfen(size)
    while len(primes) < n:
        size *= 4
        primes = func_eratosfen(size)
    return primes[n - 1]


# test_func(func4)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func4(1)"
# 100 loops, best of 5: 130 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (62.4 usec) was more than four times slower than the best time (130 nsec).
#
#  "les_4_task_2.func4(2)"
# 100 loops, best of 5: 124 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.5 usec) was more than four times slower than the best time (124 nsec).
#
# "les_4_task_2.func4(3)"
# 100 loops, best of 5: 133 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (24.6 usec) was more than four times slower than the best time (133 nsec).
#
# "les_4_task_2.func4(4)"
# 100 loops, best of 5: 128 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.1 usec) was more than four times slower than the best time (128 nsec).
#
# "les_4_task_2.func4(5)"
# 100 loops, best of 5: 133 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.2 usec) was more than four times slower than the best time (133 nsec).
#
# "les_4_task_2.func4(100)"
# 100 loops, best of 5: 122 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (28.4 usec) was more than four times slower than the best time (122 nsec).
#
# "les_4_task_2.func4(1000)"
# 100 loops, best of 5: 128 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (68.8 usec) was more than four times slower than the best time (128 nsec).
#
# "les_4_task_2.func4(10000)"
# 100 loops, best of 5: 140 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (483 usec) was more than four times slower than the best time (140 nsec).

# cProfile.run("func4(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         3    0.003    0.001    0.004    0.001 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.004    0.004 les_4_task_2.py:485(func4)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func4(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.054    0.054 <string>:1(<module>)
#         3    0.041    0.014    0.053    0.018 les_4_task_2.py:44(func_eratosfen)
#         1    0.001    0.001    0.053    0.053 les_4_task_2.py:485(func4)
#         3    0.007    0.002    0.007    0.002 les_4_task_2.py:51(<listcomp>)
#         3    0.004    0.001    0.004    0.001 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


""" 
Второй — без использования «Решета Эратосфена».
"""


def find_primes_optimized_memory(n):
    """
    Отимизированный перебор
    Находит простые числа до заданного натурального числа
    :param n: Натуральное число
    :return: Список простых чискл до числа n
    """
    primes = [2]
    for i in range(3, n, 2):
        flag = True
        for j in primes:
            if j ** 2 > i:
                break
            if i % j == 0:
                flag = False
                break
        if flag:
            primes.append(i)
    return primes


@functools.lru_cache()
def func5(n, size=None):
    """
    Рекурсия + меморизация
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n * 4
    primes = find_primes_optimized_memory(size)
    if len(primes) < n:
        size *= 4
        return func4(n, size)
    else:
        return primes[n - 1]

# test_func(func5)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func5(1)"
# 100 loops, best of 5: 121 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (60.9 usec) was more than four times slower than the best time (121 nsec).
#
# "les_4_task_2.func5(2)"
# 100 loops, best of 5: 129 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.3 usec) was more than four times slower than the best time (129 nsec).
#
# "les_4_task_2.func5(3)"
# 100 loops, best of 5: 121 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.3 usec) was more than four times slower than the best time (121 nsec).
#
# "les_4_task_2.func5(4)"
# 100 loops, best of 5: 126 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.2 usec) was more than four times slower than the best time (126 nsec).
#
# "les_4_task_2.func5(5)"
# 100 loops, best of 5: 123 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.7 usec) was more than four times slower than the best time (123 nsec).
#
# "les_4_task_2.func5(100)"
# 100 loops, best of 5: 122 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (28.1 usec) was more than four times slower than the best time (122 nsec).
#
# "les_4_task_2.func5(1000)"
# 100 loops, best of 5: 125 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (78.7 usec) was more than four times slower than the best time (125 nsec).
#
# "les_4_task_2.func5(10000)"
# 100 loops, best of 5: 126 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (842 usec) was more than four times slower than the best time (126 nsec).

# cProfile.run("func5(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.001    0.001 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        77    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.003    0.003 les_4_task_2.py:485(func4)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.006    0.006 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       549    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func5(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.096    0.096 <string>:1(<module>)
#         1    0.039    0.039    0.047    0.047 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.048    0.048 les_4_task_2.py:485(func4)
#         1    0.005    0.005    0.005    0.005 les_4_task_2.py:51(<listcomp>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:59(<listcomp>)
#         1    0.048    0.048    0.048    0.048 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.001    0.001    0.096    0.096 les_4_task_2.py:663(func5)
#         1    0.000    0.000    0.097    0.097 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      4202    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



def func6(n, size=None):
    """
    Рекурсия
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n * 4
    primes = find_primes_optimized_memory(size)
    if len(primes) < n:
        size *= 4
        return func4(n, size)
    else:
        return primes[n - 1]

# test_func(func6)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func6(1)"
# 100 loops, best of 5: 150 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (65.2 usec) was more than four times slower than the best time (150 nsec).
#
# "les_4_task_2.func6(2)"
# 100 loops, best of 5: 166 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.5 usec) was more than four times slower than the best time (166 nsec).
#
# "les_4_task_2.func6(3)"
# 100 loops, best of 5: 2.66 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (27.8 usec) was more than four times slower than the best time (2.66 usec).
#
# "les_4_task_2.func6(4)"
# 100 loops, best of 5: 3.73 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (29 usec) was more than four times slower than the best time (3.73 usec).
#
# "les_4_task_2.func6(5)"
# 100 loops, best of 5: 5.06 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (28 usec) was more than four times slower than the best time (5.06 usec).
#
# "les_4_task_2.func6(100)"
# 100 loops, best of 5: 173 usec per loop
#
# "les_4_task_2.func6(1000)"
# 100 loops, best of 5: 2.56 msec per loop
#
# "les_4_task_2.func6(10000)"
# 100 loops, best of 5: 44 msec per

# cProfile.run("func6(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:485(func4)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        77    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:44(func_eratosfen)
#         1    0.000    0.000    0.003    0.003 les_4_task_2.py:485(func4)
#         1    0.001    0.001    0.001    0.001 les_4_task_2.py:51(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.003    0.003    0.003    0.003 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.000    0.000    0.006    0.006 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       549    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func6(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.100    0.100 <string>:1(<module>)
#         1    0.042    0.042    0.052    0.052 les_4_task_2.py:44(func_eratosfen)
#         1    0.001    0.001    0.052    0.052 les_4_task_2.py:485(func4)
#         1    0.005    0.005    0.005    0.005 les_4_task_2.py:51(<listcomp>)
#         1    0.004    0.004    0.004    0.004 les_4_task_2.py:59(<listcomp>)
#         1    0.047    0.047    0.047    0.047 les_4_task_2.py:642(find_primes_optimized_memory)
#         1    0.001    0.001    0.100    0.100 les_4_task_2.py:822(func6)
#         1    0.000    0.000    0.100    0.100 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      4202    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


@functools.lru_cache()
def func7(n, size=None):
    """
    Цикл + меморизация
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n
    primes = func_eratosfen(size)
    while len(primes) < n:
        size *= 4
        primes = func_eratosfen(size)
    return primes[n - 1]

# test_func(func7)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func7(1)"
# 100 loops, best of 5: 129 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (59.7 usec) was more than four times slower than the best time (129 nsec).
#
# "les_4_task_2.func7(2)"
# 100 loops, best of 5: 133 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23.7 usec) was more than four times slower than the best time (133 nsec).
#
# "les_4_task_2.func7(3)"
# 100 loops, best of 5: 123 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (23 usec) was more than four times slower than the best time (123 nsec).
#
# "les_4_task_2.func7(4)"
# 100 loops, best of 5: 129 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22 usec) was more than four times slower than the best time (129 nsec).
#
# "les_4_task_2.func7(5)"
# 100 loops, best of 5: 121 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (24 usec) was more than four times slower than the best time (121 nsec).
#
# "les_4_task_2.func7(100)"
# 100 loops, best of 5: 137 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (26 usec) was more than four times slower than the best time (137 nsec).
#
# "les_4_task_2.func7(1000)"
# 100 loops, best of 5: 122 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (64.2 usec) was more than four times slower than the best time (122 nsec).
#
# "les_4_task_2.func7(10000)"
# 100 loops, best of 5: 127 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (490 usec) was more than four times slower than the best time (127 nsec).

# cProfile.run("func7(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         3    0.003    0.001    0.005    0.002 les_4_task_2.py:44(func_eratosfen)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.005    0.005 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func7(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.051    0.051 <string>:1(<module>)
#         3    0.039    0.013    0.050    0.017 les_4_task_2.py:44(func_eratosfen)
#         3    0.007    0.002    0.007    0.002 les_4_task_2.py:51(<listcomp>)
#         3    0.004    0.001    0.004    0.001 les_4_task_2.py:59(<listcomp>)
#         1    0.001    0.001    0.051    0.051 les_4_task_2.py:973(func7)
#         1    0.000    0.000    0.051    0.051 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}





def func8(n, size=None):
    """
    Цикл
    :param n: Порядковый номер простого числа
    :param size: Величина массива простых чисел
    :return: Простое число
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if size is None:
        size = n
    primes = func_eratosfen(size)
    while len(primes) < n:
        size *= 4
        primes = func_eratosfen(size)
    return primes[n - 1]

# test_func(func8)
# n = 1, el = 2 Test OK
# n = 2, el = 3 Test OK
# n = 3, el = 5 Test OK
# n = 4, el = 7 Test OK
# n = 5, el = 11 Test OK
# n = 100, el = 541 Test OK
# n = 1000, el = 7919 Test OK
# n = 10000, el = 104729 Test OK

# "les_4_task_2.func8(1)"
# 100 loops, best of 5: 156 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (65 usec) was more than four times slower than the best time (156 nsec).
#
# "les_4_task_2.func8(2)"
# 100 loops, best of 5: 168 nsec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (22.4 usec) was more than four times slower than the best time (168 nsec).
#
#  "les_4_task_2.func8(3)"
# 100 loops, best of 5: 2.72 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (25.3 usec) was more than four times slower than the best time (2.72 usec).
#
# "les_4_task_2.func8(4)"
# 100 loops, best of 5: 3.35 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (27.5 usec) was more than four times slower than the best time (3.35 usec).
#
# "les_4_task_2.func8(5)"
# 100 loops, best of 5: 3.8 usec per loop
# :0: UserWarning: The test results are likely unreliable.
# The worst time (29.5 usec) was more than four times slower than the best time (3.8 usec).
#
# "les_4_task_2.func8(100)"
# 100 loops, best of 5: 342 usec per loop
#
# "les_4_task_2.func8(1000)"
# 100 loops, best of 5: 3.84 msec per loop
#
# "les_4_task_2.func8(10000)"
# 100 loops, best of 5: 44.8 msec per loop

# cProfile.run("func8(1)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(2)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(3)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(4)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(5)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(100)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:1127(func8)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:44(func_eratosfen)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(1000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.004    0.004 les_4_task_2.py:1127(func8)
#         3    0.003    0.001    0.004    0.001 les_4_task_2.py:44(func_eratosfen)
#         3    0.001    0.000    0.001    0.000 les_4_task_2.py:51(<listcomp>)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run("func8(10000)")
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.053    0.053 <string>:1(<module>)
#         1    0.001    0.001    0.052    0.052 les_4_task_2.py:1127(func8)
#         3    0.040    0.013    0.052    0.017 les_4_task_2.py:44(func_eratosfen)
#         3    0.008    0.003    0.008    0.003 les_4_task_2.py:51(<listcomp>)
#         3    0.004    0.001    0.004    0.001 les_4_task_2.py:59(<listcomp>)
#         1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
