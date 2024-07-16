"""
Usage Guide for rerandom Library
================================

This guide will walk you through the usage of the rerandom library for random
number generation and working with various distributions.

The rerandom library consists of two main classes:
1. EnhancedRandomGenerator: For basic random number generation.
2. DistributionGenerator: For generating samples from various statistical distributions.
"""

# Importing the necessary classes from the rerandom library
from rerandom import EnhancedRandomGenerator, DistributionGenerator

# EnhancedRandomGenerator Usage
# =============================

# Creating an instance of EnhancedRandomGenerator
rng = EnhancedRandomGenerator()

# Generating a random float number between 0 and 1
random_float = rng.generate()
print(f"Random float between 0 and 1: {random_float}")

# Generating a random integer between 1 and 10
random_int = rng.generate_int(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Setting a custom seed for reproducibility
rng.set_seed(42)
print(f"Seed set to: {rng.get_seed()}")

# Customizing the parameters of the Linear Congruential Generator (LCG)
rng.set_parameters(a=1664525, c=1013904223, m=2**32)
a, c, m = rng.get_parameters()
print(f"LCG parameters - a: {a}, c: {c}, m: {m}")

# DistributionGenerator Usage
# ===========================

# Creating an instance of DistributionGenerator
dist_gen = DistributionGenerator()

# Generating 5 samples from a uniform distribution
uniform_samples = dist_gen.random_uniform(5)
print(f"Uniform distribution samples: {uniform_samples}")

# Generating 6 samples from a normal distribution with mean 0 and standard deviation 1
normal_samples = dist_gen.random_normal(mean=0, std_dev=1, num_samples=6)
print(f"Normal distribution samples: {normal_samples}")

# Generating 5 samples from an exponential distribution with rate 1
exponential_samples = dist_gen.random_exponential(rate=1, num_samples=5)
print(f"Exponential distribution samples: {exponential_samples}")

# Generating 5 samples from a binomial distribution with 10 trials and probability of success 0.5
binomial_samples = dist_gen.random_binomial(n=10, p=0.5, num_samples=5)
print(f"Binomial distribution samples: {binomial_samples}")

# Generating 5 samples from a Poisson distribution with lambda 3
poisson_samples = dist_gen.random_poisson(lam=3, num_samples=5)
print(f"Poisson distribution samples: {poisson_samples}")

# Generating 5 samples from a geometric distribution with probability of success 0.5
geometric_samples = dist_gen.random_geometric(p=0.5, num_samples=5)
print(f"Geometric distribution samples: {geometric_samples}")

# Generating random choices from a list with specified probabilities
choices = ['apple', 'banana', 'cherry']
probabilities = [0.2, 0.5, 0.3]
random_choices = dist_gen.random_choice(choices, probabilities, num_samples=5)
print(f"Random choices from list: {random_choices}")
