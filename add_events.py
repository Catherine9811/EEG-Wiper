

# Read the original file
file_path = "events/P4_cond1_down200_epoch_per_swipe_events.txt"

with open(file_path, 'r') as original_file:
    lines = original_file.readlines()

# Define the Hz
frequency = 200
# Define the events
events = {
    1000: 0,
    1001: 250.5,
    1002: 866.84,
    1003: 1116.9
    # "Event 1: Wiper reached the L side",
    # "Event 1001: Wiper begins moving from L to R    +250.5ms",
    # "Event 1002: Wiper reached the R side           +866.84ms",
    # "Event 1003: Wiper begins moving from R to L    +1116.9ms"
}

# Create a new list to store the modified data
new_lines = []

# Iterate through the original lines and add events as needed
event_counter = 1
for index, line in enumerate(lines):
    # Split the line into columns
    columns = line.strip().split('\t')
    if index == 0:
        new_lines.append("\t".join(columns))
        continue
    # Check if it's an event line
    if int(float(columns[1])) == 1:
        # Add the event description
        for event_number in events:
            new_lines.append("\t".join([
                str(event_counter),
                str(event_number),
                str(float(columns[2]) + events[event_number] * frequency / 1000),
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