def super_sum(*args) -> float:
    values = (_convert(x) for x in args)
    return sum(values)


def _convert(x: int | float | str) -> float:
    return float(x)
