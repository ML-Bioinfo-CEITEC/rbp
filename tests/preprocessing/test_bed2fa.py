import pytest
import os
import pandas as pd
import io
from rbp.preprocessing import bed2fa


def test_bed2fa_from_file():
    cwd = os.getcwd()
    relative_path = "/preprocessing"
    bed_path = cwd.replace(
        relative_path, "/data/test_bed.bed")

    reference_path = cwd.replace(
        relative_path, "/data/test_reference.fa")

    assert os.path.exists(bed_path)
    assert os.path.exists(reference_path)

    expeted_output = ["AACTTCCAAG", "TTTGTCCTTTCTAGTTCTGT",
                      "GAGCTTTTGT", "TTTGTCCTTTCTAGTTCTGTGCATAGGTGCTGCCT", "ACTT"]
    actual_output = bed2fa.get_fasta(bed_path, reference_path)
    assert actual_output.sequence.tolist() == expeted_output


def test_from_dataframe():
    cwd = os.getcwd()
    relative_path = "/preprocessing"
    reference_path = cwd.replace(
        relative_path, "/data/test_reference.fa")

    assert os.path.exists(reference_path)
    bed_string = io.StringIO(
        "test\t10\t20\tint1\t.\t+\ntest\t30\t50\tint2\t.\t+\ntest\t25\t35\tint3\t.\t+\ntest\t30\t65\tint4\t.\t+\ntest\t11\t15\tint5\t.\t+\n")
    intervals = pd.read_csv(bed_string, sep="\t")
    expeted_output = [
        "TTTGTCCTTTCTAGTTCTGT",
        "GAGCTTTTGT",
        "TTTGTCCTTTCTAGTTCTGTGCATAGGTGCTGCCT",
        "ACTT"
    ]

    actual_output = bed2fa.get_fasta(intervals, reference_path)
    assert actual_output.sequence.tolist() == expeted_output
