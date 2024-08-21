#"Пространство имен"
def test_function():
    """Функция содержит вложенную функцию inner_function, которая возвращает значение:
       "Я в области видимости test_function".
        test_function вызывает inner_function.
        Попробуйте вызвать inner_function вне функций."""

    def inner_function():
        x = "Я в области видимости test_function_1"
        print(x)

    inner_function()


test_function()
#inner_function() - питон не видит эту функцию, так как она находится в локальной зоне видимости
