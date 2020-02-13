import pandas as pd
from pybedtools import BedTool


def gen_random_intervals(
    sample_size: int, interval_size: int, reference: str, seed: int = 1789
):
    """ Return random gemomic intervals as BED file

    This functions integrates pyBedTools (https://daler.github.io/pybedtools/).

    Args:
        sample_size: generate N random intervals.
        interval_size: size of the interval.
        reference: path to reference genome.
        seed: random seed for reproducibility.

    Returns:
        BED like pd.DataFrame with columns chr,start,end,name,score,strand.
    """
    x = BedTool()
    y = x.random(n=sample_size, l=interval_size, genome=reference, seed=seed)
    return pd.read_csv(
        y.fn, sep="\t", names=["chr", "start", "end", "name", "score", "strand"]
    )


if __name__ == "__main__":
    pass
