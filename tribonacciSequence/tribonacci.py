def getTribonacci(limit):
    next = 0
    sequence = [0, 0, 1]
    while(next <= limit):
        next = addNumbers(int(sequence[len(sequence) - 3]), int(sequence[len(sequence) - 2]), int(sequence[len(sequence) - 1]))
        sequence.append(next)

    return sequence

def addNumbers(a, b, c):
    return a + b + c
