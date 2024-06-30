class MyException1(Exception):
    pass


class MyException2(Exception):
    pass


def temper(a):
    if a < 0:
        raise MyException1('Температура не может быть ниже -70')
    elif a > 70:
        raise MyException2('Температура не может быть больше 70')
    return True


try:
    temper(-200)
except MyException1 as exc:
    print(exc)

try:
    temper(80)
except MyException2 as exc:
    print(exc)
