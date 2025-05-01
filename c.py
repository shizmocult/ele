def order_of_zero(a, b, max_n=100):
    values = [((a + b) ** i - a ** i - b ** i) for i in range(max_n)]
    for order in range(max_n):
        if all(abs(v) < 1e-12 for v in values):
            return order
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return max_n

if __name__ == "__main__":
    print("Order of zero for a=1, b=2:", order_of_zero(1, 2))