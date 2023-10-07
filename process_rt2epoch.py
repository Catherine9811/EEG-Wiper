import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

from po_loader import Loader

def norm(x):
    return list(x) / np.max(np.abs(list(x)))

loader = Loader(channel_file_path="channels/P4_cond3_down200_block_events_lr_epoched_PO7&8_channels.txt",
                event_file_path="events/P4_cond3_down200_block_events_lr_epoched_PO7&8_events.txt",
                event_number_override=4)
reaction_time, epoched_eeg = loader.read()

epoch_processed = list(reaction_time.keys())
reaction_processed = []

for epoch in reaction_time:
    reaction_processed.append(reaction_time[epoch]["react"] - reaction_time[epoch]["appear"])

decision_processed = []

# for epoch_to_plot in epoch_processed:
#     index = np.logical_and(np.array(list(epoched_eeg[epoch_to_plot].keys())) <= 0,
#                            np.array(list(epoched_eeg[epoch_to_plot].keys())) >= -reaction_processed[epoch_to_plot - 1])
#     selected_timestamp = np.array(list(epoched_eeg[epoch_to_plot].keys()))[index]
#     selected_eeg = np.array(list(epoched_eeg[epoch_to_plot].values()))[index]
#     maximum_index = np.argmax(selected_eeg)
#     maximum_timestamp = selected_timestamp[maximum_index]
#
#     print(epoch_to_plot, maximum_timestamp)
#     decision_processed.append(-maximum_timestamp)
#
# plt.plot(epoch_processed,
#          decision_processed,
#          label="Decision Time (s)")
#
# # Customize plot labels and title
# plt.xlabel("Epoch")
# plt.ylabel("Decision Time (s)")
# plt.title("Decision Time vs. Epoch")
# plt.legend()
# plt.show()

window_size = 10
stride = 3

index = np.logical_and(np.array(list(epoched_eeg[1].keys())) <= 0,
                       np.array(list(epoched_eeg[1].keys())) >= -0.5)
timestamps = np.array(list(epoched_eeg[1].keys()))[index]
averaged_eeg = np.array([norm(epoched_eeg[epoch].values()) for epoch in epoch_processed]).mean(axis=0)[index]

plt.plot(timestamps, averaged_eeg, label="All")

for slice_num in range(0, len(epoch_processed), window_size * stride):
    plt.plot(timestamps,
             np.array([norm(epoched_eeg[epoch].values())
                       for epoch in epoch_processed[slice_num:slice_num+window_size]]).mean(axis=0)[index],
             label=f"{slice_num}-{slice_num+window_size} Epochs")

plt.legend()
plt.show()
