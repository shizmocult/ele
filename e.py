import math

def taylor_ln_series(x, eps):
    term = 2 * x
    sum_result = term
    n = 1
    while abs(term) >= eps:
        n += 2
        term = 2 * (x ** n) / n
        sum_result += term
    return sum_result

def compare_ln(x, eps):
    approx = taylor_ln_series(x, eps)
    exact = math.log((1 + x) / (1 - x))
    return approx, exact

if __name__ == "__main__":
    x_val = 0.5
    eps_val = 1e-6
    approx, exact = compare_ln(x_val, eps_val)
    print(f"Taylor series for ln((1+x)/(1-x)) with x={x_val}:")
    print("  Approximation:", approx)
    print("  Exact value: ", exact)
