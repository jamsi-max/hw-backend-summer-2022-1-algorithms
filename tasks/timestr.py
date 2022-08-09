__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds < 60:
        return f'{seconds:02}s'

    if 60 <= seconds < 3600:
        return f'{seconds//60:02}m{seconds%60:02}s'

    if 3600 <= seconds < 86400:
        return f'{seconds//3600:02}h{seconds%3600//60:02}m{seconds%60:02}s'

    if 86400 <= seconds:
        return f'{seconds//86400:02}d\
{seconds%86400//3600:02}h{seconds%3600//60:02}m{seconds%60:02}s'
