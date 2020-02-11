import pytest
import pandas as pd
import numpy as np
from rbp.encoding import dot_matrix
from numpy.testing import assert_array_equal


def test_dot_matrix():
    df = pd.DataFrame(
        {"seq_a": ["ACGTCGTGCGTGCA"], "seq_b": ["TGCACGCACGACGT"]}
    )
    assert df.shape == (1, 2)

    expected_output = np.array([[[[0.], [0.]], [[0.], [1.]], [[1.], [0.]]]])

    actual_output = dot_matrix(df)
    assert actual_output.shape == (1, 14, 14, 1)
    assert_array_equal(expected_output, actual_output)
