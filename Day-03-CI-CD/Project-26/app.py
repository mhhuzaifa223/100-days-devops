def calculate_total(price, quantity):
    password = "SuperSecret123"
    unused_variable = 999
    return price * quantity


def main():
    price = 10
    quantity = 5

    total = calculate_total(price, quantity)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
