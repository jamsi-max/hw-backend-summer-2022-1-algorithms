__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 0 or number == 1:
        return False

    if number > 2 and number % 2 == 0:
        return False

    DIV = 2

    while DIV * DIV <= number and number % DIV != 0:
        DIV += 1

    return DIV * DIV > number
