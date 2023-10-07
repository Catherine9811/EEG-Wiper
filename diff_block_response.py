

# Read the original file
file_path = "events/P4_cond3_down200_epoch_per_swipe_events.txt"

with open(file_path, 'r') as original_file:
    lines = original_file.readlines()

# Define the Hz
frequency = 200
# Define the events
events = {
    # 2000: No related white block signal found within 5s
    # 2001: L→R Response
    # 2002: R→L Response
}
swblockLR = 4
swblockRL = 8
wblockresp = 16

# Create a new list to store the modified data
new_lines = []

last_lr = 0.0
last_rl = 0.0

# Iterate through the original lines and add events as needed
event_counter = 1
for index, line in enumerate(lines):
    # Split the line into columns
    columns = line.strip().split('\t')
    if index == 0:
        new_lines.append("\t".join(columns))
        continue
    if int(float(columns[1])) == swblockRL:
        last_rl = float(columns[2])
    if int(float(columns[1])) == swblockLR:
        last_lr = float(columns[2])
    # Check if it's an event line
    if int(float(columns[1])) == wblockresp:
        # Add the event description
        event_number = 2000
        if min(float(columns[2]) - last_lr, float(columns[2]) - last_rl) < 5 * frequency:
            if float(columns[2]) - last_lr < 5 * frequency:
                event_number = 2001
            else:
                event_number = 2002
        new_lines.append("\t".join([
            str(event_counter),
            str(event_number),
            columns[2],
            columns[3]
        ]))
        event_counter += 1

    # Add the original data
    new_lines.append("\t".join([
        str(event_counter),
        columns[1],
        columns[2],
        columns[3]
    ]))

    event_counter += 1

# Save the modified data to a new file
new_file_path = "events_with_extension.txt"
with open(new_file_path, 'w') as new_file:
    # Write the modified lines
    new_file.write('\n'.join(new_lines))

print(f"Events added and saved to {new_file_path}")