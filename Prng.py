import numpy as np

class CustomPRNG:
    def __init__(self, seed=None):
        """
        Generador de números pseudoaleatorios (PRNG) personalizado con varias técnicas.

        Args:
            seed (int, opcional): Semilla inicial para el generador. Si no se proporciona,
                                 se utiliza una semilla aleatoria.
        """
        if seed is None:
            seed = np.random.randint(1, 2**32 - 1)

        self._state = seed
        self._a = 1597
        self._c = 51749
        self._m = 2**31 - 1  # Primo de Mersenne

    def _xorshift(self, x):
        """
        Transformación XORshift para mejorar la aleatoriedad.

        Args:
            x (int): Valor de entrada.

        Returns:
            int: Valor transformado.
        """
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        return x

    def _linear_congruential(self, x):
        """
        Método congruencial lineal para generar el siguiente número.

        Args:
            x (int): Valor actual.

        Returns:
            int: Siguiente valor.
        """
        return (self._a * x + self._c) % self._m

    def random(self):
        """
        Genera un número aleatorio en el rango [0, 1).

        Returns:
            float: Número aleatorio normalizado.
        """
        self._state = self._xorshift(self._state)
        self._state = self._linear_congruential(self._state)
        return self._state / self._m

    def randint(self, low, high):
        """
        Genera un número entero aleatorio en el rango [low, high].

        Args:
            low (int): Límite inferior (incluido).
            high (int): Límite superior (incluido).

        Returns:
            int: Número entero aleatorio.
        """
        return int(self.random() * (high - low + 1)) + low

    def rand_array(self, size):
        """
        Genera un array de números aleatorios en el rango [0, 1).

        Args:
            size (int): Tamaño del array.

        Returns:
            numpy.ndarray: Array de números aleatorios.
        """
        return np.array([self.random() for _ in range(size)])

# Ejecutar prueba
if __name__ == "__main__":
    prng = CustomPRNG(seed=42)
    print("Primeros 10 números generados:")
    print([prng.random() for _ in range(10)])
