from time import time

def factorize(*numbers):
    data = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        data.append(factors)
    return data

if __name__ == '__main__':
    start_time = time()
    numbers = factorize(128, 255, 99999, 10651060)


    print(numbers)

    
    end_time = time() - start_time
    print(f'App ended. [{end_time:.1f}] seconds...')