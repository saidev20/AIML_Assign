def fibonacci(limit: int) -> list[int]:
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:limit]

if __name__ == "__main__":
    print("First 10 Fibonacci numbers:", fibonacci(10))
