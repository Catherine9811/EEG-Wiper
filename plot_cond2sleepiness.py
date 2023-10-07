import matplotlib.pyplot as plt
import numpy as np

from reaction_loader import Loader

conditions = {
    "Regular Wiper": "events/P4_cond1_down200_epoch_per_swipe_events.txt",
    "Irregular Wiper": "events/P4_cond2_down200_epoch_per_swipe_events.txt",
    "Control": "events/P4_cond3_down200_epoch_per_swipe_events.txt"
}

variables = {
    "Reaction Time LR (s)": "reaction_time_lr_y",
    "Reaction Time RL (s)": "reaction_time_rl_y"
}

# Create subplots with the number of variables
num_variables = len(variables)
fig, axes = plt.subplots(1, num_variables, figsize=(14, 6))  # Adjust the figure size as needed


for idx, variable_name in enumerate(variables):
    target_arrays = []
    for condition_name in conditions:
        loader = Loader(conditions[condition_name])
        reaction_time_lr_x, reaction_time_lr_y, reaction_time_rl_x, reaction_time_rl_y, \
            sleepiness_x, sleepiness_y, sleepiness_reaction_y = loader.read()
        target_array = eval(variables[variable_name])
        target_arrays.append(target_array)

    # Combine the reaction time data into a single array
    combined_reaction_time = target_arrays

    # Create labels for the conditions (tests)
    labels = []
    for index, condition_name in enumerate(conditions):
        labels += [condition_name]

    # Create a box plot in the corresponding subplot
    axes[idx].boxplot(combined_reaction_time, labels=labels)
    axes[idx].set_title(f"{variable_name}")

# Customize plot labels and title
plt.suptitle("Reaction Time by Test Conditions")  # Add a common title

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()