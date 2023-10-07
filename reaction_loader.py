class Loader:
    def __init__(self, file_path="events/P4_cond3_down200_epoch_per_swipe_events.txt"):
        # Read the original file
        self.file_path = file_path
        # Define the Hz
        self.events = {
            "swblockLR": 4,
            "swblockRL": 8,
            "wblockresp": 16,
            "ssleep": 32
        }

        self.frequency = 200
        self.sleepiness_min = 60
        self.sleepiness_max = 220

    def read(self):
        with open(self.file_path, 'r') as original_file:
            lines = original_file.readlines()

        reaction_time_lr_x = []
        reaction_time_lr_y = []

        reaction_time_rl_x = []
        reaction_time_rl_y = []

        sleepiness_x = []
        sleepiness_y = []

        sleepiness_reaction_y = []

        sleepiness_last_reaction = 0.0
        block_lr_last_reaction = 0.0
        block_rl_last_reaction = 0.0

        # Iterate through the original lines and check event pairs
        for index, line in enumerate(lines):
            # Split the line into columns
            columns = line.strip().split('\t')
            if index == 0:
                continue
            if int(float(columns[1])) == self.events["ssleep"]:  # Sleepiness questionare
                sleepiness_last_reaction = float(columns[2]) / self.frequency  # Time in s
                continue

            if int(float(columns[1])) == self.events["swblockLR"]:  # Blocks
                block_lr_last_reaction = float(columns[2]) / self.frequency  # Time in s
                continue
            if int(float(columns[1])) == self.events["swblockRL"]:  # Blocks
                block_rl_last_reaction = float(columns[2]) / self.frequency  # Time in s
                continue
            # Check if it's an sleepiness questionaire line
            if self.sleepiness_min <= int(float(columns[1])) <= self.sleepiness_max:
                onset = float(columns[2]) / self.frequency  # Time in ms
                score = (int(float(columns[1])) - self.sleepiness_min) / (self.sleepiness_max - self.sleepiness_min)
                sleepiness_y.append(score)
                sleepiness_x.append(onset)
                reaction = onset - sleepiness_last_reaction
                sleepiness_reaction_y.append(reaction)
                continue

            if int(float(columns[1])) == self.events["wblockresp"]:
                onset = float(columns[2]) / self.frequency  # Time in ms
                if min(onset - block_lr_last_reaction, onset - block_rl_last_reaction) >= 5:
                    continue
                if onset - block_lr_last_reaction <= onset - block_rl_last_reaction:
                    reaction_time_lr_x.append(onset)
                    reaction_time_lr_y.append(onset - block_lr_last_reaction)
                else:
                    reaction_time_rl_x.append(onset)
                    reaction_time_rl_y.append(onset - block_rl_last_reaction)
        return reaction_time_lr_x, reaction_time_lr_y, reaction_time_rl_x, reaction_time_rl_y, \
               sleepiness_x, sleepiness_y, sleepiness_reaction_y