# Декоратор, подсчитывающий время выполнения функции
import time
  
def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        print("Время выполнения функции: ", time.time() - start_time)
    return wrapper

@decorator
def test_func():
    print('Hi!')
 
test_func()
