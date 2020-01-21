from argparse import ArgumentParser


def get_argument_parser(input_option=True, output_option=True, verbose_option=True):
    """Return argparser.ArgumentParser() with defaults used at RBP Bioinformatics

    Parameters:
        input_option (bool): Whether to include '--input_file' option, or not
        output_option (bool): Whether to include '--output_file' option, or not
        verbose_option (bool): Whether to include '--verbose' and '--quiet' options, or not
    """
    parser = ArgumentParser()

    if input_option:
        parser.add_argument('--input_file', '-i', type=str, help='Input file, ommit for STDIN', default='-')
    if output_option:
        parser.add_argument('--output_file', '-o', type=str, help='Output file, ommit for STDOUT', default='-')
    if verbose_option:
        parser.add_argument('--verbose', '-v', help='Make lots of noise [default]', dest='verbose', action='store_true')
        parser.add_argument('--quiet', '-q', help='Be vewwy quiet (I\'m hunting wabbits)', dest='verbose', action='store_false')
        parser.set_defaults(verbose=True)

    return parser
