import pandas as pd
from pandas.testing import assert_frame_equal
import io
from rbp.random import gen_random_intervals


def test_gen_random_intervals():
    df = gen_random_intervals(
        sample_size=2, interval_size=100, reference='hg19', seed=1789
    )
    expected_intervals = io.StringIO(
        """chr3\t7191430\t7191530\t1\t100\t+\nchrX\t134026587\t134026687\t2\t100\t-""")
    expected_output = pd.read_csv(
        expected_intervals,
        sep="\t",
        names=["chr", "start", "end", "name", "score", "strand"])
    assert_frame_equal(df, expected_output)
