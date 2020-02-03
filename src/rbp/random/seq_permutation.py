import random


def seq_permutation(seq: str, k: int = 1) -> str:
    """Shuffle a genomic sequence

    Args:
        seq (str): Sequence to be shuffled.
        k (int): For `k==1`, we shuffle individual characters. For `k>1`, we shuffle k-mers.

    Returns:
        Shuffled sequence.
    """
    if k == 1:
        return ''.join(random.sample(seq, len(seq)))
    else:
        kmers = [seq[i:(i + k)] for i in range(0, len(seq), k)]
        return ''.join(random.sample(kmers, len(kmers)))
