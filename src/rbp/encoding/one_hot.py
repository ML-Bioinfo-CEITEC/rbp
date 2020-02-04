import numpy as np
from typing import Iterable, Dict, List


ACTG = {'A': 0, 'C': 1, 'T': 2, 'G': 3}


def one_hot_encoding(seq_list: Iterable[str], alphabet: Dict[str, int] = ACTG) -> np.array:
    """One-hot encoding of a list of genomic sequences

    The sequnces must have the same length. They are encoded into a boolean numpy array.
    `X[i,j,k]` is True if the `j`th character of the sequence `i` is `k`letter in the alphabet.

    Args:
        seq_list: List of sequences. All must have the same length.
        alphabet: Dictionary mapping letters of alphabet to index.

    Returns:
        3D numpy array (number of sequences x length of one sequence x sixe of the alphabet)
    """

    n = len(seq_list)
    m = len(seq_list[0])
    k = len(alphabet.keys())
    seq_array = np.zeros((n, m, k), dtype=np.bool)

    for i in range(n):
        assert len(seq_list[i]) == m, "Sequences must be of the same length."
        for j in range(m):
            seq_array[i, j, alphabet[seq_list[i][j]]] = True
    
    return seq_array


def one_hot_decoding(seq_array: np.array, alphabet: Dict[str, int] = ACTG) -> List[str]:
    """One-hot decoding

    The function decodes boolean numpy array, ussually the output of `one_hot_encoding`.

    Args:
        seq_list: 3D numpy array (number of sequences x length x sixe of the alphabet).
        alphabet: Dictionary mapping letters of alphabet to index.

    Returns:
        List of genomic sequences.
    """

    alphabet_array = np.array(list(alphabet.keys()), dtype=str)
    seq_list = []
    n, m, _ = seq_array.shape
 
    for i in range(n):
        s = ''
        for j in range(m):
            c = alphabet_array[seq_array[i][j]][0]
            s += c
        seq_list.append(s)

    return seq_list
