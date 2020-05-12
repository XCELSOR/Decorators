def speedtest(interations):
    def decor(func):


        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(interations):
                start = time.time()
                val = func(*args, **kwargs)
                finish = time.time()
                total = total + (finish - start)
            print(f'Среднее: {total / interations} секунд.')
            return val

        return wrapper
    return decor