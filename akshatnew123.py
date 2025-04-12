import random
import matplotlib.pyplot as plt
from collections import Counter

# Dice roll 10 times
results = [random.randint(1, 6) for _ in range(10)]

# Count frequency of each number
count = Counter(results)

# Plot
plt.bar(count.keys(), count.values(), color='skyblue')
plt.xlabel('Dice Number')
plt.ylabel('Frequency')
plt.title('Dice Roll Simulator (10 Rolls)')
plt.grid(True)
plt.show()
