from greengraph.command import parser, process
from mock import mock_open, patch


def test_filename():
    args = parser.parse_args(['--from','London','--to','Paris','--out','file_name'])
    assert args.out == 'file_name'

