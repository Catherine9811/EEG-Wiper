import numpy as np

# Read the original file
file_path = "test.txt"

content = np.loadtxt(file_path)

content = content.transpose()

# Save the modified data to a new file
new_file_path = "test_transposed.txt"
np.savetxt(new_file_path, content, fmt="%.4f", delimiter="\t")

print(f"Channels added and saved to {new_file_path}")