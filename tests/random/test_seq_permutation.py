from collections import Counter
from rbp.random import seq_permutation


def test_seq_shuffle():
    s = "ACTTGCTAGCTACCCGATCGACCCCCCGAACGACTCGAGCAGCCCCCAAGCAGCTTGCAGCGTCGAGCAGT"
    t = seq_permutation(s)

    assert Counter(s) == Counter(t)


def test_kmer_shuffle():
    s = "ALPHABET"
    t = seq_permutation(s, 3)

    assert "ALP" in t
    assert "HAB" in t
    assert "ET" in t
    assert Counter(s) == Counter(t)
