def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
n = 5
print(f"The factorial of {n} is {factorial(n)}")
