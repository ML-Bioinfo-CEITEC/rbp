import numpy as np
import pandas as pd
from typing import Union, Dict, Tuple


CHR_LENGTHS_Homo_sapiens_GRCh38 = {'1': 248956422,
                                   '2': 242193529,
                                   '3': 198295559,
                                   '4': 190214555,
                                   '5': 181538259,
                                   '6': 170805979,
                                   '7': 159345973,
                                   '8': 145138636,
                                   '9': 138394717,
                                   '10': 133797422,
                                   '11': 135086622,
                                   '12': 133275309,
                                   '13': 114364328,
                                   '14': 107043718,
                                   '15': 101991189,
                                   '16': 90338345,
                                   '17': 83257441,
                                   '18': 80373285,
                                   '19': 58617616,
                                   '20': 64444167,
                                   '21': 46709983,
                                   '22': 50818468,
                                   'X': 156040895,
                                   'Y': 57227415,
                                   'MT': 16569}
CHR_LENGTHS_Homo_sapiens_GRCh38_SERIES = pd.Series(CHR_LENGTHS_Homo_sapiens_GRCh38)


def random_genomic_position(chrom_lengths: Union[Dict[str, int], pd.Series] = CHR_LENGTHS_Homo_sapiens_GRCh38_SERIES) -> Tuple[str, int]:
    """Returns a random genomic position

    The chomosome is generated from a multinomial distribution with chr. lengths used as weights. The generated position is 1-based.

    Args:
        chrom_lengths: Either Dict of pd.Series with chromosomes' lengths.

    Returns:
        A tuple of chromosome and a 1-based position on this chromosome.
    """

    chrom_lengths = pd.Series(chrom_lengths) if isinstance(chrom_lengths, dict) else chrom_lengths
    
    chrom = _random_chr(chrom_lengths)
    chrom_len = chrom_lengths[chrom]
    pos = np.random.randint(chrom_len) + 1

    return chrom, pos


def random_genomic_interval(interval_length: int,
                            chrom_lengths: Union[Dict[str, int], pd.Series] = CHR_LENGTHS_Homo_sapiens_GRCh38_SERIES) -> Tuple[str, int, int]:
    """Returns a random genomic interval

    Args:
        interval_length (int): Length of interval to be generated.
        chrom_lengths: Either Dict of pd.Series with chromosomes' lengths.

    Returns:
        A tuple of chromosome, start and end (of interval).
    """
    chrom_lengths = pd.Series(chrom_lengths) if isinstance(chrom_lengths, dict) else chrom_lengths
    chrom_lengths = (chrom_lengths - interval_length + 1).clip(0)

    chrom, start = random_genomic_position(chrom_lengths)
    end = start + interval_length - 1
    
    return chrom, start, end


def _random_chr(chrom_lengths: pd.Series):
    chrom_names = chrom_lengths.index.values
    chrom_probs = chrom_lengths / chrom_lengths.sum()
    random_chrom_index = np.argwhere(np.random.multinomial(1, chrom_probs))[0][0]

    return chrom_names[random_chrom_index]
