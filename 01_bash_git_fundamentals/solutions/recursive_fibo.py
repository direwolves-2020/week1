cache = {}

def fibo(n):
    """Returns the `n`th number of a fibonacci series"""
    if n in cache.keys():
        return cache[n]

    if n < 3:
        answer = n-1
    else:
        answer = fibo(n-1) + fibo(n-2)

    cache[n] = answer
    return answer


print(fibo(40))