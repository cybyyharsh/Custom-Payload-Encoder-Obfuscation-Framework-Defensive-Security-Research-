def obfuscate(payload: str) -> str:
    return ''.join('\\x{:02x}'.format(ord(c)) for c in payload)
