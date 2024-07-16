import numpy as np
from .rng import EnhancedRandomGenerator


class DistributionGenerator:
    def __init__(self):
        self.rng = EnhancedRandomGenerator()

    def random_uniform(self, num_samples):
        return [self.rng.generate() for _ in range(num_samples)]

    def random_normal(self, mean, std_dev, num_samples):
        results = []
        for _ in range(num_samples // 2):
            u1 = self.rng.generate()
            u2 = self.rng.generate()
            z1 = (-2 * np.log(u1)) ** 0.5 * np.cos(2 * np.pi * u2)
            z2 = (-2 * np.log(u1)) ** 0.5 * np.sin(2 * np.pi * u2)
            results.append(z1 * std_dev + mean)
            results.append(z2 * std_dev + mean)
        if num_samples % 2 == 1:
            results.append(z1 * std_dev + mean)
        return results

    def random_exponential(self, rate, num_samples):
        results = []
        for _ in range(num_samples):
            u = self.rng.generate()
            results.append(-np.log(u) / rate)
        return results

    def random_binomial(self, n, p, num_samples):
        results = []
        for _ in range(num_samples):
            count = 0
            for _ in range(n):
                if self.rng.generate() < p:
                    count += 1
            results.append(count)
        return results

    def random_poisson(self, lam, num_samples):
        results = []
        for _ in range(num_samples):
            l = np.exp(-lam)
            k = 0
            p = 1
            while p > l:
                k += 1
                p *= self.rng.generate()
            results.append(k - 1)
        return results

    def random_geometric(self, p, num_samples):
        results = []
        for _ in range(num_samples):
            results.append(int(np.ceil(np.log(1 - self.rng.generate()) / np.log(1 - p))))
        return results

    def random_choice(self, choices, probabilities, num_samples):
        results = []
        cumulative_probs = np.cumsum(probabilities)
        for _ in range(num_samples):
            r = self.rng.generate()
            for i, cp in enumerate(cumulative_probs):
                if r < cp:
                    results.append(choices[i])
                    break
        return results
