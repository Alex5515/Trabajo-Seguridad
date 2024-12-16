import random

def generate_mersenne_twister_sequence(length=10, seed=None):
    # Inicializamos el generador con una semilla (opcional)
    mt_generator = random.Random(seed)
    
    # Generamos una secuencia de números aleatorios
    sequence = [mt_generator.random() for _ in range(length)]
    return sequence

# Ejemplo de uso
mersenne_sequence = generate_mersenne_twister_sequence(length=10, seed=12345)
print("Mersenne Twister Sequence:", mersenne_sequence)
