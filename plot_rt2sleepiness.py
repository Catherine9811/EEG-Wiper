import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

from reaction_loader import Loader

loader = Loader("events/P4_cond3_down200_epoch_per_swipe_events.txt")
reaction_time_lr_x, reaction_time_lr_y, reaction_time_rl_x, reaction_time_rl_y, \
    sleepiness_x, sleepiness_y, sleepiness_reaction_y = loader.read()

# Plot Sleepiness Score
plt.scatter(sleepiness_x, sleepiness_y, label="Sleepiness Score", marker='x', s=20)


# # Plot Sleepiness Reaction Time
# plt.scatter(sleepiness_x, sleepiness_reaction_y, label="Sleepiness Reaction Time", marker='o', s=20)

# Plot Reaction Time for swblockLR
plt.scatter(reaction_time_lr_x, reaction_time_lr_y, label="Reaction Time (swblockLR)", marker='s', s=20)

# Fit with polyfit
# lr_b, lr_m = polyfit(reaction_time_lr_x, reaction_time_lr_y, 1)
# plt.plot(reaction_time_lr_x, lr_b + lr_m * np.array(reaction_time_lr_x), "-")

# Plot Reaction Time for swblockRL
plt.scatter(reaction_time_rl_x, reaction_time_rl_y, label="Reaction Time (swblockRL)", marker='^', s=20)

# Fit with polyfit
# rl_b, rl_m = polyfit(reaction_time_rl_x, reaction_time_rl_y, 1)
# plt.plot(reaction_time_rl_x, rl_b + rl_m * np.array(reaction_time_rl_x), "-")

# Customize plot labels and title
plt.xlabel("Time (s)")
plt.ylabel("Reaction Time (s)")
plt.title("Reaction Time vs. Time")
plt.legend()

# Show the plot
plt.show()

# Create an array of time values for sleepiness
sleepiness_time = np.array(sleepiness_x)
# Create an array of sleepiness scores
sleepiness_scores = np.array(sleepiness_y)

# Interpolate sleepiness scores at the timestamps of swblockLR
interpolated_sleepiness_swblocklr = np.interp(reaction_time_lr_x, sleepiness_time, sleepiness_scores)

# Interpolate sleepiness scores at the timestamps of swblockRL
interpolated_sleepiness_swblockrl = np.interp(reaction_time_rl_x, sleepiness_time, sleepiness_scores)


# Plot the interpolated sleepiness scores against reaction time for swblockLR
plt.scatter(interpolated_sleepiness_swblocklr, reaction_time_lr_y, label="swblockLR", marker='s', s=20)

# Fit with polyfit
lr_b, lr_m = polyfit(interpolated_sleepiness_swblocklr, reaction_time_lr_y, 1)
plt.plot(interpolated_sleepiness_swblocklr, lr_b + lr_m * interpolated_sleepiness_swblocklr, "-")

# Plot the interpolated sleepiness scores against reaction time for swblockRL
plt.scatter(interpolated_sleepiness_swblockrl, reaction_time_rl_y, label="swblockRL", marker='^', s=20)

# Fit with polyfit
rl_b, rl_m = polyfit(interpolated_sleepiness_swblockrl, reaction_time_rl_y, 1)
plt.plot(interpolated_sleepiness_swblocklr, rl_b + rl_m * interpolated_sleepiness_swblocklr, "-")

# Customize plot labels and title
plt.xlabel("Interpolated Sleepiness Score")
plt.ylabel("Reaction Time (s)")
plt.title("Reaction Time vs. Interpolated Sleepiness Score")
plt.legend()

# Show the plot
plt.show()