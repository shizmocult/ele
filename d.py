def generate_sum_d(x, n):
    a_prev, a_curr = 1, 1
    sum_result = 0
    factorial = 1
    for k in range(1, n + 1):
        if k > 2:
            a_prev, a_curr = a_curr, a_prev + a_curr
        a_k = a_curr
        factorial *= (2 * k - 1) * (2 * k)
        sum_result += a_k * (x ** (2 * k)) / factorial
    return sum_result

if __name__ == "__main__":
    print("S_n for x=1, n=5:", generate_sum_d(1, 5))