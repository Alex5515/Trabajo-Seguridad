import os

def generate_openssl_rng_sequence(length=10, bits=32):
    # Cada número tendrá 'bits' de tamaño
    sequence = [int.from_bytes(os.urandom(bits // 8), byteorder="big") for _ in range(length)]
    return sequence

# Ejemplo de uso
openssl_sequence = generate_openssl_rng_sequence(length=10, bits=32)
print("OpenSSL RNG Sequence:", openssl_sequence).
