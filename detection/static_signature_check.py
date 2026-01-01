def detect(payload: str) -> bool:
    signatures = ["payload", "execute", "command"]
    return any(sig in payload.lower() for sig in signatures)
