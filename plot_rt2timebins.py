import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

from reaction_loader import Loader


def get_bins(x, y, num_bins=7):
    bins = np.linspace(min(x), max(x), num_bins)
    bin_indices = np.digitize(x, bins)
    data_in_bins = [[] for _ in range(len(bins))]
    for i in range(len(bin_indices)):
        bin_index = bin_indices[i] - 1  # Subtract 1 to match list indexing
        data_in_bins[bin_index].append(y[i])
    box_data = [np.array(data) for data in data_in_bins[:-1]]
    labels = [f'{bins[i-1]:.0f}-{bins[i]:.0f}' for i in range(1, len(bins))]
    return box_data, labels

if __name__ == "__main__":
    loader = Loader("events/P4_cond3_down200_epoch_per_swipe_events.txt")
    reaction_time_lr_x, reaction_time_lr_y, reaction_time_rl_x, reaction_time_rl_y, \
        sleepiness_x, sleepiness_y, sleepiness_reaction_y = loader.read()

    # Create subplots with the number of variables
    num_variables = 2
    fig, axes = plt.subplots(1, num_variables, figsize=(14, 6))  # Adjust the figure size as needed


    data_lr, labels_lr = get_bins(reaction_time_lr_x, reaction_time_lr_y)
    data_rl, labels_rl = get_bins(reaction_time_rl_x, reaction_time_rl_y)

    # Create a box plot in the corresponding subplot
    axes[0].boxplot(data_lr, labels=labels_lr)
    axes[0].set_title(f"LR Reaction Time (s)")

    axes[1].boxplot(data_rl, labels=labels_rl)
    axes[1].set_title(f"RL Reaction Time (s)")

    # Customize plot labels and title
    # plt.xlabel("Time Bins (s)")
    # plt.ylabel("Reaction Time (s)")
    plt.suptitle("Reaction Time vs. Time Bins")
    plt.legend()

    # Show the plot
    plt.show()