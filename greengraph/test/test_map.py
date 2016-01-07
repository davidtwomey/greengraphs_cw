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

#Test Map(object) class method green()		
def test_green():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_map.yaml')) as fixtures_file:
		fixtures = yaml.load(fixtures_file)['green']
		for fixture in fixtures:
			lat = fixture.pop('lat')
			longs = fixture.pop('longs')
			satellite = fixture.pop('satellite')
			zoom = fixture.pop('zoom')
			size = tuple(fixture.pop('size'))
			threshold = fixture.pop('threshold')
			answer = fixture.pop('answer')
			
			geo = Map(lat, longs, satellite, zoom, size)
			assert_equal(sum(sum(geo.green(threshold)==True)), size[0]*size[1])

#Test Map(object) class	method count_green()		
def test_count_green():
    vals = range(1,100)
    m = Map(10.,15.)
    for val in vals:
        pixels = ([[0.,1.,0.]] * val) + ([[1.,1.,1.]] * (100-val))
        pixels = np.array(pixels, dtype='float32')
        pixels = pixels.reshape(10,10,3)
        m.pixels = pixels
        assert_equal(m.count_green(), val)
	print pixels
	