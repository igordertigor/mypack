def super_sum(*args) -> float:
    if len(args) == 1:
        raise ValueError('No sum of single arg')
    values = (_convert(x) for x in args)
    return sum(values)


def _convert(x: int | float | str) -> float:
    return float(x)
