from greengraph.command import parser, process
from mock import mock_open, patch

# Test command line input arguments
def test_command():
    args = parser.parse_args(['--from','London','--to','Paris','--steps','15','--out','file_name'])
    assert args.startLoc == 'London'
    assert args.endLoc == 'Paris'
    assert args.steps == 15
    assert args.out == 'file_name'

    
@patch('greengraph.command.process')
@patch('greengraph.command.parser.parse_args',return_value='test')
def test_process(mock_parse, mock_process):
    process()
    assert mock_parse.called == True
    mock_thing.assert_called_with('test')
    
    