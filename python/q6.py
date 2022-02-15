def solution(numbers):
    ''''''
    sum = 0;
    for val in range(0,10):
        sum += val
    
    for val in numbers:
        sum -= val

    return sum