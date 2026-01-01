import base64

def encode(payload: str) -> str:
    return base64.b64encode(payload.encode()).decode()

def decode(payload: str) -> str:
    return base64.b64decode(payload.encode()).decode()
