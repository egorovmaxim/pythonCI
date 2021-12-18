import program

# обязательный префикс 'test' в названии функции
def test_program():
    assert program.min([1, 2, -5, 6]) == -5, "Тест не прошёл для функции min"
    assert program.max([-9, -1, 3, 0, 0]) == 3, "Тест не прошёл для функции max"
    assert program.sum([2, 1, 2, 3, 1]) == 9, "Тест не прошёл для функции sum"
    assert program.mult([2, 2, 3, 1, 1, 2]) == 24, "Тест не прошёл для функции mult"
    assert program.negative_count([0, -1, 3]) == 1, "Тест не прошёл для функции negative_count"
    assert program.run_time(program.start_time) < 20, "Тест не прошёл для run_time (больше 20 сек. выполнения)"
