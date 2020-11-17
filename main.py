import math

from characteristics import fourier_amplitude, root_average_value_a, root_average_value_b, m_rules
from constants import EXPECTED_AMPLITUDE, EXPECTED_ROOT_MEAN_SQUARE, N, K, PHASES, LABELS
from createSchema import plot_section
from matplotlib import pyplot as plt

from signal_generator import harmonic_signal_generator


def lab_2():
    lines = []

    plt.subplots_adjust(top=0.8)

    for i, phase_description in enumerate(PHASES.items()):
        phase_repr, phase = phase_description
        plt.subplot(1, 2, i + 1)
        signal = lambda N, M: harmonic_signal_generator(N, M, phase)
        plots = [
            m_rules(signal, N, K, fourier_amplitude, EXPECTED_AMPLITUDE),
            m_rules(signal, N, K, root_average_value_a, EXPECTED_ROOT_MEAN_SQUARE),
            m_rules(signal, N, K, root_average_value_b, EXPECTED_ROOT_MEAN_SQUARE)
        ]
        lines = plot_section(plots)

    plt.figlegend(lines, LABELS, loc='upper center')

    plt.show()


if __name__ == '__main__':
    lab_2()
