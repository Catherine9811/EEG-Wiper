import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

from po_loader import Loader
from plot_rt2timebins import get_bins

if __name__ == "__main__":
    loader = Loader(channel_file_path="channels/P4_cond3_down200_block_events_lr_epoched_PO7&8_channels.txt",
                    event_file_path="events/P4_cond3_down200_block_events_lr_epoched_PO7&8_events.txt",
                    event_number_override=4)
    reaction_time, epoched_eeg = loader.read()

    epoch_processed = list(reaction_time.keys())
    reaction_processed = []

    for epoch in reaction_time:
        reaction_processed.append(reaction_time[epoch]["react"] - reaction_time[epoch]["appear"])

    # Plot Reaction Time
    plt.scatter(epoch_processed, reaction_processed, label="Reaction Time (s)", marker='x', s=20)
    # Fit with polyfit
    lr_b, lr_m = polyfit(epoch_processed, reaction_processed, 1)
    plt.plot(epoch_processed, lr_b + lr_m * np.array(epoch_processed), "-")
    # Customize plot labels and title
    plt.xlabel("Time (s)")
    plt.ylabel("Reaction Time (s)")
    plt.title("Reaction Time vs. Epoch")
    plt.legend()

    # Show the plot
    plt.show()

    data, label = get_bins(epoch_processed, reaction_processed, 12)
    plt.boxplot(data, labels=label)
    plt.xlabel("Epoch")
    plt.ylabel("Reaction Time (s)")
    plt.title("Reaction Time vs. Epoch")
    plt.show()

    # Show the plot
    plt.show()

    epoch_to_plot = 2

    index = np.logical_and(np.array(list(epoched_eeg[epoch_to_plot].keys())) <= 0,
                           np.array(list(epoched_eeg[epoch_to_plot].keys())) >= -reaction_processed[epoch_to_plot - 1])
    selected_timestamp = np.array(list(epoched_eeg[epoch_to_plot].keys()))[index]
    selected_eeg = np.array(list(epoched_eeg[epoch_to_plot].values()))[index]

    maximum_index = np.argmax(selected_eeg)
    maximum_timestamp = selected_timestamp[maximum_index]

    print(epoch_to_plot, maximum_timestamp)

    # Plot Reaction Time
    plt.plot(epoched_eeg[epoch_to_plot].keys(),
             epoched_eeg[epoch_to_plot].values(),
             label="EEG (uV)")

    plt.plot(selected_timestamp,
             selected_eeg,
             label="EEG (uV)")

    # Customize plot labels and title
    plt.xlabel("Time (s)")
    plt.ylabel("EEG (uV)")
    plt.title("EEG vs. Time")
    plt.legend()
    plt.show()