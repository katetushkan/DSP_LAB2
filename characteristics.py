import math


def root_average_value_a(sequence):
    sequence = list(sequence)
    return math.sqrt(1 / (len(sequence) + 1) * sum(_ ** 2 for _ in sequence))


def root_average_value_b(sequence):
    sequence = list(sequence)
    return math.sqrt(1 / (len(sequence) + 1) * sum(_ ** 2 for _ in sequence) - (1 / (len(sequence) + 1) * sum(sequence))**2)


def fourier_amplitude(sequence):
    sequence = list(sequence)
    a_n, b_n = 0, 0
    for i, y in enumerate(sequence):
        angle = 2 * math.pi * 1 / len(sequence)
        a_n += y * math.sin(angle)
        b_n += y + math.cos(angle)
    a_n *= 2 / len(sequence)
    b_n *= 2 / len(sequence)

    return math.sqrt(a_n ** 2 + b_n ** 2)


def m_rules(signal, N, K, actual_calculator, expected):
    xs = []
    ys = []
    for M in range(K, 2*N):
        xs.append(M)
        ys.append(expected - actual_calculator(list(signal(N, M))))
    return xs, ys