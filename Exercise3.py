import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (k-j) = split_ratio*(j-i). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].

    Returns:
        generator for batch indices [i, j, k]
    """
    length_jk=round((N-1)/(n_batches+1/split_ratio))
    length_ij=round(length_jk/split_ratio)
    inds = np.array([0, length_ij, length_ij+length_jk])
    yield inds
    for i in range(1,n_batches):
        # todo: move forward batch
        # calculate new indices
        if (i==n_batches-1) and (inds[2]+length_jk!=N-1):
            inds[2]=N-1
            inds[0]+=length_jk
            inds[1]=inds[0]+(inds[2]-inds[0])/(1+split_ratio)
        else:
            inds+=length_jk
        yield inds

def main():
    for inds in get_indices(100, 20, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()