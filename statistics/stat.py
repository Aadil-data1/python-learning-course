import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)    # 42 = seed

# Create a hypothetical population
population = rng.normal(
    loc=50000,            # loc is the mean, the value the data is centered around.
    scale=12000,          # scale is the standard deviation, which measures how far values typically stray from the center
    size=100000           # size is the number of values to generate
)

# True population average
population_mean = population.mean()

# Draw one sample
sample_size = 40

sample = rng.choice(
    population,
    size=sample_size,
    replace=False               # no value can be picked twice 
)

sample_mean = sample.mean()
sample_std = sample.std(ddof=1)      # ddof=1 divides by n − 1 instead of n

standard_error = sample_std / np.sqrt(sample_size)

print("Population mean:", population_mean)
print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_std)
print("Estimated standard error:", standard_error)

# Repeat the sampling process 5,000 times
sample_means = []

for _ in range(5000):
    new_sample = rng.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_means.append(new_sample.mean())

# Visualise the distribution of sample means
plt.hist(sample_means, bins=40, edgecolor="black")

plt.axvline(
    population_mean,
    linestyle="--",
    label="True population mean"
)

plt.xlabel("Sample average salary")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means")
plt.legend()

plt.show()