def generate_sequence_a(x, k):
    xk = 1  # x^0 / 0! = 1
    for i in range(1, k + 1):
        xk *= x**2 / ((2 * i - 1) * (2 * i))
    return xk

if __name__ == "__main__":
    print("x_k for x=2, k=3:", generate_sequence_a(2, 3))