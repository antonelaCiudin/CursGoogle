def sum_func(*nums, **params):
    suma = 0
    for n in nums:
        if type(n) == int or type(n) == float:
            suma += float(n)

    return int(suma) if suma - int(suma) == 0 else suma


def recursive_func(n: int) -> (int, int, int):
    return sum(range(n)), sum(range(0, n, 2)), sum(range(1, n, 2))


def check_input_func():
    user_input = input()

    return int(user_input) if user_input.isnumeric() else 0


def main():
    print(sum_func(1, 5, -3, 'abc', [12, 56, 'cad']))
    print(sum_func())
    print(sum_func(2, 4, 'abc', param_1=2))

    print(recursive_func(5))

    print(check_input_func())


if __name__ == "__main__":
    main()
