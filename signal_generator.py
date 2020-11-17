import math


def harmonic_signal_generator(N, M, phase):
    for _ in range(M):
        yield math.sin((2*math.pi*_)/N + phase)