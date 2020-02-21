import io
import pytest
import pandas as pd
from pathlib import Path
from rbp.preprocessing import bed2fa

test_data_dir = Path(__file__).parents[0] / '..' / 'data'


def test_bed2fa_from_file():
    bed_path = test_data_dir / 'test_bed.bed'
    reference_path = test_data_dir / 'test_reference.fa'

    assert bed_path.exists()
    assert reference_path.exists()

    expeted_output = ["AACTTCCAAG", "TTTGTCCTTTCTAGTTCTGT",
                      "GAGCTTTTGT", "TTTGTCCTTTCTAGTTCTGTGCATAGGTGCTGCCT", "ACTT"]
    actual_output = bed2fa.get_fasta(str(bed_path), str(reference_path))
    assert actual_output.sequence.tolist() == expeted_output

    actual_output2 = bed2fa.get_fasta(str(bed_path), str(reference_path), tab=False)
    expeted_output2 = ">int1::test:10-20(+)\nAACTTCCAAG"
    assert actual_output2[:31] == expeted_output2


def test_from_dataframe():
    reference_path = test_data_dir / 'test_reference.fa'

    assert reference_path.exists()
    bed_string = io.StringIO(
        "test\t10\t20\tint1\t.\t+\ntest\t30\t50\tint2\t.\t+\ntest\t25\t35\tint3\t.\t+\ntest\t30\t65\tint4\t.\t+\ntest\t11\t15\tint5\t.\t+\n")
    intervals = pd.read_csv(bed_string, sep="\t")
    expeted_output = [
        "TTTGTCCTTTCTAGTTCTGT",
        "GAGCTTTTGT",
        "TTTGTCCTTTCTAGTTCTGTGCATAGGTGCTGCCT",
        "ACTT"
    ]

    actual_output = bed2fa.get_fasta(intervals, str(reference_path))
    assert actual_output.sequence.tolist() == expeted_output


def test_fails_on_wrong_type():
    with pytest.raises(TypeError):
        bed2fa.get_fasta(float(1), pd.DataFrame())
