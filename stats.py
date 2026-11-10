"""Summary statistics over a list of numbers."""


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2
    return ordered[mid]


def percent_change(old: float, new: float) -> float:
    return (new - old) / new * 100
