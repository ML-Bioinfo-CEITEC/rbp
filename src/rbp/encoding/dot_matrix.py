import pandas as pd
from typing import Dict
import numpy as np


def dot_matrix(
        df: pd.DataFrame, alphabet: Dict[str, int] = {"AT": 1.0, "TA": 1.0, "GC": 1.0, "CG": 1.0}, dtype: str = "float32") -> np.array:
    """ create 2D dot matrix of watson-crick nucleotide interaction value between 2 sequences.

    The pandas df must be of 2 columns filled with pairs of nucleotide sequences [e.g. binding site - miRNA].

    Args:
        df: dataframe of sequences.
        alphabet: Dictionary mapping letters of alphabet to interaction value.
        dtype: np array type.
    Returns:
        3D numpy array of seq1 length x seq2 length x watson-crick interactions.
    """
    assert isinstance(df, pd.core.frame.DataFrame), "df must be pd.DataFrame"
    assert df.shape[1] == 2, "df must have 2 columns"

    X = df.copy()
    X.columns = ["seq1", "seq2"]

    len_seq1 = len(X.seq1.max())
    len_seq2 = len(X.seq2.max())
    samples = X.shape[0]

    dot_matrix = np.zeros((samples, len_seq1, len_seq2, 1),
                          dtype=dtype)  # create empty matrix

    # fill matrix with watson-crick interactions.
    for sample_index, sample in X.iterrows():
        for seq1_index, seq1_nt in enumerate(sample.seq1):
            for seq2_index, seq2_nt in enumerate(sample.seq2):
                dot_matrix[sample_index, seq1_index, seq2_index,
                           0] = alphabet.get(seq1_nt+seq2_nt, 0.0)
    return dot_matrix


if __name__ == "__main__":
    pass
