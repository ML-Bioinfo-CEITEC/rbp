import numpy as np
import pandas as pd
from collections import defaultdict
from typing import Iterable, Optional


class MarkovModel:

    """ Markov chanin model for genomic sequences (based on kmers of the length `k`)

    Example:

        m = MarkovModel(k=2)
        m.fit(['ACCG', 'GAACAT', 'CTAGAAA', 'AGGCCCG', 'CAGATAC'])
        m.predict(10)   # output a random sequence of 10 nucleotides

    """

    def __init__(self, k: int = 3):
        """ Initialize the model

        Args:
            k: the length of kmers to be used.
        """

        self.k = k
        self.trained = False

    def fit(self, seqs: Iterable[str], only_valid_seqs: bool = True):
        """ Train the model over the list of genomic sequences

        Args:
            seqs: genomic sequences
            only_valid_seqs: if True, sequences with letters other than A, C, G, or T, are ommitted
        """

        kmers = defaultdict(int)
        kmer_pairs = defaultdict(int)
        N = 0
        k = self.k

        for s in seqs:
            if only_valid_seqs and not set(s).issubset({'A', 'C', 'G', 'T'}):  # sequences of A,C,T,G letters only
                continue
            prev_kmer = None
            for i in range(0, len(s), k):
                curr_kmer = s[i:(i + k)]
                if len(curr_kmer) == k:  # if not last partial kmer
                    N += 1
                    kmers[curr_kmer] += 1
                    if prev_kmer is not None:  # if not the first kmer
                        kmer_pairs[(prev_kmer, curr_kmer)] += 1
                prev_kmer = curr_kmer

        self.N = N
        self.kmers = pd.Series(kmers)
        self.kmer_pairs = pd.Series(kmer_pairs)
        self.kmer_pairs.index.names = ['prev', 'curr']
        self.trained = True

    def predict(self, length: int, seed: str = ''):
        """ Generate a random sequence

        Based on kmer counts, it returns a random sequence of the given length

        Args:
            length: length of the sequence to be generated
            seed: beginning of the sequence (default is an empty string)

        Returns:
            string of length `length`
        """

        assert self.trained, "The model must be trained before calling `predict` method."

        s = seed
        if len(s) >= self.k:
            prev_kmer = s[-self.k:]
        else:
            prev_kmer = relative_multinomial(self.kmers, self.N)[0]
            s = s + prev_kmer

        while len(s) < length:
            possible_curr = self.kmer_pairs[self.kmer_pairs.index.get_level_values('prev') == prev_kmer]
            if len(possible_curr) == 0:
                curr_kmer = relative_multinomial(self.kmers, self.N)[0]
            else:
                curr_kmer = relative_multinomial(possible_curr)[1].values[0]
            s = s + curr_kmer
            prev_kmer = curr_kmer

        return s[:length]


def relative_multinomial(counts: pd.Series, total: Optional[int] = None):
    """Helper function drawing one sample from a multinomial distribution

    Args:
        counts: Labels are supposed to be index of counts. Relative probabilities are values of counts (they are not expected to sum to one.)
        total: optional sum of `counts`, if None, it is calculated from `counts`.
    """

    if total is None:
        total = counts.sum()
    return counts.index[np.argwhere(np.random.multinomial(1, counts / total) == 1)][0]
