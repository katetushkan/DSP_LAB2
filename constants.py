import math

EXPECTED_ROOT_MEAN_SQUARE = 0.707
EXPECTED_AMPLITUDE = 1
N = 64
K = N // 4
PHASES = {
    '0': 0,
    r'\pi/2': math.pi / 2
}
LABELS = [
    'Amplitude fouriere error',
    'Root avearage sqaure with constant component error',
    'Root average sqaure without constant component error'
]
