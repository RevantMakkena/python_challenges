from typing import List


def slices(series: str, length: int) -> List[str]:
    """Output all the contiguous substrings of length n in series."""
    if length > len(series) or length <= 0:
        raise ValueError(f"Error Length: {length}")

    return [series[i:i + length] for i in range(len(series) - length + 1)]
