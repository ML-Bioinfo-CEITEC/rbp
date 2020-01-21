from rbp.utils import get_argument_parser


def test_argument_parser():
    parser = get_argument_parser()

    # parser.__dict__['_option_string_actions'] contains all possible options
    all_options = parser.__dict__['_option_string_actions']
    assert '--input_file' in all_options
    assert '--output_file' in all_options
    assert '--verbose' in all_options
    assert '--quiet' in all_options
    assert '--help' in all_options
