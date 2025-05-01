def generate_product_b(n):
    product = 1
    for i in range(1, n + 1):
        product *= 1 + 1 / (i ** 2)
    return product

if __name__ == "__main__":
    print("P_n for n=5:", generate_product_b(5))