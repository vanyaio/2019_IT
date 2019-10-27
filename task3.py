import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].

    Returns:
        generator for batch indices [i, j, k]
    """
    dx = (N - 1) / (n_batches + 1/split_ratio)
    dy = (1/split_ratio) * dx
    i = 0
    j = dy
    k = dx + j
    for c in range(n_batches):
        yield (i, j, k)
        i += dx
        j += dx
        k += dx

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)

if __name__ == "__main__":
    main()
