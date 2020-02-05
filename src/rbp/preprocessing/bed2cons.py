import pyBigWig
import pandas as pd
from typing import Union


def get_conservation(intervals: Union[str, pd.DataFrame], reference: str):
    """ Return conservation track for each input interval.

    This functions integrates pyBigWig (https://github.com/deeptools/pyBigWig).

    Args:
        intervals: BED file path or pd.DataFrame like obj.
        reference: path to reference genome.

    Returns:
        A pd.DataFrame of bitwise conservation for each input interval.
    """
    def extract_cons(row, bw_obj):
        cons_score = bw_obj.values(row.chr, row.start, row.end)
        return ",".join(map(str, cons_score))

    if isinstance(intervals, str):
        assert intervals.endswith('bed'), 'required BED-6 file as input file'
        field_name = {"chr": str, "start": int, "end": int,
                      "name": str, "score": str, "strand": str}

        intervals_df = pd.read_csv(
            intervals, sep="\t", names=field_name.keys(), dtype=field_name,
        )
    elif isinstance(tst, pd.core.frame.DataFrame) == True:
        pass
    else:
        raise TypeError("Input must be BED file or Pandas DataFrame")

    bw = pyBigWig.open(reference)  # load refernece as bw obj
    cons_series = intervals_df.apply(
        extract_cons, bw_obj=bw, axis=1
    )  # apply extract_cons function to each row

    return pd.DataFrame(cons_series, columns=["cons_score"])


if __name__ == "__main__":
    print(get_conservation(
        intervals="bed_cons_test.bed", reference='http://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP7way/hg38.phyloP7way.bw'))
