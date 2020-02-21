import pandas as pd
import numpy as np
from rbp.encoding import dot_matrix
from numpy.testing import assert_array_equal


def test_dot_matrix():
    df = pd.DataFrame({"seq_a": ["ACGT"], "seq_b": ["TG"]})
    assert df.shape == (1, 2)

    expected_output = np.array(
        [[[[1.], [0.]], [[0.], [1.]], [[0.], [0.]], [[0.], [0.]]]], dtype='float32')

    actual_output = dot_matrix(df)
    assert_array_equal(expected_output, actual_output)
