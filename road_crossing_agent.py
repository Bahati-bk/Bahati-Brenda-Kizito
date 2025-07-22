import numpy as np
import random

# Environment settings
grid_size = 5
actions = ['left', 'right', 'forward']
q_table = np.zeros((grid_size, len(actions)))  # One row per Y-position

# Hyperparameters
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 1000

# Simulated car positions
def is_car(position):
    return random.random() < 0.1  # 10% chance car is in the way

# Training loop
for episode in range(episodes):
    position = 0  # Agent starts at row 0
    done = False

    while not done:
        if random.random() < epsilon:
            action_index = random.randint(0, 2)  # explore
        else:
            action_index = np.argmax(q_table[position])  # exploit

        action = actions[action_index]

        # Simulate environment response
        new_position = position
        if action == 'forward':
            new_position += 1
        elif action == 'left' or action == 'right':
            pass  # ignore for now, could add lateral position

        # Calculate reward
        if new_position >= grid_size:
            reward = 100
            done = True
        elif is_car(new_position):
            reward = -100
            done = True
        else:
            reward = -1  # small penalty to encourage fewer steps

        # Q-learning update
        q_table[position, action_index] = q_table[position, action_index] + alpha * (
            reward + gamma * np.max(q_table[new_position if new_position < grid_size else position]) - q_table[position, action_index])

        position = new_position

# Display learned Q-values
print("Q-table after training:\n", q_table)
