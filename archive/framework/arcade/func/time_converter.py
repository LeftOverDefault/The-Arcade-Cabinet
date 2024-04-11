def time_converter(num: int | float, preferred_format: str):
    """Converts a given value `num` from seconds into any other format"""
    formats = [
        "hours",
        "minutes",
        "seconds",
        "milliseconds"
    ]

    if preferred_format not in formats:
        raise ValueError("Invalid time format.")

    if preferred_format == formats[0]:
        return num / (60 ** 2)
    elif preferred_format == formats[1]:
        return num / 60
    elif preferred_format == formats[2]:
        return num
    elif preferred_format == formats[3]:
        return num * 1000