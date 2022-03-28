import os
import uuid

import nanoid


def generate_nanoid(
    size: int = 8,
    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_",
):
    """
    랜덤 문자열 생성
    """
    return nanoid.generate(alphabet, size)