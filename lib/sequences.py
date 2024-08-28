def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    
    fib_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    
    
    formatted_sequence = '[' + ', '.join(map(str, fib_sequence)) + ']'
    print(formatted_sequence + '')