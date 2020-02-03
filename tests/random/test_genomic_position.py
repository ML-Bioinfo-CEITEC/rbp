import pandas as pd
from rbp.random import random_genomic_position, random_genomic_interval


MINI_GENOME = {'1': 5, '2': 3}
MINI_GENOME_SERIES = pd.Series(MINI_GENOME)


def test_genomic_position():
    thousand_positions = [random_genomic_position(MINI_GENOME_SERIES) for _ in range(1000)]
    thousand_positions_df = pd.DataFrame(thousand_positions, columns=['chr', 'pos'])

    assert thousand_positions_df.chr.isin(['1', '2']).all()
    assert (thousand_positions_df.pos >= 1).all
    assert (thousand_positions_df.pos <= 5).all

    ten_positions = [random_genomic_position(MINI_GENOME) for _ in range(10)]
    assert len(ten_positions) == 10


def test_genomic_interval():
    hundered_intervals = [random_genomic_interval(3, MINI_GENOME_SERIES) for _ in range(100)]
    hundered_intervals_df = pd.DataFrame(hundered_intervals, columns=['chr', 'start', 'end'])
    assert all(hundered_intervals_df.end - hundered_intervals_df.start + 1 == 3)

    ten_intervals = [random_genomic_interval(4, MINI_GENOME_SERIES) for _ in range(10)]
    ten_intervals_df = pd.DataFrame(ten_intervals, columns=['chr', 'start', 'end'])
    assert all(ten_intervals_df.chr == '1')
