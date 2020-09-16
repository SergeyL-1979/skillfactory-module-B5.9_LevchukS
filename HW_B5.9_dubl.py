import time

class Repeater:
    def __init__(self, num_runs = 10):
        self.num_runs = num_runs
    def __call__(self, func):
        def wrap():
            start = time.time()
            func()
            print("Начало функции-обертки")
            for i in range(self.num_runs):
                func()
            print("Конец функции обертки")
            end = time.time()
            print('[*] Время выполнения: {} sec.'.format((end-start)/self.num_runs))
        return wrap

rep = Repeater()

# Используем декоратор
@rep
def f():
    print("Основная функция")

# Теперь вызовем функцию
f()