"""Тестовое задание Python Developer Trainee."""

import asyncio
import random
import sys
from hashlib import sha256
from typing import Optional


async def print_worker(msg: str) -> None:
    """Функция печатает текст, с задержкой от 1 до max_sleep_time сек.

    Args:
        msg (str): строка для печати.
    """
    max_sleep_time = 5

    # not a security/cryptographic purposes.
    await asyncio.sleep(random.randint(1, max_sleep_time))  # noqa:S311

    # print allowed in scripts:
    print(msg)  # noqa:WPS421


async def main() -> None:
    """Функция создает асинхронные задачи и запускает их."""
    args = ('Sergey', 'Python Developer Trainee', '60.000+')
    tasks = []

    for arg in args:
        task = print_worker(arg)
        tasks.append(task)

    await asyncio.gather(*tasks)


def calc_sha256_from_input() -> Optional[str]:
    """Функция читает stdin и возвращает sha256 от полученных данных.

    Returns:
        Хеш от stdin 16-й формат или None, если данных не было
    """
    # print allowed in scripts:
    print('Type any text:')  # noqa:WPS421

    line = sys.stdin.readline().strip()
    if line:
        return sha256(line.encode(encoding='utf-8')).hexdigest()


if __name__ == '__main__':
    asyncio.run(main())
    # print allowed in scripts:
    print(calc_sha256_from_input())  # noqa:WPS421
