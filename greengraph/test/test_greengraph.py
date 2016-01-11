import yaml
import os
import numpy as np

from mock import patch

from ..greengraph import Greengraph
from nose.tools import assert_raises, assert_equal, assert_almost_equal
import mock
from matplotlib import image as img
import requests
from ..map import Map

# Test Greengraph(object) class initialisation
def test_Greengraph():
	"""Tests the initialisation of Greengraph"""
	mygraph = Greengraph('London','Oxford')
	assert_equal(mygraph.start, 'London')
	assert_equal(mygraph.end, 'Oxford')
	
# Test Greengraph(object) class method geolocate()
@patch('greengraph.greengraph.Greengraph.geolocate')
def test_geolocate_valid(mock_geolocate):
    with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
        fixtures =yaml.load(fixture_file)['geolocate']
    for fix in fixtures:
        location = fix.pop('location')
        ans_lat = fix.pop('ans_lat')
        ans_long = fix.pop('ans_long')
        answer = (ans_lat, ans_long)
        geo = Greengraph(0.0, 0.0)
        mock_geolocate.return_value = (ans_lat,ans_long)
        assert_equal(geo.geolocate(location), answer)
        print mock_geolocate

# Test Greengraph(object) class method location_sequence()
@patch('greengraph.map.Map.count_green')
@patch('greengraph.greengraph.Greengraph.geolocate',return_value = (50.,10.))
def test_location_sequence(mock_geolocate,mock_map):
    with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
        fixtures = yaml.load(fixture_file)['location_sequence']
    for fix in fixtures:
        start = fix.pop('start')
        end = fix.pop('end')
        steps = fix.pop('steps')
        ans = np.array(fix.pop('ans'))
        mock_graph = Greengraph(0.0, 0.0)
        return_val = mock_graph.location_sequence(start,end,steps)
        print ans
        np.testing.assert_array_equal(return_val, ans)

# Test Greengraph(object) class method green_between()
@mock.patch.object(img, 'imread')
@mock.patch.object(requests, 'get')
@mock.patch.object(Greengraph, 'geolocate')
@mock.patch.object(Map, 'count_green')
def test_green_between(mock_geolocate,mock_count_green,mock_get,mock_imread):
    with open(os.path.join(os.path.dirname(__file__),'fixtures','sample_greengraph.yaml')) as fixture_file:
                fixtures = yaml.load(fixture_file)['green_between']
    for fix in fixtures:
        start = fix.pop('start')
        end = fix.pop('end')
        steps = fix.pop('steps')
        start_loc = fix.pop('start_loc')
        end_loc = fix.pop('end_loc')
        green_counts = fix.pop('green_counts')
        # Tell mocks the output of functions for input 
        mock_count_green.side_effect = [start_loc,end_loc]
        mock_geolocate.side_effect =green_counts
        # Num of green pixels for each step
        green_px = Greengraph(start,end).green_between(steps)
        # Check that output is as predicted
        assert_equal(green_px, green_counts) 

@patch('greengraph.map.Map.count_green')
@patch('greengraph.greengraph.Greengraph.geolocate',return_value = (50.,10.))
def test_green_between_mock(mock_geolocate, mock_map):
    Greengraph('10.,10.','50.,50.').green_between(2)
    assert mock_map.call_count == 2

def test_max_limit():
    with assert_raises(RuntimeError):
        while True:
            Greengraph(0.0, 0.0).geolocate('Lapland')