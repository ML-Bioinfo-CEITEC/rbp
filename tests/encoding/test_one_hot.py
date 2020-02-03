import pytest
import numpy as np
from numpy.testing import assert_array_equal
from rbp.encoding import one_hot_encoding, one_hot_decoding


def test_one_hot_encoding():
    X = one_hot_encoding(['AACT', 'CCTG'])
    assert X.shape == (2, 4, 4)
    assert (X.sum(axis=2) == 1).all()

    expected_output = np.array([[[True, False, False, False],
                                 [True, False, False, False],
                                 [False, True, False, False],
                                 [False, False, True, False]]], dtype=bool)
    actual_output = one_hot_encoding(['AACT'])
    assert actual_output.shape == (1, 4, 4)
    assert_array_equal(expected_output, actual_output)


def test_one_hot_decoding():
    X = one_hot_encoding(['AACT', 'CCTG'])
    assert one_hot_decoding(X) == ['AACT', 'CCTG']


def test_one_hot_encoding_not_equal_length():
    with pytest.raises(Exception) as e:
        one_hot_encoding(['AACT', 'CC'])
    assert str(e.value) == "Sequences must be of the same length."
