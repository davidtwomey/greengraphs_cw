from greengraph.command import parser, process, build_greengraph
from mock import mock_open, patch


# Test command line input arguments
def test_command_args():
    args = parser.parse_args(['--from','London','--to','Paris','--steps','15','--out','file_name'])
    assert args.startLoc == 'London'
    assert args.endLoc == 'Paris'
    assert args.steps == 15
    assert args.out == 'file_name'

    
@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.plot')
@patch('greengraph.greengraph.Map.show_green',return_value='Test')
@patch('greengraph.greengraph.Map.count_green')
@patch('matplotlib.image.imread')
@patch('requests.get')
@patch('greengraph.greengraph.Greengraph.location_sequence',return_value=[(10.,10.),(15.,15.)])
@patch('greengraph.greengraph.Greengraph.geolocate', return_value=(10.,10))
def test_build_greengraph(mock_geolocate,mock_location_sequence,mock_get,mock_imread,mock_count_green,mock_show_green,mock_plot, mock_savefig,mock_show):
    args = parser.parse_args(['--from','London','--to','Paris','--steps','1','--out','file_name'])
    build_greengraph(args)
    mock_location_sequence.assert_called_with((10.,10.),(10.,10.),1)
    assert mock_count_green.called == True

@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.plot')    
@patch('greengraph.greengraph.Greengraph.green_between', return_value = 'Test')    
def test_build_greengraph_steps(mock_green_between,mock_savefig,mock_plot,mock_show):
    args = parser.parse_args(['--to','London','--from','Amsterdam'])
    build_greengraph(args)
    mock_green_between.assert_called_with(20)


    
@patch('greengraph.command.build_greengraph')
@patch('greengraph.command.parser.parse_args',return_value='test')
def test_process(mock_parse, mock_build_greengraph):
    process()
    assert mock_parse.called == True
    mock_build_greengraph.assert_called_with('test')
    
    