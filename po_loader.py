class Loader:
    def __init__(self,
                 channel_file_path="channels/P4_cond3_down200_block_events_lr_epoched_PO7&8_channels.txt",
                 event_file_path="events/P4_cond3_down200_block_events_lr_epoched_PO7&8_events.txt",
                 event_number_override=4
                 ):
        # Read the original file
        self.channel_file_path = channel_file_path
        self.event_file_path = event_file_path
        # Define the Hz
        self.events = {
            event_number_override: "appear",
            16: "react"
        }
        self.channels = {
            "PO7": 1,
            "PO8": 2
        }
        self.frequency = 200
        self.channel_resolution = 1e-3

    def read(self):
        # Read event file for the recorded reaction time
        with open(self.event_file_path, 'r') as original_file:
            lines = original_file.readlines()

        # Format - epoch: {"appear": 0.0 ms, "react": 0.0 ms}
        reaction_time = {}

        # Iterate through the original lines and check event pairs
        for index, line in enumerate(lines):
            # Split the line into columns
            columns = line.strip().split('\t')
            if index == 0:
                continue
            type_num = int(float(columns[2]))
            if type_num in self.events.keys():  # Contained in events
                epoch_num = int(float(columns[7]))
                latency_num = float(columns[3])
                if epoch_num not in reaction_time:
                    reaction_time[epoch_num] = {"appear": 0.0, "react": 0.0}
                reaction_time[epoch_num][self.events[type_num]] = latency_num / self.frequency

        # Read channel file for the recorded EEG
        with open(self.channel_file_path, 'r') as original_file:
            lines = original_file.readlines()

        # Format - epoch: [{time (ms): voltage (uV)}]
        epoched_eeg = {}
        current_epoch_num = 0
        current_epoch_timestamp = 0

        # Iterate through the original lines and check event pairs
        for index, line in enumerate(lines):
            # Split the line into columns
            columns = line.strip().split('\t')
            if index == 0:
                continue
            epoch_timestamp = float(columns[0]) * self.channel_resolution
            eeg = float(columns[self.channels["PO7"]]) - float(columns[self.channels["PO8"]])
            if epoch_timestamp < current_epoch_timestamp:
                current_epoch_num += 1
            current_epoch_timestamp = epoch_timestamp
            if current_epoch_num not in epoched_eeg:
                epoched_eeg[current_epoch_num] = {}
            epoched_eeg[current_epoch_num][epoch_timestamp] = eeg

        return reaction_time, epoched_eeg