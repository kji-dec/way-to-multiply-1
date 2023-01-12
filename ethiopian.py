def hello():
    print('Good luck!!')


def division(div_num: int) -> int:
    return div_num // 2


def multiplication(mul_num: int) -> int:
    return mul_num * 2


def is_odd(quotient: int) -> bool:
    return quotient % 2 == 1


def main():
    num1, num2 = map(int, input("input two integers with sapcing.").split())
    sum_ = 0
    div = max(num1, num2)
    mul = min(num1, num2)

    while div >= 1:
        div = division(div)
        mul = multiplication(mul)

        if is_odd(div):
            sum_ += mul
        else:
            continue


    print(sum_)





if __name__=='__main__':
    main()
