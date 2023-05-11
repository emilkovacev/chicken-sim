import math
import random
import matplotlib.pyplot as plt
import numpy as np

p_0 = 20 # sample initial population
days = 1000 # number of days

# Chicken population rates 
birth_rate = 0.2 # notice the difference between 0.1 and 0.2! (0.12 is wild)
road_crossing_attempt_rate = 0.6
road_crossing_success_rate = 0.8

cc = 10_000 # max number of chickens
cc_max = 100 # max variance in carrying capacity
r_max = 0.0015 # max difference in rate of chicken growth change
noise = 20

# Modeled population using the logistic function: https://en.wikipedia.org/wiki/Logistic_function
def population(days): 
    death_rate = road_crossing_attempt_rate * (1 - road_crossing_success_rate)
    r_temp = birth_rate - death_rate
    r_temp = r_temp + ((random.random() - 0.5) * r_max)
    cc_temp = cc + ((random.random() - 0.5) * cc_max)
    pop = cc_temp / (1 + ((cc_temp - p_0) / p_0) * (math.e ** (-1 * r_temp * days)))
    return pop + ((random.random() - 0.5) * noise)

population_over_time = [population(d) for d in range(1, days)]

fig, ax = plt.subplots()
ax.scatter([d for d in range(1, days)], population_over_time, marker='.')
ax.set_title("Chicken Population Over Time")
ax.set_xlabel("Time (days)")
ax.set_ylabel("Number of chickens")
plt.show()