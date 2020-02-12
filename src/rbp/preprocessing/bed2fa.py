import pandas as pd
from pybedtools import BedTool
import io
from typing import Union


def get_fasta(intervals: Union[str, pd.DataFrame], reference: str, tab: bool = True, s: bool = True, name: bool = True) -> Union[pd.DataFrame, str]:
    """ Return fasta sequences of each input interval.

        This functions integrates pyBedTools (https://daler.github.io/pybedtools/).

        Returns pd.DataFrame if tab==True, else read file obj.
    Args:
        intervals: BED file path or pd.DataFrame like obj.
        reference: path to reference genome.
        tab: output fasta tab format.
        s: force strandedness.
        name: Use the “name” column in the BED file for the FASTA headers in the output FASTA file.

    Returns:
        A pd.DataFrame of sequences for each input interval.
    """
    if isinstance(intervals, str):
        assert intervals.endswith('bed'), 'required BED-6 file as input file'
        bed_obj = BedTool(intervals)  # creates bedtool obj
    elif isinstance(intervals, pd.core.frame.DataFrame) == True:
        bed_obj = BedTool.from_dataframe(intervals)  # creates bedtool obj
    else:
        raise TypeError("Input must be BED file or Pandas DataFrame")

    ref_obj = BedTool(reference)  # creates reference obj

    a = bed_obj.sequence(fi=ref_obj, tab=tab, s=s,
                         name=name)  # retrive sequences

    if tab:
        seq_tab = pd.read_csv(
            a.seqfn, header=None, names=["fasta_id", "sequence"], sep="\t"
        )
        seq_tab["sequence"] = seq_tab["sequence"].str.upper()
        return seq_tab  # return Pandas df of name,sequences
    else:
        with open(a.seqfn, 'r') as fi:
            return fi.read()  # return whole FASTA file


if __name__ == "__main__":
    pass
