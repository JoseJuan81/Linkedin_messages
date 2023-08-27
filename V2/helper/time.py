import time
from random import choice


def time_to_sleep(min: int, max: int) -> None:
    seconds = choice(range(min, max + 1))
    time.sleep(seconds)
