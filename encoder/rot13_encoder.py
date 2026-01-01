import codecs

def rot13(payload: str) -> str:
    return codecs.encode(payload, 'rot_13')
