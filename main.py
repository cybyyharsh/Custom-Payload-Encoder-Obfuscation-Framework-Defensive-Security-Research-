from encoder.base64_encoder import encode as b64_encode
from encoder.xor_encoder import xor_encode
from encoder.rot13_encoder import rot13

from obfuscation.random_insertion import obfuscate as random_obf
from detection.static_signature_check import detect

payload = "test_payload_example"

print("[+] Original Payload:", payload)
print("[+] Detected:", detect(payload))

b64_payload = b64_encode(payload)
print("\n[+] Base64 Encoded:", b64_payload)
print("[+] Detected:", detect(b64_payload))

xor_payload = xor_encode(payload)
print("\n[+] XOR Encoded:", xor_payload)
print("[+] Detected:", detect(xor_payload))

obf_payload = random_obf(payload)
print("\n[+] Obfuscated Payload:", obf_payload)
print("[+] Detected:", detect(obf_payload))
