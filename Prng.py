import numpy as np
import scipy.stats as stats


def chi_square_frequency_test(sequence):
    """
    Prueba de frecuencia usando chi-cuadrado.
    :param sequence: Lista de números reales en [0, 1].
    :return: Valor p.
    """
    binary_sequence = [1 if x > 0.5 else 0 for x in sequence]
    observed_zeros = binary_sequence.count(0)
    observed_ones = binary_sequence.count(1)
    n = len(binary_sequence)
    expected = n / 2
    chi_square = ((observed_zeros - expected) ** 2 / expected) + ((observed_ones - expected) ** 2 / expected)
    p_value = stats.chi2.sf(chi_square, 1)  # Grados de libertad = 1
    return p_value


def kolmogorov_smirnov_test(sequence):
    """
    Prueba de Kolmogorov-Smirnov.
    :param sequence: Lista de números reales en [0, 1].
    :return: Valor p.
    """
    return stats.kstest(sequence, 'uniform').pvalue


def runs_above_mean_test(sequence):
    """
    Prueba de corridas por encima de la media.
    :param sequence: Lista de números reales.
    :return: Valor p.
    """
    mean = np.mean(sequence)
    runs = 1
    for i in range(1, len(sequence)):
        if (sequence[i - 1] < mean) != (sequence[i] < mean):
            runs += 1
    expected_runs = (2 * len(sequence) - 1) / 3
    variance_runs = (16 * len(sequence) - 29) / 90
    z = (runs - expected_runs) / np.sqrt(variance_runs)
    p_value = 2 * stats.norm.sf(abs(z))  # Dos colas
    return p_value


def fft_test(sequence):
    """
    Transformada Rápida de Fourier (FFT).
    :param sequence: Lista de números reales.
    :return: Valor p.
    """
    n = len(sequence)
    fft = np.fft.fft(sequence - np.mean(sequence))
    magnitude = np.abs(fft[:n // 2])  # Solo frecuencias positivas
    threshold = stats.norm.ppf(0.95)  # Umbral de significancia
    peaks = np.sum(magnitude > threshold)
    expected_peaks = 0.05 * (n / 2)
    variance_peaks = expected_peaks * 0.95
    z = (peaks - expected_peaks) / np.sqrt(variance_peaks)
    p_value = stats.norm.sf(abs(z)) * 2  # Dos colas
    return p_value


def approximate_entropy(sequence, m=2):
    """
    Entropía Aproximada.
    :param sequence: Lista de números reales.
    :param m: Longitud del patrón.
    :return: Valor de entropía.
    """
    def _phi(m):
        patterns = [tuple(sequence[i:i + m]) for i in range(len(sequence) - m + 1)]
        counts = {pattern: patterns.count(pattern) for pattern in set(patterns)}
        probabilities = [count / len(patterns) for count in counts.values()]
        return sum(-p * np.log(p) for p in probabilities)


    return _phi(m) - _phi(m + 1)


def correlation_test(sequence):
    """
    Ataque de correlación: Verifica dependencia entre números consecutivos.
    :param sequence: Lista de números reales.
    :return: Valor p.
    """
    x = sequence[:-1]
    y = sequence[1:]
    n = len(sequence)
    correlation = np.corrcoef(x, y)[0, 1]
    t = correlation * np.sqrt((n - 2) / (1 - correlation ** 2))
    p_value = 2 * stats.t.sf(abs(t), df=n - 2)  # Dos colas
    return p_value


# Pruebas con números aleatorios de ejemplo
if __name__ == "__main__":
    # Generar secuencia de prueba
    sequence = []
  # Números reales en [0, 1]
   
    # Ejecutar todas las pruebas
    print("Prueba Estadistica: Chi-cuadrado Frecuencia (p):", chi_square_frequency_test(sequence))
    print("Prueba Uniformidad: Kolmogorov-Smirnov (p):", kolmogorov_smirnov_test(sequence))
    print("Prueba de Independencia: Runs Above the Mean (p):", runs_above_mean_test(sequence))
    print("Prueba de periodo: FFT Test (p):", fft_test(sequence))
    print("Prueba de complejidad: Approximate Entropy:", approximate_entropy(sequence))
    print("Prueba de seguridad en la criptografia: Correlation Test (p):", correlation_test(sequence))
