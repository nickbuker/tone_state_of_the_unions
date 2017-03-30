import matplotlib.pyplot as plt
import numpy as np


def individual_tones(df, tone, colors, title, y_lab, figsize=(12, 6)):
    plt.figure(figsize=(figsize))
    plt.plot(df[tone], color=colors[tone], marker='o', label=y_lab)
    plt.title(title, fontsize=18, fontweight='bold')
    plt.xlabel("Year", fontsize=14, fontweight='bold')
    plt.ylabel(y_lab, fontsize=14, fontweight='bold')
    plt.ylim(0, 0.8)
    plt.axhline(np.mean(df[tone]), color='k', linestyle=':', label='Mean')
    plt.legend(fontsize=14)


def multiple_tones(df, tone_labels, colors, title,
                   figsize=(12, 6), y_lim=(-0.1, 1)):
    plt.figure(figsize=(figsize))
    for i, tone in enumerate(tone_labels):
        plt.plot(df[tone], color=colors[tone], marker='o', label=tone)
    plt.title(title, fontsize=18, fontweight='bold')
    plt.xlabel("Year", fontsize=14, fontweight='bold')
    plt.ylabel("Score", fontsize=14, fontweight='bold')
    plt.ylim(y_lim)
    plt.legend(fontsize=14)


def stacked_bar(df, colors, figsize=(12, 8), y_lim=(0, 2.5)):
    plt.figure(figsize=figsize)
    bottom = 0
    for i, col in enumerate(df.columns):
        plt.bar(df.index, df[col], bottom=bottom, alpha=0.8,
                color=colors[col], label=col)
        bottom += df[col]
    plt.legend(fontsize=10)
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Tone Score', fontsize=16)
    plt.title('Stacked Bar Graph', fontsize=18, fontweight='bold')
