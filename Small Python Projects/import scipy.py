import scipy.stats as stats

# Given values
sample_mean = 38.3
hypothesized_mean = 38.25
sample_std_dev = 0.4
sample_size = 75

# Calculate the z-score
z_score = (sample_mean - hypothesized_mean) / (sample_std_dev / (sample_size ** 0.5))

# Calculate the p-value for one-tailed test
p_value = 1 - stats.norm.cdf(z_score)

# Convert the p-value to a confidence level
confidence_level = (1 - p_value) * 100

# Round the confidence level to two decimal places
confidence_level_rounded = round(confidence_level, 2)

print(confidence_level)