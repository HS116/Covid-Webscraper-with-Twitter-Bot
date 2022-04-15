#Decorators to measure time performance
import time
def timer_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.time()
        return_value = original_function(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start} seconds")
        return return_value
    return wrapper_function
