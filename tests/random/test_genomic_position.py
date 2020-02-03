import pandas as pd
from rbp.random import random_genomic_position


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
