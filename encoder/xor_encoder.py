def xor_encode(payload: str, key: int = 3) -> str:
    return ''.join(chr(ord(c) ^ key) for c in payload)
