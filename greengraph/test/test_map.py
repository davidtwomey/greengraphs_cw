import yaml
import os
import numpy as np

from mock import patch

from ..greengraph import Greengraph
from ..map import Map
from nose.tools import assert_equal, assert_raises

# Test Map(object) class initialisation

@patch('requests.get')
@patch('matplotlib.image.imread')
def test_map(mock_imread,mock_get):
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_map.yaml')) as fixture_file:
		fixtures = yaml.load(fixture_file)['init']
	for fix in fixtures:
		lat = fix.pop('lat')
		long = fix.pop('long')
		url = fix.pop('url')
		map = Map(lat,long)
		param = fix.pop('params')
		mock_get.assert_called_with(url,params=param)