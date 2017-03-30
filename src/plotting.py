import matplotlib.pyplot as plt


def individual_tones(series, color, y_lab, figsize=(14, 8)):
    plt.figure(figsize=(figsize))
    plt.plot(series, color=color)
    plt.title(title, fontsize=18, fontweight='bold')
    plt.xlabel("Year", fontsize=14, fontweight='bold')
    plt.ylabel(y_lab, fontsize=14, fontweight='bold')
