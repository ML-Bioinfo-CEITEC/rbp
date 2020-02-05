from rbp.utils.random_intervals import gen_random_intervals as gen_random
from rbp.utils.bed2fa import get_fasta as get_fasta
import pybedtools


def test_bedtools():
    """
    pybedtools test.
    """
    a = pybedtools.example_bedtool("a.bed")
    b = pybedtools.example_bedtool("b.bed")
    assert a.intersect(b)


def test_random_intervals():
    # reference = "tests/data/test_reference.fa"
    random_bed = gen_random(sample_size=10, interval_size=5, reference="hg19", df=True)
    # print(random_bed)
    assert type(random_bed)


if __name__ == "__main__":
    test_bedtools()
    test_random_intervals()

