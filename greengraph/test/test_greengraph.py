import yaml
import os
import numpy as np

from mock import patch

from ..greengraph import Greengraph
from nose.tools import assert_raises, assert_equal, assert_almost_equal



# Test Greengraph(object) class initialisation
def test_Greengraph():
	"""Tests the initialisation of Greengraph"""
	mygraph = Greengraph('London','Oxford')
	assert_equal(mygraph.start, 'London')
	assert_equal(mygraph.end, 'Oxford')
	
# Test Greengraph(object) class method geolocate()
def test_geolocate_valid():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
		fixtures =yaml.load(fixture_file)['geolocate']
	for fix in fixtures:
		location = fix.pop('location')
		ans_lat = fix.pop('ans_lat')
		ans_long = fix.pop('ans_long')
		answer = (ans_lat, ans_long)
		geo = Greengraph(0.0, 0.0)
		assert_equal(geo.geolocate(location), answer)

# Test Greengraph(object) class method location_sequence()
def test_location_sequence():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
		fixtures = yaml.load(fixture_file)['location_sequence']
	for fix in fixtures:
		start = fix.pop('start')
		end = fix.pop('end')
		steps = fix.pop('steps')
		answer = fix.pop('answer')
		geo = Greengraph(0.0, 0.0)
		return_val = geo.location_sequence(geo.geolocate(start), geo.geolocate(end), steps)
		answer = np.array(answer)
		np.testing.assert_array_equal(return_val, answer)
	
# Test Greengraph(object) class method green_between()	
def test_green_between():
	with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
                fixtures = yaml.load(fixture_file)['green_between']
	for fix in fixtures:
		start = fix.pop('start')
		end = fix.pop('end')
		steps = fix.pop('steps')
		answer = fix.pop('answer')
		geo = Greengraph(start, end)
		assert_equal(geo.green_between(steps), answer)

@patch('greengraph.map.Map.count_green')
@patch('greengraph.greengraph.Greengraph.geolocate',return_value = (50.,10.))
def test_green_between_mock(mock_geolocate, mock_map):
    Greengraph('10.,10.','50.,50.').green_between(2)
    assert mock_map.call_count == 2

def test_max_limit():
    with assert_raises(RuntimeError):
        while True:
            Greengraph(0.0, 0.0).geolocate('Lapland')