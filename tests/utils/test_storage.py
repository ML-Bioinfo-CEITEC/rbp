from io import StringIO
from tempfile import NamedTemporaryFile
from rbp.utils import get_input_file, get_output_file


# mock arguments
class ArgParserMock(object):
    pass


args = ArgParserMock()


def test_stdin_input(monkeypatch):
    input_file_mock = StringIO('1234\n')
    args.input_file = "-"
    monkeypatch.setattr('sys.stdin', input_file_mock)

    input = get_input_file(args).readlines()
    assert input == ['1234\n']


def test_file_input():
    tempfile = NamedTemporaryFile()
    args.input_file = tempfile.name
    with open(tempfile.name, "w") as fw:
        fw.write('4567\n')

    input = get_input_file(args).readlines()
    assert input == ['4567\n']


def test_stdout_output(capsys):
    args.output_file = "-"

    output_handle = get_output_file(args)
    output_handle.writelines(['3124\n'])

    captured_stdout, _ = capsys.readouterr()
    print(captured_stdout)

    assert captured_stdout == '3124\n'


def test_file_output():
    tempfile = NamedTemporaryFile()
    args.output_file = tempfile.name

    output_handle = get_output_file(args)
    with output_handle as fw:
        fw.write('7890\n')

    output = open(tempfile.name, "r").readlines()
    assert output == ['7890\n']
