def memoize(func):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized

def expensive_computation(x):
    # Simulating a costly function
    result = 0
    for i in range(1, x + 1):
        result += i ** 2
    return result

memoized_computation = memoize(expensive_computation)

# Example usage
if __name__ == '__main__':
    print(memoized_computation(1000))
    print(memoized_computation(1000))  # Should return cached result
    print(memoized_computation(500))
    print(memoized_computation(500))  # Should return cached result
