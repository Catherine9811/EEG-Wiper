# Read the original file
file_path = "channels/P4_cond1_down200_epoch_per_swipe_channels.txt"

with open(file_path, 'r') as original_file:
    lines = original_file.readlines()

new_lines = []

for index, line in list(enumerate(lines)):
    # Split the line into columns
    columns = line.strip().split('\t')
    if index == 0:

        continue
    new_lines.append("\t".join(columns[1:]))

# Save the modified data to a new file
new_file_path = "channels_with_extension_noheader.txt"
with open(new_file_path, 'w') as new_file:
    # Write the modified lines
    new_file.write('\n'.join(new_lines))

print(f"Channels added and saved to {new_file_path}")