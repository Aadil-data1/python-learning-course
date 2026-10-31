import numpy as np

def bootstrap_ci(data, n_bootstrap=10000, confidence=0.95, random_state=42):

    values = np.asarray(data, dtype=float)
    values = values[np.isfinite(values)]

    if len(values) == 0:
        raise ValueError("Data must contain at least one valid number.")

    rng = np.random.default_rng(random_state)

    # Generate bootstrap samples
    bootstrap_samples = rng.choice(
        values,
        size=(n_bootstrap, len(values)),
        replace=True
    )

    # Calculate the mean of every bootstrap sample
    bootstrap_means = bootstrap_samples.mean(axis=1)

    # Calculate the confidence interval
    alpha = 1 - confidence

    lower = np.quantile(bootstrap_means, alpha / 2)
    upper = np.quantile(bootstrap_means, 1 - alpha / 2)

    return {
        "sample_mean": values.mean(),
        "lower_bound": lower,
        "upper_bound": upper
    }


salaries = np.array([
    35000, 40000, 42000, 45000, 46000,
    48000, 50000, 52000, 55000, 60000
])

result = bootstrap_ci(salaries)

print(result)