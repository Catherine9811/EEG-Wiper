from tqdm import tqdm

# Read the original file
file_path = "channels/P4_cond1_down200_epoch_per_swipe_channels.txt"

with open(file_path, 'r') as original_file:
    lines = original_file.readlines()

# Define the Hz
frequency = 200
time_scale = 1e-3
# Define the events
expressions = [
    "Fp1-Fp2",
    "AF3-AF4",
    "AF7-AF8",
    "F7-F8",
    "F5-F6",
    "F3-F4",
    "F1-F2",
    "FT7-FT8",
    "FC5-FC6",
    "FC3-FC4",
    "FC1-FC2",
    "T7-T8",
    "C5-C6",
    "C3-C4",
    "C1-C2",
    "TP7-TP8",
    "CP5-CP6",
    "CP3-CP4",
    "CP1-CP2",
    "P9-P10",
    "P7-P8",
    "P5-P6",
    "P3-P4",
    "P1-P2",
    "PO7-PO8",
    "PO3-PO4",
    "O1-O2"
]

# Create a new list to store the modified data
new_lines = []
name_index = {}
# Iterate through the original lines and add events as needed
event_counter = 1
for index, line in tqdm(list(enumerate(lines))):
    # Split the line into columns
    columns = line.strip().split('\t')
    if index == 0:
        for count, name in enumerate(columns):
            name_index[name] = count

        # new_lines.append("\t".join(columns))
        continue
    for expression in expressions:
        exp_result = eval(expression, {
            key: float(columns[name_index[key]]) for key in name_index
        })
        for key_name in expression.split("-"):
            columns[name_index[key_name]] = str(exp_result)
    # Add the original data
    new_lines.append("\t".join(columns[1:]))

# Save the modified data to a new file
new_file_path = "channels_with_diff_replacement.txt"
with open(new_file_path, 'w') as new_file:
    # Write the modified lines
    new_file.write('\n'.join(new_lines))

print(f"Channels added and saved to {new_file_path}")