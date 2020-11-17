from matplotlib import pyplot as plt


def plot_section(plots):
    lines = []
    for plot in plots:
        lines.append(plt.plot(*plot)[0])
    return lines